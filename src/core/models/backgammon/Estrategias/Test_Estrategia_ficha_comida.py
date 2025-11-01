import unittest
from unittest.mock import Mock
from src.core.models.backgammon.Estrategias.EstrategiaMovimientoComida import EstrategiaMovimientoComida
from src.core.enums.TipoFicha import TipoFicha
from src.core.models.ficha.Ficha import Ficha
from src.core.models.tablero.Tablero import Tablero
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador

# pylint: disable=C0116,W0212,C0303


class TestEstrategiaMovimientoComida(unittest.TestCase):
    def setUp(self):
        self.estrategia = EstrategiaMovimientoComida()
        self.tablero = Tablero(
            Tablero_inicializador.inicializar_tablero(),
            Tablero_Validador()
        )
        self.backgammon_mock = Mock()

    def test_puede_mover_sin_fichas_comidas(self):
        """No hay fichas comidas, retorna False"""
        self.tablero.fichas_comidas = []
        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [1, 2], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_puede_mover_con_fichas_comidas_del_otro_color(self):
        """Hay fichas comidas pero del otro color, retorna False"""
        self.tablero.fichas_comidas = [Ficha(TipoFicha.ROJA.value)]
        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [1, 2], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_puede_mover_ficha_comida_negra_bloqueada(self):
        """Ficha comida negra pero bloqueada por rivales"""
        self.tablero.fichas_comidas = [Ficha(TipoFicha.NEGRA.value)]
        for i in range(6):
            self.tablero.tablero[i] = [
                Ficha(TipoFicha.ROJA.value),
                Ficha(TipoFicha.ROJA.value),
            ]
        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [2], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_puede_mover_ficha_comida_roja_bloqueada(self):
        """Ficha comida roja pero bloqueada por rivales"""
        self.tablero.fichas_comidas = [Ficha(TipoFicha.ROJA.value)]
        for i in range(18, 24):
            self.tablero.tablero[i] = [
                Ficha(TipoFicha.NEGRA.value),
                Ficha(TipoFicha.NEGRA.value),
            ]
        resultado = self.estrategia.puede_mover(
            TipoFicha.ROJA.value, [2], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_puede_mover_ficha_comida_negra_valida(self):
        """Ficha comida negra puede entrar en triangulo 1"""
        self.tablero.fichas_comidas = [Ficha(TipoFicha.NEGRA.value)]
        self.tablero.tablero[0] = []
        self.tablero.tablero[1] = []
        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [2, 1], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)

    def test_puede_mover_ficha_comida_roja_valida(self):
        """Ficha comida roja puede entrar en triangulo 22"""
        self.tablero.fichas_comidas = [Ficha(TipoFicha.ROJA.value)]
        self.tablero.tablero[22] = []
        self.tablero.tablero[23] = []
        resultado = self.estrategia.puede_mover(
            TipoFicha.ROJA.value, [2, 1], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)

    def test_puede_mover_ficha_comida_negra_con_multiples_dados(self):
        """Ficha comida negra encuentra el primer dado válido"""
        self.tablero.fichas_comidas = [Ficha(TipoFicha.NEGRA.value)]
        self.tablero.tablero[0] = [Ficha(TipoFicha.ROJA.value), Ficha(TipoFicha.ROJA.value)]
        self.tablero.tablero[1] = []
        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [2, 1], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)



if __name__ == '__main__':
    unittest.main()