### modelo
Claude
### propmt 
teniendo en cuenta el enum de tipo ficha, haz un test para verificar el metodo repr
### respuesta    
import unittest
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha

class TestFicha(unittest.TestCase):
    
    def test_repr_ficha_negra(self):
        ficha = Ficha(TipoFicha.NEGRA.value)
        self.assertEqual(repr(ficha), '\033[30m●\033[0m')
        
    def test_repr_ficha_roja(self):
        ficha = Ficha(TipoFicha.ROJA.value)
        self.assertEqual(repr(ficha), '\033[31m●\033[0m')
        
    def test_repr_ficha_invalida(self):
        ficha = Ficha(3)  # Valor inválido
        self.assertEqual(repr(ficha), '●')

if __name__ == '__main__':
    unittest.main()
### cambios
le quite el ultimo tests, ya que el tipado no permite el valor 3 para tipo, solo 1 y 2
### archivos finales
Test_Ficha.py

### modelo
Claude
### propmt 
crea los unit test de esta clase, pon enfasis en el metodo get_punto_position_base ya que defnira como se vera mis trianguos del tablero 
### respuesta    
import unittest
import pygame
from src.pygame_ui.ui import TableroUI, BOARD_WIDTH, BOARD_HEIGHT, BOARD_X, BOARD_Y

class TestTableroUI(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.tablero = TableroUI()
        self.punto_width = (BOARD_WIDTH - 100) // 12
        
    def test_get_punto_position_superior_derecha(self):
        expected_x = BOARD_X + BOARD_WIDTH - self.punto_width
        expected_y = BOARD_Y
        x, y = self.tablero.get_punto_position_base(0)
        self.assertEqual((x, y), (expected_x, expected_y))
        
    def test_get_punto_position_superior_izquierda(self):
        expected_x = BOARD_X + BOARD_WIDTH - (6 * self.punto_width) - 150
        expected_y = BOARD_Y
        x, y = self.tablero.get_punto_position_base(6)
        self.assertEqual((x, y), (expected_x, expected_y))
        
    def test_get_punto_position_inferior_derecha(self):
        punto_index = 12
        expected_x = BOARD_X + (punto_index - 12 + 1) * self.punto_width + BOARD_WIDTH/2
        expected_y = BOARD_Y + BOARD_HEIGHT - 250
        x, y = self.tablero.get_punto_position_base(punto_index)
        self.assertEqual((x, y), (expected_x, expected_y))
        
    def test_get_punto_position_inferior_izquierda(self):
        punto_index = 18
        expected_x = BOARD_X + (punto_index - 18) * self.punto_width
        expected_y = BOARD_Y + BOARD_HEIGHT - 250
        x, y = self.tablero.get_punto_position_base(punto_index)
        self.assertEqual((x, y), (expected_x, expected_y))
        
    def test_todos_puntos_en_rango(self):
        for i in range(24):
            x, y = self.tablero.get_punto_position_base(i)
            self.assertTrue(BOARD_X <= x <= BOARD_X + BOARD_WIDTH)
            self.assertTrue(BOARD_Y <= y <= BOARD_Y + BOARD_HEIGHT)
            
    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
### Fixed
### cambios
quite el ultimo test, ya que no lo considero importante, ya que si esta generando correctamente 
la posicion de los triangulos en los otros cuadrantes, los esta generando dentro del tablero 
en el primer test agrege la variable punto_index para permitir calcular cualquier triangulo del primer cuadrante
### archivos finales
Test_ui


