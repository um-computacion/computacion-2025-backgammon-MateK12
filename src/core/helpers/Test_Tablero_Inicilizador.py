import unittest
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador
from src.core.enums.TipoFicha import TipoFicha

# pylint: disable=C0116
class TestFicha(unittest.TestCase):
    def test_inicializar_tablero(self):
        tablero = Tablero_inicializador.inicializar_tablero()

        self.assertEqual(len(tablero), 24)

        self.assertEqual(len(tablero[0]), 2)
        self.assertEqual(len(tablero[11]), 5)
        self.assertEqual(len(tablero[16]), 3)
        self.assertEqual(len(tablero[18]), 5)

        self.assertEqual(tablero[0][0].tipo, TipoFicha.NEGRA.value)
        self.assertEqual(tablero[11][0].tipo, TipoFicha.NEGRA.value)
        self.assertEqual(tablero[16][0].tipo, TipoFicha.NEGRA.value)
        self.assertEqual(tablero[18][0].tipo, TipoFicha.NEGRA.value)

        self.assertEqual(len(tablero[23]), 2)
        self.assertEqual(len(tablero[12]), 5)
        self.assertEqual(len(tablero[7]), 3)
        self.assertEqual(len(tablero[5]), 5)

        self.assertEqual(tablero[23][0].tipo, TipoFicha.ROJA.value)
        self.assertEqual(tablero[12][0].tipo, TipoFicha.ROJA.value)
        self.assertEqual(tablero[7][0].tipo, TipoFicha.ROJA.value)
        self.assertEqual(tablero[5][0].tipo, TipoFicha.ROJA.value)

        posiciones_vacias = [1, 2, 3, 4, 6, 8, 9, 10, 13, 14, 15, 17, 19, 20, 21, 22]
        for pos in posiciones_vacias:
            self.assertEqual(len(tablero[pos]), 0)
