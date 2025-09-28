import pygame
import sys
from src.core.interfaces.JuegoInterfazMovimientos import IJuegoInterfazMovimientos
from src.core.models.backgammon.backgammon import Backgammon
from src.pygame_ui.Tablero_UI import TableroUI
from src.core.models.tablero.Tablero import Tablero
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.pygame_ui.CamposUI.camposUI import CamposUi
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador
from src.core.models.dado.Dados import Dados
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 700
BROWN_LIGHT = (222, 184, 135)


class BackgammonUI(IJuegoInterfazMovimientos):
    def __init__(self,backgammon:Backgammon, tablero:Tablero,tableroUI:TableroUI,camposUi:CamposUi,surface:pygame.Surface):
        pygame.init()
        self.__backgammon = backgammon
        self.__tablero = tablero
        self.__tablero_ui = tableroUI
        self.__running = True
        self.__campos_ui = camposUi
        self.__screen = surface
        self.__screen.fill(BROWN_LIGHT)

        pygame.display.set_caption("Backgammon")
    

    def jugar(self):
        """Loop principal del juego"""
        clock = pygame.time.Clock()
        time_delta = clock.tick(60) / 1000.0
        self.__backgammon.quien_empieza()
        self.__campos_ui.turno_actual = self.__backgammon.turno
        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                self.__campos_ui.manager.process_events(event)
            self.__campos_ui.manager.update(time_delta)
            self.__screen.fill(BROWN_LIGHT)
            self.__campos_ui.dibujar_campos(self.__screen)
            self.__tablero_ui.dibujar_tablero(self.__screen)
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    def puede_hacer_algun_movimiento(self):
        pass

if __name__ == "__main__":
    tablero = Tablero(Tablero_inicializador.inicializar_tablero(),Tablero_Validador())
    backgammon = Backgammon(tablero,Dados())
    tableroUi = TableroUI(tablero)
    camposUi = CamposUi(1500, 700,[1,2])
    pantalla = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    app = BackgammonUI(backgammon, tablero, tableroUi, camposUi, pantalla)
    app.jugar()
