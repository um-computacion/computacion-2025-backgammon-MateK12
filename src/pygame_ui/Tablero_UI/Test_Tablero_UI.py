import unittest
import pygame
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador
from src.pygame_ui.Tablero_UI.Tablero_UI import TableroUI, BOARD_WIDTH,BOARD_HEIGHT,BOARD_X,BOARD_Y,BLACK
from src.core.models.tablero.Tablero import Tablero
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from unittest.mock import patch

# pylint: disable=C0116
class TestTableroUI(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.tablero_inicial = Tablero(Tablero_inicializador.inicializar_tablero(),Tablero_Validador())
        self.tablero_UI = TableroUI(self.tablero_inicial)
        self.punto_width = (BOARD_WIDTH - 100) // 12

    def test_get_tablero_inicializado(self):
        self.assertIsNotNone(self.tablero_UI.tablero)
        self.assertEqual(self.tablero_UI.tablero, self.tablero_inicial)
    def test_set_tablero(self):
        nuevo_tablero = Tablero_inicializador.inicializar_tablero()
        nuevo_tablero[-1] = []
        self.tablero_UI.tablero = nuevo_tablero
        self.assertEqual(self.tablero_UI.tablero, nuevo_tablero)
    def test_get_punto_position_superior_derecha(self):
        punto_index = 0
        expected_x = BOARD_X + BOARD_WIDTH - (punto_index + 1) * self.punto_width
        expected_y = BOARD_Y
        x, y = self.tablero_UI.get_punto_position_base(0)
        self.assertEqual((x, y), (expected_x, expected_y))

    def test_get_punto_position_superior_izquierda(self):
        expected_x = BOARD_X + BOARD_WIDTH - (6 * self.punto_width) - 150
        expected_y = BOARD_Y
        x, y = self.tablero_UI.get_punto_position_base(6)
        self.assertEqual((x, y), (expected_x, expected_y))

    def test_get_punto_position_inferior_derecha(self):
        punto_index = 12
        expected_x = (
            BOARD_X + (punto_index - 12 + 1) * self.punto_width + BOARD_WIDTH / 2
        )
        expected_y = BOARD_Y + BOARD_HEIGHT - 250
        x, y = self.tablero_UI.get_punto_position_base(punto_index)
        self.assertEqual((x, y), (expected_x, expected_y))

    def test_get_punto_position_inferior_izquierda(self):
        punto_index = 18
        expected_x = BOARD_X + (punto_index - 18) * self.punto_width
        expected_y = BOARD_Y + BOARD_HEIGHT - 250
        x, y = self.tablero_UI.get_punto_position_base(punto_index)
        self.assertEqual((x, y), (expected_x, expected_y))

    @patch('pygame.draw.polygon')
    def test_dibujar_triangulo(self, mock_draw_polygon):
        screen = pygame.Surface((BOARD_WIDTH + 200, BOARD_HEIGHT + 100))
        punto_index = 0
        color = (255, 0, 0)
        self.tablero_UI.dibujar_triangulo(punto_index, color, screen)
        self.assertEqual(mock_draw_polygon.call_count, 2)

        llamadas = mock_draw_polygon.call_args_list

        primera_llamada = llamadas[0][0]
        self.assertEqual(primera_llamada[0], screen)
        self.assertEqual(primera_llamada[1], color) 

        segunda_llamada = llamadas[1][0]
        self.assertEqual(segunda_llamada[0], screen)
        self.assertEqual(segunda_llamada[1], BLACK)


    @patch('src.pygame_ui.Tablero_UI.Tablero_UI.TableroUI._TableroUI__dibujar_numero_triangulo')
    @patch('src.pygame_ui.Tablero_UI.Tablero_UI.TableroUI.dibujar_triangulo')
    @patch('pygame.draw.rect')
    def test_dibujar_tablero(self, mock_draw_rect, mock_dibujar_triangulo, mock_dibujar_numero_triangulo):
        screen = pygame.Surface((BOARD_WIDTH + 200, BOARD_HEIGHT + 100))
        self.tablero_UI.dibujar_tablero(screen)
        self.assertEqual(mock_draw_rect.call_count, 2)
        self.assertEqual(mock_dibujar_triangulo.call_count, 24)
        self.assertEqual(mock_dibujar_numero_triangulo.call_count, 24)

    @patch('src.pygame_ui.Tablero_UI.Tablero_UI.TableroUI.dibujar_ficha')
    @patch('src.pygame_ui.Tablero_UI.Tablero_UI.TableroUI.get_punto_position_base_ficha')
    def test_dibujar_fichas_en_punto(self, mock_get_punto_position_base_ficha, mock_dibujar_ficha):
        screen = pygame.Surface((BOARD_WIDTH + 200, BOARD_HEIGHT + 100))
        punto_index = 0
        mock_get_punto_position_base_ficha.return_value = (100, 100)
        self.tablero_UI.dibujar_fichas_en_punto(punto_index, screen)
        self.assertEqual(mock_get_punto_position_base_ficha.call_count, 1)
        self.assertEqual(mock_dibujar_ficha.call_count, 2)

    @patch('src.pygame_ui.Tablero_UI.Tablero_UI.TableroUI.dibujar_ficha')
    @patch('src.pygame_ui.Tablero_UI.Tablero_UI.TableroUI.get_punto_position_base_ficha')
    def test_dibujar_fichas_en_punto_vacio(self,mock_get_punto_position_base_ficha, mock_dibujar_ficha):
        screen = pygame.Surface((BOARD_WIDTH + 200, BOARD_HEIGHT + 100))
        punto_index = 1
        self.tablero_UI.dibujar_fichas_en_punto(punto_index, screen)
        self.assertEqual(mock_get_punto_position_base_ficha.call_count, 0)
        self.assertEqual(mock_dibujar_ficha.call_count, 0)

    def test_get_punto_position_base_ficha_coordenadas_correctas(self):
        """Test que verifica que las coordenadas devueltas correspondan al punto_index"""

        x_base = BOARD_X  
        y_superior = BOARD_Y  
        y_inferior = BOARD_Y + BOARD_HEIGHT -250
        punto_width = 58

        for i in range(6):
            x, y = self.tablero_UI.get_punto_position_base_ficha(i)
            expected_x = x_base + BOARD_WIDTH - (i + 1) * punto_width
            expected_y = y_superior

            self.assertEqual(x, expected_x)
            self.assertEqual(y, expected_y)

        # Test triángulos superiores 6-11 (lado izquierdo)
        for i in range(6, 12):
            x, y = self.tablero_UI.get_punto_position_base_ficha(i)
            expected_x = x_base + BOARD_WIDTH - i * punto_width - 150
            expected_y = y_superior

            self.assertEqual(x, expected_x)
            self.assertEqual(y, expected_y)

        # Test triángulos inferiores 12-17 (lado izquierdo)
        for i in range(12, 18):
            x, y = self.tablero_UI.get_punto_position_base_ficha(i)
            expected_x = x_base + (i - 12) * punto_width
            expected_y = y_inferior

            self.assertEqual(x, expected_x)
            self.assertEqual(y, expected_y)

        # Test triángulos inferiores 18-23 (lado derecho)
        for i in range(18, 24):
            x, y = self.tablero_UI.get_punto_position_base_ficha(i)
            expected_x = (x_base + (i - 18) * punto_width + 
                         6 * punto_width + 110)
            expected_y = y_inferior

            self.assertEqual(x, expected_x)
            self.assertEqual(y, expected_y)



    def tearDown(self):
        pygame.quit()


if __name__ == "__main__":
    unittest.main()
