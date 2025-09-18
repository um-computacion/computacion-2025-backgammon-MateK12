import pygame
import sys
from src.core.models.backgammon.backgammon import Backgammon
from src.pygame_ui.Tablero_UI import TableroUI
from src.core.models.tablero.Tablero import Tablero
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha

# Colores para las fichas
FICHA_ROJA = (139, 0, 0)
FICHA_NEGRA = (50, 50, 50)
FICHA_BORDER = (0, 0, 0)

class BackgammonUI:
    def __init__(self):
        pygame.init()
        self.backgammon = Backgammon()
        self.tablero_ui = TableroUI()
        self.screen = self.tablero_ui.screen
        self.tablero = Tablero(self.backgammon.inicializar_tablero())  
        self.running = True
        
        # Configurar la ventana
        pygame.display.set_caption("Backgammon")
        
        # Inicializar tablero con fichas de ejemplo (puedes quitar esto más tarde)
        # self._inicializar_tablero_ejemplo()
    
    # def _inicializar_tablero_ejemplo(self):
    #     """Inicializa el tablero con una configuración de ejemplo para testing"""
    #     # Agregar algunas fichas rojas en diferentes posiciones
    #     for _ in range(5):
    #         ficha_roja = Ficha(TipoFicha.ROJA)
    #         self.tablero.tablero[0].append(ficha_roja)
        
    #     for _ in range(3):
    #         ficha_negra = Ficha(TipoFicha.NEGRA)
    #         self.tablero.tablero[1].append(ficha_negra)
        
    #     for _ in range(2):
    #         ficha_roja = Ficha(TipoFicha.ROJA)
    #         self.tablero.tablero[12].append(ficha_roja)
        
    #     for _ in range(4):
    #         ficha_negra = Ficha(TipoFicha.NEGRA)
    #         self.tablero.tablero[23].append(ficha_negra)
    
    def dibujar_ficha(self, x, y, tipo_ficha, radius=20):
        """Dibuja una ficha individual en la posición especificada"""
        color = FICHA_ROJA if tipo_ficha == TipoFicha.ROJA.value else FICHA_NEGRA
        
        pygame.draw.circle(self.screen, color, (int(x), int(y)), radius)
        pygame.draw.circle(self.screen, FICHA_BORDER, (int(x), int(y)), radius, 2)
    
    def dibujar_fichas_en_punto(self, punto_index):
        """Dibuja todas las fichas en un punto específico del tablero"""
        fichas = self.tablero.tablero[punto_index]
        if not fichas:
            return
        # Obtener la posición base del triángulo
        base_x, base_y = self.tablero_ui.get_punto_position_base(punto_index)
        punto_width = self.tablero_ui.punto_width
        punto_height = self.tablero_ui.punto_height
        
        # Calcular la posición central del triángulo para las fichas
        center_x = base_x + punto_width // 2
        
        # Determinar la dirección de apilamiento según la posición del triángulo
        if punto_index <= 11:  # Parte superior - fichas se apilan hacia abajo
            start_y = base_y + 30  # Comenzar un poco abajo del vértice
            y_offset = 35  # Espacio entre fichas
        else:  # Parte inferior - fichas se apilan hacia arriba
            start_y = base_y + punto_height - 30  # Comenzar un poco arriba del vértice
            y_offset = -35  # Espacio negativo para apilar hacia arriba
        
        # Dibujar cada ficha
        for i, ficha in enumerate(fichas):
            ficha_y = start_y + (i * y_offset)
            self.dibujar_ficha(center_x, ficha_y, ficha.tipo)
    
    def dibujar_todas_las_fichas(self):
        """Dibuja todas las fichas en todos los puntos del tablero"""
        for punto_index in range(24):
            self.dibujar_fichas_en_punto(punto_index)
    
    def actualizar_tablero(self, nuevo_tablero=None):
        """Actualiza el objeto tablero y redibuja"""
        if nuevo_tablero:
            self.tablero = nuevo_tablero
    
    def dibujar_frame(self):
        """Dibuja un frame completo del tablero con fichas"""
        # Limpiar pantalla
        self.screen.fill((222, 184, 135))  # BROWN_LIGHT
        
        # Dibujar el tablero
        self.tablero_ui.dibujar_tablero()
        
        # Dibujar las fichas
        self.dibujar_todas_las_fichas()
        
        # Actualizar pantalla
        pygame.display.flip()
    
    def run(self):
        """Loop principal del juego"""
        clock = pygame.time.Clock()
        
        while self.running:
            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            
            # Dibujar frame completo
            self.dibujar_frame()
            clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    # Crear y ejecutar la aplicación
    app = BackgammonUI()
    app.run()
