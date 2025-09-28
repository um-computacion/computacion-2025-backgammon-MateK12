import pygame
import pygame_gui
from pygame.font import Font
from src.core.enums.TipoFicha import TipoFicha
ELEMENT_WIDTH = 250
LABEL_WIDTH = 200
BUTTON_WIDTH = 150
LABEL_COLOR = (0,0,0)
class CamposUi:
    def __init__(self, screen_width, screen_height,dados_actuales: list[int]):
        self.__screen_width = screen_width
        self.__screen_height = screen_height

        self.__dados_actuales = dados_actuales

        self.__manager = pygame_gui.UIManager((screen_width, screen_height))
        self.__base_x = 920
        self.__turno_actual:int = None
        self.__boton_mover = None
        self.__font = Font(None, 36)
        
        self.__text_triangulo = None
        self.__text_dado = None
        self.__text_turno = None
        self.__elementos_creados = False
        
    @property
    def manager(self):
        return self.__manager
    @property
    def elementos_creados(self):
        return self.__elementos_creados
    @property
    def turno_actual(self):
        return self.__turno_actual
    @turno_actual.setter
    def turno_actual(self, value:TipoFicha):
        self.__turno_actual = value
    @property
    def boton_mover(self):
        return self.__boton_mover
    @property
    def dados_actuales(self):
        return self.__dados_actuales
    @dados_actuales.setter
    def dados_actuales(self, dados: list[int]):
        self.__dados_actuales = dados
        # if self.select_dado:
        #     self.select_dado.kill()
        #     self.select_dado = None
        #     self.__text_dado = None
        #     self.__elementos_creados = False
    
    def __crear_elementos(self):
        """Crea todos los elementos de la interfaz"""
        if self.__elementos_creados:
            return
        y_offset = 50  
        spacing = 50   
        
        self.select_triangulo = pygame_gui.elements.UIDropDownMenu(
            options_list=[str(i) for i in range(0, 24)],  
            starting_option="0",
            relative_rect=pygame.Rect(self.__base_x, y_offset + 30, ELEMENT_WIDTH, 35),
            manager=self.__manager,
        )
        
        y_offset += spacing + 30  

        self.__text_dado = self.__font.render('Seleccionar Dado:', True, LABEL_COLOR)

        opciones_dados = [f"Dado {i+1}: {valor}" for i, valor in enumerate(self.__dados_actuales)]
        self.select_dado = pygame_gui.elements.UIDropDownMenu(
            options_list=opciones_dados,
            starting_option=opciones_dados[1],
            relative_rect=pygame.Rect(self.__base_x, y_offset + 30, ELEMENT_WIDTH, 35),
            manager=self.__manager,
        )
        
        y_offset += spacing + 30

        self.__boton_mover = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.__base_x, y_offset, BUTTON_WIDTH, 40),
            text="Realizar Movimiento",
            manager=self.__manager,
        )
        
        y_offset += spacing + 10

        self.__text_turno = self.__font.render(self.__get_text_turno(), True, LABEL_COLOR)
        
        y_offset += 40


        self.__text_triangulo = self.__font.render('Seleccione un triangulo', True, LABEL_COLOR)
        self.__elementos_creados = True

    def __dibujar_textos(self, screen):
        """Dibuja todos los elementos en la pantalla"""
        y_offset = 50
        spacing = 50
        
        if self.__text_triangulo:
            screen.blit(self.__text_triangulo, (self.__base_x, y_offset))
        
        y_offset += spacing + 30
        
        if self.__text_dado:
            screen.blit(self.__text_dado, (self.__base_x, y_offset))
        
        y_offset += spacing + 30 + spacing + 10
        
        if self.__text_turno:
            screen.blit(self.__text_turno, (self.__base_x,10))
        
        y_offset += 40
        
        
    def __get_text_turno(self)-> str:
        '''Obtiene el texto del turno actual
            Returns: str: Texto del turno actual
        '''
        if self.__turno_actual == TipoFicha.ROJA.value:
            return "Turno del jugador Rojo"
        elif self.__turno_actual == TipoFicha.NEGRA.value:    
            return "Turno del jugador Negro"
    def get_dado_seleccionado(self) -> int | None:
        if self.select_dado and self.select_dado.selected_option:
            (valor,_) =self.select_dado.selected_option
            valor = valor.split(': ')[1]
            return int(valor)
        return None
    def get_seleccion_triangulo(self) -> int:
        """Obtiene el triángulo seleccionado"""
        if self.select_triangulo:
            (valor,_) =self.select_triangulo.selected_option
            return int(valor)
        return None

    def dibujar_campos(self, screen):
        """Dibuja todos los elementos en la pantalla"""
        self.__dibujar_textos(screen)
        self.__crear_elementos()
        self.__manager.draw_ui(screen)
