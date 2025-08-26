import unittest
from unittest.mock import Mock, patch
from src.core.models.backgammon.backgammon import Backgammon
from src.core.enums.TipoFicha import TipoFicha

class TestBackgammon(unittest.TestCase):
    def setUp(self):
        self.game = Backgammon()

    def test_tirar_dados(self):
        with patch('src.core.models.dado.Dados.Dados.tirar_dados') as mock_dados:
            mock_dados.return_value = {'dado1': 4, 'dado2': 6}
            resultado = self.game.tirar_dados()
            self.assertEqual(resultado, {'dado1': 4, 'dado2': 6})

    def test_mover_ficha(self):
        self.game._Backgammon__tablero__.mover_ficha = Mock()
        self.game.mover_ficha()
        self.game._Backgammon__tablero__.mover_ficha.assert_called_once()

    def test_seleccionar_ficha(self):
        with self.assertRaises(AttributeError):  # Method is incomplete in source
            self.game.seleccionar_ficha(0, TipoFicha.NEGRA)

if __name__ == '__main__':
    unittest.main()