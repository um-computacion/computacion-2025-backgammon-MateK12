import pygame
import pygame_gui
from pygame.font import Font
from src.core.enums.TipoFicha import TipoFicha
from src.core.models.ficha.Ficha import Ficha

ELEMENT_WIDTH = 250
LABEL_WIDTH = 200
BUTTON_WIDTH = 150
LABEL_COLOR = (0, 0, 0)


class CamposUi:
    def __init__(self, screen_width: int, screen_height: int):
        self.__screen_width = screen_width
        self.__screen_height = screen_height

        self.__dados_actuales = []

        self.__manager = pygame_gui.UIManager((screen_width, screen_height))
        self.__base_x = 920
        self.__turno_actual: int = None
        self.__boton_mover = None
        self.__font = Font(None, 36)
        self.__select_dado = None
        self.__text_triangulo = None
        self.__text_dado = None
        self.__text_turno = None
        self.__elementos_creados = False
        self.__text_fichas_comidas = None
        self.__fichas_comidas: list[Ficha] = []

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
    def turno_actual(self, value: TipoFicha):
        self.__turno_actual = value
        self.__actualizar_texto_turno()

    @property
    def boton_mover(self):
        return self.__boton_mover

    @property
    def dados_actuales(self):
        return self.__dados_actuales

    @dados_actuales.setter
    def dados_actuales(self, dados: list[int]):
        old_dados = self.__dados_actuales.copy()
        self.__dados_actuales = dados.copy()
        if self.__elementos_creados and old_dados != dados:
            self.__actualizar_dropdown_dados()

    @property
    def fichas_comidas(self):
        return self.__fichas_comidas

    @fichas_comidas.setter
    def fichas_comidas(self, fichas: list[Ficha]):
        self.__fichas_comidas = fichas
        self.__text_fichas_comidas = self.__font.render(
            self.__get_text_fichas_comidas(), True, LABEL_COLOR
        )

    @property
    def select_dado(self):
        return self.__select_dado

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

        self.__text_dado = self.__font.render("Seleccionar Dado:", True, LABEL_COLOR)

        opciones_dados = [
            f"Dado {i+1}: {valor}" for i, valor in enumerate(self.__dados_actuales)
        ]
        self.__select_dado = pygame_gui.elements.UIDropDownMenu(
            options_list=opciones_dados,
            starting_option=opciones_dados[0] if opciones_dados else "No hay dados",
            relative_rect=pygame.Rect(self.__base_x, y_offset + 30, ELEMENT_WIDTH, 35),
            manager=self.__manager,
        )

        y_offset += spacing + 30

        self.__boton_mover = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.__base_x, y_offset, BUTTON_WIDTH, 40),
            text="Realizar Movimiento",
            manager=self.__manager,
        )

        # y_offset += spacing + 10

        self.__text_turno = self.__font.render(
            self.__get_text_turno(), True, LABEL_COLOR
        )

        # y_offset += 40

        self.__text_triangulo = self.__font.render(
            "Seleccione un triangulo", True, LABEL_COLOR
        )
        self.__text_fichas_comidas = self.__font.render(
            self.__get_text_fichas_comidas(), True, LABEL_COLOR
        )
        self.__actualizar_textos()

        self.__elementos_creados = True

    def __dibujar_textos(self, screen):
        """poner los textos (etiquetas) en la pantalla"""
        y_offset = 50
        spacing = 50

        if self.__text_triangulo:
            screen.blit(self.__text_triangulo, (self.__base_x, y_offset))

        y_offset += spacing + 30

        if self.__text_dado:
            screen.blit(self.__text_dado, (self.__base_x, y_offset))

        y_offset += spacing + 30 + spacing + 10

        if self.__text_turno:
            screen.blit(self.__text_turno, (self.__base_x, 10))
        if self.__text_fichas_comidas:
            screen.blit(self.__text_fichas_comidas, (self.__base_x, y_offset + 20))

        y_offset += 40

    def get_dado_seleccionado(self) -> int | None:
        if self.__select_dado and self.__select_dado.selected_option:
            (valor, _) = self.__select_dado.selected_option
            valor = valor.split(": ")[1]
            return int(valor)
        return None

    def get_seleccion_triangulo(self) -> int:
        """Obtiene el triángulo seleccionado"""
        if self.select_triangulo:
            (valor, _) = self.select_triangulo.selected_option
            return int(valor)
        return None

    def __actualizar_dropdown_dados(self):
        """Actualiza el dropdown de dados cuando cambian los dados disponibles"""
        if self.__select_dado:
            self.__select_dado.kill()
        y_offset = 50 + 50 + 30
        opciones_dados = self.__get_opciones_dados()
        self.__select_dado = pygame_gui.elements.UIDropDownMenu(
            options_list=opciones_dados,
            starting_option=opciones_dados[0] if opciones_dados else "No hay dados",
            relative_rect=pygame.Rect(self.__base_x, y_offset + 30, ELEMENT_WIDTH, 35),
            manager=self.__manager,
        )

    def __actualizar_textos(self):
        """Actualiza todas las superficies de texto"""
        self.__text_triangulo = self.__font.render(
            "Seleccione un triangulo", True, LABEL_COLOR
        )
        self.__text_dado = self.__font.render("Seleccionar Dado:", True, LABEL_COLOR)
        self.__actualizar_texto_turno()

    def __actualizar_texto_turno(self):
        """Actualiza solo el texto del turno"""
        texto_turno = self.__get_text_turno()
        if texto_turno:
            self.__text_turno = self.__font.render(texto_turno, True, LABEL_COLOR)

    def __get_opciones_dados(self) -> list[str]:
        """Obtiene las opciones para el dropdown de dados"""
        return [f"Dado {i+1}: {valor}" for i, valor in enumerate(self.__dados_actuales)]

    def __get_text_turno(self) -> str:
        """Obtiene el texto del turno actual
        Returns: str: Texto del turno actual
        """
        if self.__turno_actual == TipoFicha.ROJA.value:
            return "Turno del jugador Rojo"
        elif self.__turno_actual == TipoFicha.NEGRA.value:
            return "Turno del jugador Negro"

    def __get_text_fichas_comidas(self) -> str:
        """Obtiene el texto de las fichas comidas
        Returns: str: Texto de las fichas comidas
        """
        negras = len(
            [f for f in self.__fichas_comidas if f.tipo == TipoFicha.NEGRA.value]
        )
        rojas = len(
            [f for f in self.__fichas_comidas if f.tipo == TipoFicha.ROJA.value]
        )
        return f"Fichas comidas - Negras: {negras} Rojas: {rojas}"

    def dibujar_campos(self, screen):
        """Dibuja todos los elementos en la pantalla"""
        self.__crear_elementos()
        self.__dibujar_textos(screen)
        self.__manager.draw_ui(screen)
