import pygame
import pygame_gui


class CamposUi:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.manager = pygame_gui.UIManager((screen_width, screen_height))
        self.base_x = 920
        self.turno_actual = "Jugador 1"
        self.ultimo_movimiento = ""

    def dibujar_elementos(self):
        """Crea todos los elementos de la interfaz"""

        # Campo de entrada para movimientos
        self.campo_movimiento = pygame_gui.elements.UIDropDownMenu(
            options_list=range(0, 23),
            starting_option="0",
            relative_rect=pygame.Rect(self.base_x, 80, 200, 30),
            manager=self.manager,
        )

        # Botón para ejecutar movimiento
        self.boton_mover = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.base_x, 50, 100, 30),
            text="Mover",
            manager=self.manager,
        )

        # Label para mostrar el turno actual
        self.label_turno = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(self.base_x, 100, 200, 30),
            text=f"Turno: {self.turno_actual}",
            manager=self.manager,
        )

        # Label para mostrar mensajes/estado
        self.label_mensaje = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(self.base_x, 140, 300, 30),
            text="Ingresa tu movimiento",
            manager=self.manager,
        )

        # Label para mostrar dados (futuro)
        self.label_dados = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(self.base_x, 100, 150, 30),
            text="Dados: -",
            manager=self.manager,
        )

    def dibujar(self, screen):
        """Dibuja todos los elementos en la pantalla"""
        self.manager.draw_ui(screen)
