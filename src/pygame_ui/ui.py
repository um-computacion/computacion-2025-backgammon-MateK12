import pygame
import sys

import pygame_gui
from src.core.interfaces.JuegoInterfazMovimientos import IJuegoInterfazMovimientos
from src.core.interfaces.PuedeHacerMovimiento import IPuedeHacerMovimiento
from src.core.models.backgammon.backgammon import Backgammon
from src.pygame_ui.Tablero_UI.Tablero_UI import TableroUI
from src.core.models.tablero.Tablero import Tablero
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.NingunMovimientoPosible import NingunMovimientoPosible
from src.core.exceptions.CasillaOcupadaException import CasillaOcupadaException
from src.core.exceptions.NoHayFichaEnTriangulo import NoHayFichaEnTriangulo
from src.core.exceptions.MovimientoNoJustoParaGanar import MovimientoNoJustoParaGanar
from src.core.exceptions.SeleccionDadoInvalida import SeleccionDadoInvalida
from src.core.exceptions.SeleccionTrianguloInvalida import SeleccionTrianguloInvalida
from src.pygame_ui.CamposUI.camposUI import CamposUi
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador
from src.core.models.dado.Dados import Dados
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.pygame_ui.Cartel_UI.Cartel_UI import Cartel_UI
from src.core.models.backgammon.Backgammon_Turnos import Backgammon_Turnos
from src.core.exceptions.NoPuedeLiberarException import NoPuedeLiberarException
from src.core.interfaces.CartelUI import ICartelUI
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 700
BROWN_LIGHT = (222, 184, 135)
RED = (255, 0, 0)
INFO_COLOR = (128, 128, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
class BackgammonUI(IJuegoInterfazMovimientos, IPuedeHacerMovimiento):
    def __init__(
        self,
        backgammon: Backgammon,
        tableroUI: TableroUI,
        camposUi: CamposUi,
        surface: pygame.Surface,
        cartel_UI: ICartelUI,
    ):
        pygame.init()
        self.__backgammon = backgammon
        self.__tablero_ui = tableroUI
        self.__campos_ui = camposUi
        self.__screen = surface
        self.__screen.fill(BROWN_LIGHT)
        self.__dados_tirados: bool = False
        self.__cartel_UI = cartel_UI
        pygame.display.set_caption("Backgammon")

    def tirar_dados(self):
        if self.__dados_tirados:
            return
        resultado = self.__backgammon.dados.tirar_dados()
        self.__campos_ui.dados_actuales = resultado
        self.__backgammon.dados_disponibles = resultado
        self.__dados_tirados = True
        self.puede_hacer_algun_movimiento()

    def actualizar_tablero_ui(self, time_delta: float):
        self.__tablero_ui.tablero = self.__backgammon.tablero
        self.__campos_ui.manager.update(time_delta)
        self.__screen.fill(BROWN_LIGHT)
        self.__campos_ui.dibujar_campos(self.__screen)
        self.__tablero_ui.dibujar_tablero(self.__screen)
        self.__cartel_UI.actualizar_y_dibujar(self.__screen)
        pygame.display.flip()

    def realizar_movimiento(self):
        """Procesa el movimiento del jugador"""
        dado = self.__campos_ui.get_dado_seleccionado()
        triangulo = self.__campos_ui.get_seleccion_triangulo()
        if self.__backgammon.hay_fichas_comidas():
            self.__backgammon.mover_ficha_comida(dado)
        else:
            self.__backgammon.mover_ficha(int(triangulo), dado)
        self.__campos_ui.dados_actuales = self.__backgammon.dados_disponibles
        self.__campos_ui.fichas_comidas = self.__backgammon.tablero.fichas_comidas

    def jugar(self):
        """Loop principal del juego"""
        clock = pygame.time.Clock()
        self.quien_empieza()
        self.__campos_ui.turno_actual = self.__backgammon.turnero.turno
        self.tirar_dados()
        self.actualizar_tablero_ui(0)
        while not self.__backgammon.hay_ganador():
            try:
                time_delta = clock.tick(60) / 1000.0
                self.tirar_dados()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if (
                        event.type == pygame_gui.UI_BUTTON_START_PRESS
                        and event.ui_element == self.__campos_ui.boton_mover
                    ):
                        self.realizar_movimiento()
                        if self.__backgammon.dados_disponibles:
                            self.puede_hacer_algun_movimiento()
                    self.__campos_ui.manager.process_events(event)
                if not self.__backgammon.dados_disponibles:
                    self.cambiar_turno()
                self.actualizar_tablero_ui(time_delta)
            except (
                NingunMovimientoPosible,
                NoHayFichaEnTriangulo,
                MovimientoNoJustoParaGanar,
                CasillaOcupadaException,
                SeleccionDadoInvalida,
                SeleccionTrianguloInvalida,
                NoPuedeLiberarException
            ) as e:
                if not self.__backgammon.hay_ganador():
                    self.__cartel_UI.mostrar_cartel(str(e), duracion=5.0,titulo="Error", color_fondo=RED, color_texto=WHITE)
        self.mostrar_ganador()
        pygame.quit()
        sys.exit()

    def puede_hacer_algun_movimiento(self):
        """Verifica si el jugador actual puede hacer algún movimiento con los dados disponibles, si puede retorna True, si no puede lanza una excepción
        Raises: NingunMovimientoPosible
        """
        tipo = self.__backgammon.turnero.turno
        try:
            self.__backgammon.puede_mover_ficha(tipo, self.__backgammon.dados_disponibles)
        except NingunMovimientoPosible as e:
            self.__backgammon.dados_disponibles = []
            raise NingunMovimientoPosible(e)

    def cambiar_turno(self):
        """Cambia el turno al siguiente jugador dejando los parametros en su estado correspondiente"""
        self.__backgammon.turnero.cambiar_turno()
        self.__campos_ui.turno_actual = self.__backgammon.turnero.turno
        self.__dados_tirados = False

    def mostrar_ganador(self):
        """Muestra el ganador en la UI"""
        ganador = self.__backgammon.hay_ganador()
        if ganador == TipoFicha.ROJA.value:
            self.__cartel_UI.mostrar_cartel(
                "¡El jugador Rojo ha ganado!", duracion=5.0, titulo="Ganador", color_fondo=GREEN, color_texto=WHITE
            )
        elif ganador == TipoFicha.NEGRA.value:
            self.__cartel_UI.mostrar_cartel(
                "¡El jugador Negro ha ganado!", duracion=5.0, titulo="Ganador", color_fondo=GREEN,color_texto=WHITE
            )
        fin_ms = pygame.time.get_ticks() + 5000
        clock = pygame.time.Clock()
        while pygame.time.get_ticks() < fin_ms:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                self.__campos_ui.manager.process_events(event)
            self.actualizar_tablero_ui(time_delta)

    def quien_empieza(self):
        """Determina quien empieza el juego"""
        dados = self.__backgammon.turnero.quien_empieza()
        title = ("Rojo" if self.__backgammon.turnero.turno == TipoFicha.ROJA.value else "Negro")
        self.__cartel_UI.mostrar_cartel(
            titulo='Empieza: {}'.format(title),
            duracion=5.0,
            mensaje='Rojo: {} y Negro: {}'.format(dados[0], dados[1]),
            color_fondo=INFO_COLOR,
            color_texto=WHITE
            )

def main():
    tablero = Tablero(Tablero_inicializador.inicializar_tablero(), Tablero_Validador())
    turnero = Backgammon_Turnos(Dados())
    backgammon = Backgammon(tablero, Dados(), turnero)
    tableroUi = TableroUI(tablero)
    camposUi = CamposUi(WINDOW_WIDTH, WINDOW_HEIGHT)
    pantalla = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    cartelUi = Cartel_UI((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    app = BackgammonUI(
        backgammon, tableroUi, camposUi, pantalla, cartelUi
    )
    app.jugar()


if __name__ == "__main__":
    main()
