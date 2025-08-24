import unittest
from src.core.models.tablero.Tablero import Tablero
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.CasillaOcupadaException import CasillaOcupadaException

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero_vacio = [[] for _ in range(24)]
        self.tablero = Tablero(self.tablero_vacio)

    def test_mover_ficha_a_espacio_vacio(self):
        ficha = Ficha(TipoFicha.NEGRA.value)
        self.tablero.__tablero__[0].append(ficha)
        
        self.tablero.mover_ficha(ficha, 0, 1)
        
        self.assertEqual(len(self.tablero.__tablero__[0]), 0)
        self.assertEqual(len(self.tablero.__tablero__[1]), 1)
        self.assertEqual(self.tablero.__tablero__[1][0], ficha)

    def test_mover_ficha_a_espacio_con_ficha_mismo_color(self):
        ficha1 = Ficha(TipoFicha.NEGRA.value)
        ficha2 = Ficha(TipoFicha.NEGRA.value)
        self.tablero.__tablero__[0].append(ficha1)
        self.tablero.__tablero__[1].append(ficha2)
        
        self.tablero.mover_ficha(ficha1, 0, 1)
        
        self.assertEqual(len(self.tablero.__tablero__[0]), 0)
        self.assertEqual(len(self.tablero.__tablero__[1]), 2)

    def test_mover_ficha_a_espacio_con_fichas_rivales(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja1 = Ficha(TipoFicha.ROJA.value)
        ficha_roja2 = Ficha(TipoFicha.ROJA.value)
        
        self.tablero.__tablero__[0].append(ficha_negra)
        self.tablero.__tablero__[1].append(ficha_roja1)
        self.tablero.__tablero__[1].append(ficha_roja2)
        
        with self.assertRaises(CasillaOcupadaException):
            self.tablero.mover_ficha(ficha_negra, 0, 1)

if __name__ == '__main__':
    unittest.main()