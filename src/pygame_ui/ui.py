import pygame
import sys

import pygame_gui
from src.core.interfaces.JuegoInterfazMovimientos import IJuegoInterfazMovimientos
from src.core.interfaces.JuegoInterfazDados import IJuegoInterfazDados
from src.core.models.backgammon.backgammon import Backgammon
from src.pygame_ui.Tablero_UI.Tablero_UI import TableroUI
from src.core.models.tablero.Tablero import Tablero
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.SeleccionTrianguloInvalida import SeleccionTrianguloInvalida
from src.core.exceptions.SeleccionDadoInvalida import SeleccionDadoInvalida
from src.core.exceptions.NingunMovimientoPosible import NingunMovimientoPosible
from src.pygame_ui.CamposUI.camposUI import CamposUi
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador
from src.core.models.dado.Dados import Dados
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.pygame_ui.Cartel_UI.Cartel_UI import Cartel_UI
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 700
BROWN_LIGHT = (222, 184, 135)


class BackgammonUI(IJuegoInterfazMovimientos):
    def __init__(self,backgammon:Backgammon,tableroUI:TableroUI,camposUi:CamposUi,surface:pygame.Surface,cartel_error:Cartel_UI,cartel_victoria:Cartel_UI):
        pygame.init()
        self.__backgammon = backgammon
        self.__tablero_ui = tableroUI
        self.__campos_ui = camposUi
        self.__screen = surface
        self.__screen.fill(BROWN_LIGHT)
        self.__dados_disponibles: list[int] = []
        self.__dados_tirados: bool = False
        self.__cartel_error = cartel_error
        self.__cartel_victoria = cartel_victoria
        pygame.display.set_caption("Backgammon")
    
    def tirar_dados(self):
        if self.__dados_tirados:
            return 
        resultado = self.__backgammon.dados.tirar_dados()
        self.__campos_ui.dados_actuales = resultado
        self.__dados_disponibles = resultado
        self.__dados_tirados = True

    def actualizar_tablero_ui(self,time_delta:float):
        self.__tablero_ui.tablero = self.__backgammon.tablero
        self.__campos_ui.manager.update(time_delta)  
        self.__screen.fill(BROWN_LIGHT)
        self.__campos_ui.dibujar_campos(self.__screen)
        self.__tablero_ui.dibujar_tablero(self.__screen)
        self.__cartel_error.actualizar_y_dibujar(self.__screen)
        self.__cartel_victoria.actualizar_y_dibujar(self.__screen)
        pygame.display.flip()

    def realizar_movimiento(self):
        """Procesa el movimiento del jugador"""
        self.seleccion_dado_valida()
        self.seleccion_triangulo_valida()
        dado = self.__campos_ui.get_dado_seleccionado()
        triangulo = self.__campos_ui.get_seleccion_triangulo()
        seleccion_index = self.__dados_disponibles.index(dado)
        if self.__backgammon.hay_fichas_comidas():
            self.__backgammon.mover_ficha_comida(dado)
            self.__dados_disponibles.pop(int(seleccion_index))
        else:
            self.__backgammon.mover_ficha(int(triangulo), dado)
            self.__dados_disponibles.pop(int(seleccion_index))
        self.__campos_ui.dados_actuales = self.__dados_disponibles

    def seleccion_triangulo_valida(self):
        """Valida que la selección del triángulo desde la UI sea correcta
        Raises:
            SeleccionTrianguloInvalida
        """
        if self.__campos_ui.get_seleccion_triangulo() is not None:
            return
        raise SeleccionTrianguloInvalida("Selección de triángulo inválida")
    def seleccion_dado_valida(self):
        """Valida que la selección del dado desde la UI sea correcta
        Raises:
            SeleccionDadoInvalida
        """
        if self.__campos_ui.get_dado_seleccionado() is not None:
            return True
        raise SeleccionDadoInvalida("Selección de dado inválida")
    def jugar(self):
        """Loop principal del juego"""
        clock = pygame.time.Clock()
        self.__backgammon.quien_empieza()
        self.__campos_ui.turno_actual = self.__backgammon.turno
        self.tirar_dados()
        self.actualizar_tablero_ui(0)
        while not self.__backgammon.hay_ganador():
            time_delta = clock.tick(60) / 1000.0 
            self.tirar_dados()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                if event.type == pygame_gui.UI_BUTTON_START_PRESS:
                    if event.ui_element == self.__campos_ui.boton_mover:
                        self.onMove()
                self.__campos_ui.manager.process_events(event)
            self.actualizar_tablero_ui(time_delta)
        self.mostrar_ganador()
        pygame.quit()
        sys.exit()

    def onMove(self):
        """Procesa el movimiento del jugador"""
        try:  
            self.puede_hacer_algun_movimiento()
            self.realizar_movimiento()
            if not self.__dados_disponibles:
                self.cambiar_turno()
        except Exception as e:
            self.__cartel_error.mostrar_cartel(str(e), duracion=3.0)

    def puede_hacer_algun_movimiento(self):
        """Verifica si el jugador actual puede hacer algún movimiento con los dados disponibles
        Raises: NingunMovimientoPosible
        """
        tipo = self.__backgammon.turno
        for dado in self.__dados_disponibles:
            if self.__backgammon.puede_mover_ficha(tipo, dado):
                return True
        self.__dados_disponibles = []
        raise NingunMovimientoPosible(
            "No hay movimientos posibles con los dados disponibles"
        )

    def cambiar_turno(self):
        '''Cambia el turno al siguiente jugador dejando los parametros en su estado correspondiente'''
        self.__backgammon.cambiar_turno()
        self.__campos_ui.turno_actual = self.__backgammon.turno
        self.__dados_tirados = False

    def mostrar_ganador(self):
        """Muestra el ganador en la UI"""
        ganador = self.__backgammon.hay_ganador()
        if ganador == TipoFicha.ROJA.value:
            self.__cartel_victoria.mostrar_cartel("¡El jugador Rojo ha ganado!", duracion=5.0,titulo="Ganador")
        elif ganador == TipoFicha.NEGRA.value:
            self.__cartel_victoria.mostrar_cartel("¡El jugador Negro ha ganado!", duracion=5.0,titulo="Ganador")


if __name__ == "__main__":
    tablero = Tablero(Tablero_inicializador.inicializar_tablero(),Tablero_Validador())
    backgammon = Backgammon(tablero,Dados())
    tableroUi = TableroUI(tablero)
    camposUi = CamposUi(WINDOW_WIDTH, WINDOW_HEIGHT)
    pantalla = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    cartel_error = Cartel_UI((WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    cartel_victoria = Cartel_UI((WINDOW_WIDTH/2, WINDOW_HEIGHT/2),color_fondo=(0,128,0),color_texto=(255,255,255))
    app = BackgammonUI(backgammon, tableroUi, camposUi, pantalla,cartel_error, cartel_victoria)
    app.jugar()
