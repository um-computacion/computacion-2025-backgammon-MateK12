import unittest
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.MovimientoNoJustoParaGanar import MovimientoNoJustoParaGanar

# pylint: disable=C0116


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

    def test_no_puede_ganar_se_queda_corto_roja(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_roja, 0, 3))

    def test_no_puede_ganar_se_queda_corto_roja_no_se_pasa(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.se_pasa_del_tablero(ficha_roja, 0, 3))

    def test_puede_ganar_ficha_negra(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertTrue(self.validador.puede_ganar(ficha_negra, 24, 23))

    def test_no_puede_ganar_ficha_roja(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_roja, 5, 6))

    def test_no_puede_ganar_ficha_negra(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_negra, 20, 19))

    def test_puede_ganar_ficha_roja(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertTrue(self.validador.puede_ganar(ficha_roja, -1, 0))

    def test_no_puede_ganar_ficha_roja(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_roja, 0, 6))

    def test_no_puede_ganar_volviendo_de_comida(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_roja, -1, 24))

    def test_no_se_pasa_del_tablero_ficha_negra(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertFalse(self.validador.se_pasa_del_tablero(ficha_negra, 24, 23))

    def test_no_se_pasa_del_tablero_ficha_roja(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.se_pasa_del_tablero(ficha_roja, -1, 0))

    def test_no_se_pasa_del_tablero_ficha_roja_si_sale_6(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.se_pasa_del_tablero(ficha_roja, -1, 0))

    def test_no_se_pasa_del_tablero_ficha_negra_si_sale_6(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertFalse(self.validador.se_pasa_del_tablero(ficha_negra, 24, 24))

    def test_se_pasa_del_tablero_ficha_negra_mueve_3(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertTrue(self.validador.se_pasa_del_tablero(ficha_negra, 26, 23))

    def test_se_pasa_del_tablero_ficha_roja_mueve_3(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertTrue(self.validador.se_pasa_del_tablero(ficha_roja, -2, 1))

    def test_no_se_pasa_si_es_menor_roja(self):
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.se_pasa_del_tablero(ficha_roja, 0, 3))

    def test_no_se_pasa_si_es_menor_negra(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertFalse(self.validador.se_pasa_del_tablero(ficha_negra, 23, 20))


if __name__ == "__main__":
    unittest.main()
