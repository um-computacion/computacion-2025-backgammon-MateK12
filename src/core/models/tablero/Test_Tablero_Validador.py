import unittest
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.MovimientoNoJustoParaGanar import MovimientoNoJustoParaGanar


class TestTableroValidador(unittest.TestCase):
    def setUp(self):
        self.validador = Tablero_Validador()
        self.tablero = [[] for _ in range(24)]

    def test_triangulo_con_dos_fichas_rivales(self):  # triangulo_con_fichas_rivales()
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja1 = Ficha(TipoFicha.ROJA.value)
        ficha_roja2 = Ficha(TipoFicha.ROJA.value)

        self.tablero[0] = [ficha_roja1, ficha_roja2]  # poner 2 fichas en triangulo

        self.assertTrue(
            self.validador.triangulo_con_fichas_rivales(self.tablero, 0, ficha_negra)
        )  # movimiento invalido

    def test_triangulo_mas_dos_fichas_rivales(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja1 = Ficha(TipoFicha.ROJA.value)
        ficha_roja2 = Ficha(TipoFicha.ROJA.value)
        ficha_roja3 = Ficha(TipoFicha.ROJA.value)
        self.tablero[0] = [
            ficha_roja1,
            ficha_roja2,
            ficha_roja3,
        ]  # poner 3 fichas en triangulo

        self.assertTrue(
            self.validador.triangulo_con_fichas_rivales(self.tablero, 0, ficha_negra)
        )  # movimiento invalido

    def test_triangulo_con_una_ficha_rival(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja = Ficha(TipoFicha.ROJA.value)

        self.tablero[0] = [ficha_roja]

        self.assertFalse(
            self.validador.triangulo_con_fichas_rivales(self.tablero, 0, ficha_negra)
        )  # movimiento valido come ficha

    def test_triangulo_vacio(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)

        self.assertFalse(
            self.validador.triangulo_con_fichas_rivales(self.tablero, 0, ficha_negra)
        )

    def test_triangulo_con_fichas_mismo_color(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_negra1 = Ficha(TipoFicha.NEGRA.value)
        ficha_negra2 = Ficha(TipoFicha.NEGRA.value)

        self.tablero[0] = [ficha_negra1, ficha_negra2]

        self.assertFalse(
            self.validador.triangulo_con_fichas_rivales(self.tablero, 0, ficha_negra)
        )

    def test_puede_comer_con_una_ficha_rival(self):  # puede_comer()
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.tablero[3] = [ficha_roja]
        self.assertTrue(self.validador.puede_comer(self.tablero, 3, ficha_negra))

    def test_no_puede_comer_2_fichas(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja1 = Ficha(TipoFicha.ROJA.value)
        ficha_roja2 = Ficha(TipoFicha.ROJA.value)

        self.tablero[3] = [ficha_roja1, ficha_roja2]
        self.assertFalse(self.validador.puede_comer(self.tablero, 3, ficha_negra))

    def test_no_puede_comer_si_no_hay_fichas(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertFalse(self.validador.puede_comer(self.tablero, 3, ficha_negra))

    def test_no_puede_comer_mismo_tipo(self):
        ficha_roja1 = Ficha(TipoFicha.ROJA.value)
        ficha_roja3 = Ficha(TipoFicha.ROJA.value)
        self.tablero[3] = [ficha_roja1]
        self.assertFalse(self.validador.puede_comer(self.tablero, 3, ficha_roja3))

    def test_tiene_fichas_comidas_tablero_vacio(self):  # tiene_fichas_comidas()
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertTrue(self.validador.tiene_fichas_comidas(self.tablero, ficha_negra))

    def test_no_tiene_fichas_comidas_con_fichas_en_tablero(self):
        """Prueba cuando hay fichas del mismo color en el tablero"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_negra2 = Ficha(TipoFicha.NEGRA.value)
        self.tablero[0] = [ficha_negra2]

        self.assertFalse(self.validador.tiene_fichas_comidas(self.tablero, ficha_negra))

    def test_tiene_fichas_comidas_solo_fichas_rivales(self):
        """Prueba cuando solo hay fichas rivales en el tablero"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.tablero[0] = [ficha_roja]

        self.assertTrue(self.validador.tiene_fichas_comidas(self.tablero, ficha_negra))

    def test_no_tiene_fichas_comidas_multiples_posiciones(self):
        """Prueba con fichas en múltiples posiciones del tablero"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_negra2 = Ficha(TipoFicha.NEGRA.value)
        ficha_roja = Ficha(TipoFicha.ROJA.value)

        self.tablero[0] = [ficha_roja]
        self.tablero[5] = [ficha_negra2]
        self.tablero[10] = [ficha_roja]

        self.assertFalse(self.validador.tiene_fichas_comidas(self.tablero, ficha_negra))

    def test_puede_ganar_ficha_negra(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertTrue(self.validador.puede_ganar(ficha_negra, 24, 23, 1))

    def test_no_puede_ganar_ficha_roja(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_roja, 5, 6, 1))

    def test_no_puede_ganar_ficha_negra(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_negra, 20, 19, 1))

    def test_raise_movimiento_no_justo_para_ganar_roja(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        with self.assertRaises(MovimientoNoJustoParaGanar):
            self.validador.puede_ganar(ficha_roja, -2, 4, -6)

    def test_raise_movimiento_no_justo_para_ganar_negra(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        with self.assertRaises(MovimientoNoJustoParaGanar):
            self.validador.puede_ganar(ficha_negra, 25, 23, 2)

    def test_puede_ganar_ficha_roja(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertTrue(self.validador.puede_ganar(ficha_roja, -1, 0, -1))

    def test_no_puede_ganar_ficha_roja(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_roja, 0, 6, -6))

    def test_no_puede_ganar_volviendo_de_comida(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_roja, -1, 24, -1))


if __name__ == "__main__":
    unittest.main()
