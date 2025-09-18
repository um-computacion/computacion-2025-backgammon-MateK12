import pygame
import math
import random
import sys

pygame.init()

# Constantes
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
BOARD_WIDTH = 800
BOARD_HEIGHT = 600
BOARD_X = 100
BOARD_Y = 50

# Colores
BLACK = (50, 50, 50)
BROWN_LIGHT = (222, 184, 135)
DARK = (23, 23, 23)
RED = (139, 0, 0)
class TableroUI():
     
    def __init__(self):
        self.__ancho_tablero__ = BOARD_WIDTH
        self.__alto_tablero__ = BOARD_HEIGHT
        self.__x__ = BOARD_X #posicion x del vertice inicial del tablero 
        self.__y__ = BOARD_Y
        self.__punto_width__ = (self.__ancho_tablero__ - 100) // 12  # 100 para el bar central
        self.__punto_height__ = (self.__alto_tablero__ - 100) // 2  
        self.__screen__ = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.__screen__.fill(BROWN_LIGHT)
    
    @property
    def screen(self):
        """Getter para la pantalla"""
        return self.__screen__
    
    @property
    def punto_width(self):
        """Getter para el ancho de cada punto"""
        return self.__punto_width__
    
    @property
    def punto_height(self):
        """Getter para la altura de cada punto"""
        return self.__punto_height__
    def dibujar_triangulo(self, punto_index, color):
        """Dibuja un triángulo para un punto específico
            Si son los primeros 12 triangulos apuntan hacia abajo, si son los ultimos 12 triangulos apuntan hacia arriba
        """
        punto_x, punto_y = self.get_punto_position_base(punto_index) #obtengo el vertice base del triangulo
        
        if punto_index <= 11: # triangulo apuntando hacia abajo
            puntos = [
                (punto_x, punto_y), #vertice base del triangulo
                (punto_x + self.__punto_width__, punto_y),
                (punto_x + self.__punto_width__ // 2, punto_y + self.__punto_height__) #vertice mas alto
            ]
        else:  # triangulo apuntando hacia arriba
            puntos = [
                (punto_x, punto_y + self.__punto_height__),
                (punto_x + self.__punto_width__, punto_y + self.__punto_height__),
                (punto_x + self.__punto_width__ // 2, punto_y) #vertice mas alto
            ]
        
        pygame.draw.polygon(self.__screen__, color, puntos)
        pygame.draw.polygon(self.__screen__, BLACK, puntos, 2)
    
    def dibujar_tablero(self):
            """Dibuja el tablero completo
            Incluye el borde del tablero, el bar central y los 24 triangulos
            """
            pygame.draw.rect(self.__screen__, BLACK, (self.__x__, self.__y__, self.__ancho_tablero__, self.__alto_tablero__), 3) # Borde del tablero
            
            bar_x = self.__x__ + self.__ancho_tablero__ // 2 - 25
            pygame.draw.rect(self.__screen__, DARK, (bar_x, self.__y__, 50, self.__alto_tablero__)) #barra del medio divisoria
            
            for i in range(24): #triangulos alternando el color
                color = DARK if i % 2 == 0 else RED
                self.dibujar_triangulo( i, color)
            
        
    def get_punto_position_base(self, punto_index):
        """Obtiene la posición x, y de un triangulo especifico,
        este punto sera el base ya que en base a este punto se calularan los otros 2 vertices del triangulo"""
        
        if punto_index <= 11:  # Parte superior
            if punto_index <= 5:
                x = self.__x__ + self.__ancho_tablero__ - (punto_index + 1) * self.__punto_width__
            else:
                x = self.__x__ + self.__ancho_tablero__ - (punto_index) * self.__punto_width__ - 150   
            y = self.__y__
        else:  # Parte inferior
            if punto_index <= 17:
                x = self.__x__  + (punto_index - 12+1) * self.__punto_width__ + self.__ancho_tablero__ /2  # pos_inicial_x+ desplazamiento en x +ancho_del_tablero/2 
            else:
                x = self.__x__ + (punto_index - 18 ) * self.__punto_width__
            y = self.__y__ + self.__alto_tablero__ - 250
        
        return x, y
if __name__ == "__main__":
    pygame.display.set_caption("Tablero Backgammon")
    running = True
    
    tablero = TableroUI()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        tablero.dibujar_tablero()
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()