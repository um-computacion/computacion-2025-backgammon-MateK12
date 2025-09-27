import unittest
from src.core.models.tablero.Tablero import Tablero
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.CasillaOcupadaException import CasillaOcupadaException
from src.core.exceptions.MovimientoNoJustoParaGanar import MovimientoNoJustoParaGanar
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from unittest.mock import patch


# pylint: disable=C0116
class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero_vacio = [[] for _ in range(24)]
        self.tablero = Tablero(self.tablero_vacio)

    def test_mover_ficha_a_espacio_vacio(self):  # mover_ficha()
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

    def test_mover_ficha_a_espacio_con_una_ficha_rival(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja = Ficha(TipoFicha.ROJA.value)

        self.tablero.__tablero__[0].append(ficha_negra)
        self.tablero.__tablero__[1].append(ficha_roja)

        self.tablero.mover_ficha(ficha_negra, 0, 1)

        self.assertEqual(len(self.tablero.__tablero__[0]), 0)
        self.assertEqual(len(self.tablero.__tablero__[1]), 1)
        self.assertEqual(self.tablero.__tablero__[1][0], ficha_negra)
        self.assertEqual(len(self.tablero.fichas_comidas), 1)  # ficha roja
        self.assertEqual(self.tablero.fichas_comidas[0], ficha_roja)
        self.assertTrue(self.tablero.fichas_comidas[0].comida)

    def test_mover_ficha_fuera_del_tablero(self):
        ficha = Ficha(TipoFicha.NEGRA.value)
        self.tablero.__tablero__[0].append(ficha)

        with self.assertRaises(MovimientoNoJustoParaGanar):
            self.tablero.mover_ficha(ficha, 22, 5)

    def test_mover_ficha_a_ganar_negra(self):
        ficha = Ficha(TipoFicha.NEGRA.value)
        self.tablero.__tablero__[22].append(ficha)
        self.tablero.mover_ficha(ficha, 22, 2)
        self.assertEqual(len(self.tablero.__tablero__[22]), 0)
        self.assertEqual(len(self.tablero.fichas_ganadas), 1)

    def test_mover_ficha_a_ganar_roja(self):
        ficha = Ficha(TipoFicha.ROJA.value)
        self.tablero.__tablero__[2].append(ficha)
        self.tablero.mover_ficha(ficha, 2, -3)
        self.assertEqual(len(self.tablero.__tablero__[2]), 0)
        self.assertEqual(len(self.tablero.fichas_ganadas), 1)

    def test_mover_ficha_se_queda_corta__roja(self):
        ficha = Ficha(TipoFicha.ROJA.value)
        self.tablero.__tablero__[3].append(ficha)
        self.tablero.mover_ficha(ficha, 3, -3)
        self.assertEqual(len(self.tablero.fichas_ganadas), 0)
        self.assertEqual(len(self.tablero.__tablero__[3]), 0)

    def test_validador_getter(self):
        self.assertIsInstance(self.tablero.validador, Tablero_Validador)

    def test_get_tablero(self):
        self.assertEqual(self.tablero.tablero, self.tablero.__tablero__)


if __name__ == "__main__":
    unittest.main()
