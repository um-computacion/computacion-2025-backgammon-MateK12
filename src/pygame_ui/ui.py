import pygame
import sys

import pygame_gui
from src.core.interfaces.JuegoInterfazMovimientos import IJuegoInterfazMovimientos
from src.core.interfaces.JuegoInterfazDados import IJuegoInterfazDados
from src.core.models.backgammon.backgammon import Backgammon
from src.pygame_ui.Tablero_UI import TableroUI
from src.core.models.tablero.Tablero import Tablero
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.SeleccionTrianguloInvalida import SeleccionTrianguloInvalida
from src.core.exceptions.SeleccionDadoInvalida import SeleccionDadoInvalida
from src.pygame_ui.CamposUI.camposUI import CamposUi
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador
from src.core.models.dado.Dados import Dados
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.helpers.Tablero_Impresor import Tablero_Impresor
from tkinter import messagebox
import tkinter as tk
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 700
BROWN_LIGHT = (222, 184, 135)


class BackgammonUI(IJuegoInterfazMovimientos):
    def __init__(self,backgammon:Backgammon,tableroUI:TableroUI,camposUi:CamposUi,surface:pygame.Surface):
        pygame.init()
        self.__backgammon = backgammon
        self.__tablero = backgammon.tablero
        self.__tablero_ui = tableroUI
        self.__running = True
        self.__campos_ui = camposUi
        self.__screen = surface
        self.__screen.fill(BROWN_LIGHT)
        self.__dados_disponibles: list[int] = []
        self.__dados_tirados: bool = False
        pygame.display.set_caption("Backgammon")
    
    def tirar_dados(self):
        if self.__dados_tirados:
            return 
        resultado = self.__backgammon.dados.tirar_dados()
        self.__campos_ui.dados_actuales = resultado
        self.__dados_disponibles = resultado
        self.__dados_tirados = True
        return resultado
    import tkinter as tk

    def actualizar_tablero_ui(self,time_delta:int):
        self.__campos_ui.manager.update(time_delta)
        self.__screen.fill(BROWN_LIGHT)
        self.__campos_ui.dibujar_campos(self.__screen)
        self.__tablero_ui.dibujar_tablero(self.__screen)
        pygame.display.flip()
    def realizar_movimiento(self):
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
            Tablero_Impresor.imprimir_tablero(self.__backgammon.tablero) #to do eliminar solo de prueba


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
        time_delta = clock.tick(60) / 1000.0
        self.__backgammon.quien_empieza()
        self.__campos_ui.turno_actual = self.__backgammon.turno
        while self.__running:
            self.tirar_dados()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                if event.type == pygame_gui.UI_BUTTON_START_PRESS:
                    if event.ui_element == self.__campos_ui.boton_mover:
                        try:
                            self.realizar_movimiento()
                        except Exception as e:
                            self.mostrar_error(e)
                        self.realizar_movimiento()

                self.__campos_ui.manager.process_events(event)
            self.actualizar_tablero_ui(time_delta)
        pygame.quit()
        sys.exit()
    def puede_hacer_algun_movimiento(self):
        pass
    def mostrar_error(self, mensaje: str):
        root = tk.Tk()
        root.withdraw() 
        tk.messagebox.showerror("Error", mensaje)
        root.destroy()
if __name__ == "__main__":
    tablero = Tablero(Tablero_inicializador.inicializar_tablero(),Tablero_Validador())
    backgammon = Backgammon(tablero,Dados())
    tableroUi = TableroUI(tablero)
    camposUi = CamposUi(1500, 700)
    pantalla = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    app = BackgammonUI(backgammon, tableroUi, camposUi, pantalla)
    app.jugar()
