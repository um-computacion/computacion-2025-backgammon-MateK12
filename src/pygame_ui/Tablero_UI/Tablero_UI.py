import pygame
from src.core.enums.TipoFicha import TipoFicha
from src.core.models.tablero.Tablero import Tablero

pygame.init()

# Constantes
BOARD_WIDTH = 800
BOARD_HEIGHT = 600
BOARD_X = 100
BOARD_Y = 50


# Colores
# Colores para las fichas
FICHA_BORDER = (0, 0, 0)
BLACK = (50, 50, 50)
DARK = (23, 23, 23)
RED = (139, 0, 0)


class TableroUI:

    def __init__(self, tablero: Tablero):
        self.__tablero = tablero
        self.__ancho_tablero__ = BOARD_WIDTH
        self.__alto_tablero__ = BOARD_HEIGHT
        self.__x__ = BOARD_X  # posicion x del vertice inicial del tablero
        self.__y__ = BOARD_Y
        self.__punto_width__ = (
            self.__ancho_tablero__ - 100
        ) // 12  # 100 para el bar central
        self.__punto_height__ = (self.__alto_tablero__ - 100) // 2

    @property
    def tablero(self):
        """Getter para el tablero"""
        return self.__tablero
    @tablero.setter
    def tablero(self, nuevo_tablero):
        """Setter para el tablero"""
        self.__tablero = nuevo_tablero

    def dibujar_triangulo(self, punto_index:int, color:tuple, screen:pygame.Surface):
        """Dibuja un triángulo para un punto específico
        Si son los primeros 12 triangulos apuntan hacia abajo, si son los ultimos 12 triangulos apuntan hacia arriba
        """
        punto_x, punto_y = self.get_punto_position_base(
            punto_index
        )  

        if punto_index <= 11:  # triangulo apuntando hacia abajo
            puntos = [
                (punto_x, punto_y),  # vertice base del triangulo
                (punto_x + self.__punto_width__, punto_y),
                (
                    punto_x + self.__punto_width__ // 2,
                    punto_y + self.__punto_height__,
                ),  # vertice mas alto
            ]
        else:  # triangulo apuntando hacia arriba
            puntos = [
                (punto_x, punto_y + self.__punto_height__),
                (punto_x + self.__punto_width__, punto_y + self.__punto_height__),
                (punto_x + self.__punto_width__ // 2, punto_y),  # vertice mas alto
            ]

        pygame.draw.polygon(screen, color, puntos)
        pygame.draw.polygon(screen, BLACK, puntos, 2)
    def __dibujar_numero_triangulo(self, punto_index:int, screen:pygame.Surface):
        """Dibuja el número del triángulo encima o debajo según corresponda"""
        font = pygame.font.Font(None, 24)
        
        base_x, base_y = self.get_punto_position_base(punto_index)
        
        text_x = base_x + self.__punto_width__ // 2
        
        if punto_index <= 11:  
            text_y = base_y - 15
        else:  
            text_y = base_y + self.__punto_height__ + 15
        
        text_surface = font.render(str(punto_index), True, BLACK)
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        
        screen.blit(text_surface, text_rect)

    def dibujar_tablero(self, screen):
        """Dibuja el tablero completo
        Incluye el borde del tablero, el bar central, los 24 triangulos y las fichas
        """
        pygame.draw.rect(
            screen,
            BLACK,
            (self.__x__, self.__y__, self.__ancho_tablero__, self.__alto_tablero__),
            3,
        )  # Borde del tablero

        barra_x = self.__x__ + self.__ancho_tablero__ // 2 - 25
        pygame.draw.rect(
            screen, DARK, (barra_x, self.__y__, 50, self.__alto_tablero__)
        )

        for i in range(24):  # triangulos alternando el color
            color = DARK if i % 2 == 0 else RED
            self.dibujar_triangulo(i, color, screen)
            self.__dibujar_numero_triangulo(i, screen)

        self.dibujar_todas_las_fichas(screen)

    def get_punto_position_base(self, punto_index):
        """Obtiene la posición x, y de un triangulo especifico,
        este punto sera el base ya que en base a este punto se calularan los otros 2 vertices del triangulo
        param punto_index: Índice del triángulo (0-23)
        return: (x, y) coordenadas del vértice base del triangulo
        """

        if punto_index <= 11:  # Parte superior
            if punto_index <= 5:
                x = (
                    self.__x__
                    + self.__ancho_tablero__
                    - (punto_index + 1) * self.__punto_width__
                )
            else:
                x = (
                    self.__x__
                    + self.__ancho_tablero__
                    - (punto_index) * self.__punto_width__
                    - 150
                )
            y = self.__y__
        else:  # Parte inferior
            if punto_index <= 17:
                x = (    self.__x__+ (punto_index - 12 + 1) * self.__punto_width__+ self.__ancho_tablero__ / 2)  # pos_inicial_x+ desplazamiento en x +ancho_del_tablero/2
            else:
                x = self.__x__ + (punto_index - 18) * self.__punto_width__
            y = self.__y__ + self.__alto_tablero__ - 250

        return x, y

    def get_punto_position_base_ficha(self, punto_index):
        """Obtiene la posición x, y de un triángulo específico,
        este punto será la base ya que en base a este punto se calcularán los otros 2 vértices del triángulo
        @param punto_index: Índice del triángulo (0-23)
        @return: (x, y) coordenadas del vértice base de la ficha
        """
        if punto_index <= 11:  # Parte superior
            if punto_index <= 5:
                x = (
                    self.__x__
                    + self.__ancho_tablero__
                    - (punto_index + 1) * self.__punto_width__
                )
            else:
                x = (
                    self.__x__
                    + self.__ancho_tablero__
                    - (punto_index) * self.__punto_width__
                    - 150
                )
            y = self.__y__
        else:  # Parte inferior
            if punto_index <= 17:
                # Triángulos 12-17 van del lado izquierdo
                x = self.__x__ + (punto_index - 12) * self.__punto_width__
            else:
                # Triángulos 18-23 van del lado derecho después del bar
                x = (
                    self.__x__
                    + (punto_index - 18) * self.__punto_width__
                    + 6 * self.__punto_width__
                    + 110
                )
            y = self.__y__ + self.__alto_tablero__ - self.__punto_height__

        return x, y

    def dibujar_ficha(self, x, y, tipo_ficha, screen):
        """Dibuja una ficha individual en la posición especificada
        @param x: Coordenada x del centro de la ficha
        @param y: Coordenada y del centro de la ficha
        @param tipo_ficha: Tipo de ficha (TipoFicha.ROJA o TipoFicha.NEGRA)
        """
        radius = 20
        color = RED if tipo_ficha == TipoFicha.ROJA.value else BLACK

        pygame.draw.circle(screen, color, (int(x), int(y)), radius)
        pygame.draw.circle(screen, FICHA_BORDER, (int(x), int(y)), radius, 2)

    def dibujar_fichas_en_punto(self, punto_index, screen):
        """Dibuja todas las fichas en un triangulo específico del tablero, validando la posición del triangulo
        @param punto_index: Índice del triángulo (0-23)
        """
        fichas = self.__tablero.tablero[punto_index]
        if not fichas:
            return
        base_x, base_y = self.get_punto_position_base_ficha(punto_index)
        punto_width = self.__punto_width__
        punto_height = self.__punto_height__

        center_x = base_x + punto_width // 2

        if punto_index <= 11:
            start_y = base_y + 30
            y_offset = 35
        else:
            start_y = base_y + punto_height - 30
            y_offset = -35

        for i, ficha in enumerate(fichas):
            ficha_y = start_y + (i * y_offset)
            self.dibujar_ficha(center_x, ficha_y, ficha.tipo, screen)

    def dibujar_todas_las_fichas(self, screen):
        """Dibuja todas las fichas en todos los puntos del tablero"""
        for punto_index in range(24):
            self.dibujar_fichas_en_punto(punto_index, screen)

