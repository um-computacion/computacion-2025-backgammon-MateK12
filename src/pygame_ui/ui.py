import pygame
import sys
from src.core.models.backgammon.backgammon import Backgammon
from src.pygame_ui.Tablero_UI import TableroUI
from src.core.models.tablero.Tablero import Tablero
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.pygame_ui.CamposUI.camposUI import CamposUi

WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 700
BROWN_LIGHT = (222, 184, 135)

class BackgammonUI:
    def __init__(self):
        pygame.init()
        self.__backgammon = Backgammon()
        self.__tablero = Tablero(self.__backgammon.inicializar_tablero())  
        self.__tablero_ui = TableroUI(self.__tablero)
        self.__running = True
        self.__campos_ui = CamposUi(1000, 700)
        self.__screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.__screen.fill(BROWN_LIGHT)

        pygame.display.set_caption("Backgammon")
    

    def jugar(self):
        """Loop principal del juego"""
        clock = pygame.time.Clock()
        time_delta = clock.tick(60) / 1000.0

        while self.__running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                
                self.__campos_ui.manager.process_events(event)
            self.__campos_ui.manager.update(time_delta)
            self.__screen.fill(BROWN_LIGHT)
            self.__campos_ui.dibujar_elementos()
            self.__campos_ui.dibujar(self.__screen)
            self.__tablero_ui.dibujar_tablero(self.__screen)
            pygame.display.flip()
            clock.tick(60)  # 60 FPS
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    # Crear y ejecutar la aplicación
    app = BackgammonUI()
    app.jugar()
