import unittest
import pygame
from src.core.models.backgammon.backgammon import Backgammon
from src.pygame_ui.Tablero_UI import (
    TableroUI,
    BOARD_WIDTH,
    BOARD_HEIGHT,
    BOARD_X,
    BOARD_Y,
)

# pylint: disable=C0116
class TestTableroUI(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.backgammon = Backgammon()
        self.tablero = TableroUI(self.backgammon.inicializar_tablero())
        self.punto_width = (BOARD_WIDTH - 100) // 12

    def test_get_punto_position_superior_derecha(self):
        punto_index = 0
        expected_x = BOARD_X + BOARD_WIDTH - (punto_index + 1) * self.punto_width
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
        expected_x = (
            BOARD_X + (punto_index - 12 + 1) * self.punto_width + BOARD_WIDTH / 2
        )
        expected_y = BOARD_Y + BOARD_HEIGHT - 250
        x, y = self.tablero.get_punto_position_base(punto_index)
        self.assertEqual((x, y), (expected_x, expected_y))

    def test_get_punto_position_inferior_izquierda(self):
        punto_index = 18
        expected_x = BOARD_X + (punto_index - 18) * self.punto_width
        expected_y = BOARD_Y + BOARD_HEIGHT - 250
        x, y = self.tablero.get_punto_position_base(punto_index)
        self.assertEqual((x, y), (expected_x, expected_y))

    def tearDown(self):
        pygame.quit()


if __name__ == "__main__":
    unittest.main()
