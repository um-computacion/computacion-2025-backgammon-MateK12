import unittest
from unittest.mock import Mock
from src.core.models.backgammon.Estrategias.EstrategiaMovimientoNormal import EstrategiaMovimientoNormal
from src.core.enums.TipoFicha import TipoFicha
from src.core.models.ficha.Ficha import Ficha
from src.core.models.tablero.Tablero import Tablero
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador

# pylint: disable=C0116,W0212,C0303


class TestEstrategiaMovimientoNormal(unittest.TestCase):
    def setUp(self):
        self.estrategia = EstrategiaMovimientoNormal()
        self.tablero = Tablero(
            Tablero_inicializador.inicializar_tablero(),
            Tablero_Validador()
        )
        self.backgammon_mock = Mock()

    def test_puede_mover_todas_posiciones_bloqueadas(self):
        """Todas las posiciones están bloqueadas"""
        for i in range(24):
            self.tablero.tablero[i] = []

        self.tablero.tablero[10] = [Ficha(TipoFicha.NEGRA.value)]
        self.tablero.tablero[15] = [Ficha(TipoFicha.NEGRA.value)]

        self.tablero.tablero[13] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        self.tablero.tablero[19] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        self.tablero.tablero[18] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        self.tablero.tablero[14] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        
        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [3, 4], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_puede_mover_roja_desde_5_para_ganar(self):
        """Ficha roja puede ganar desde posición 5"""
        for i in range(24):
            self.tablero.tablero[i] = []
        self.tablero.tablero[4] = [Ficha(TipoFicha.ROJA.value) for _ in range(14)]
        self.tablero.tablero[5] = [Ficha(TipoFicha.ROJA.value)]
        
        resultado = self.estrategia.puede_mover(
            TipoFicha.ROJA.value, [6], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)

    def test_puede_mover_se_pasa_sin_poder_ganar(self):
        """Ficha se pasa pero no puede ganar, hay otra opción"""
        for i in range(24):
            self.tablero.tablero[i] = []

        self.tablero.tablero[2] = [Ficha(TipoFicha.ROJA.value)]
        self.tablero.tablero[15] = [Ficha(TipoFicha.ROJA.value)]

        resultado = self.estrategia.puede_mover(
            TipoFicha.ROJA.value, [6], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)

    def test_puede_mover_completamente_bloqueado_negro(self):
        """Ficha negra no bloqueada completamente"""
        for i in range(24):
            self.tablero.tablero[i] = []

        self.tablero.tablero[22] = [Ficha(TipoFicha.NEGRA.value)]
        self.tablero.tablero[10] = [Ficha(TipoFicha.NEGRA.value)]

        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [3], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)

    def test_no_puede_mover_solo_una_ficha_completamente_bloqueada(self):
        """Una sola ficha completamente bloqueada"""
        for i in range(24):
            self.tablero.tablero[i] = []

        self.tablero.tablero[5] = [Ficha(TipoFicha.NEGRA.value)]
        self.tablero.tablero[7] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]

        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [2], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_no_puede_mover_pared_completa_bloqueo(self):
        """Pared completa bloquea todos los movimientos"""
        for i in range(24):
            self.tablero.tablero[i] = []

        self.tablero.tablero[20] = [Ficha(TipoFicha.NEGRA.value)]
        self.tablero.tablero[21] = [Ficha(TipoFicha.NEGRA.value)]

        self.tablero.tablero[22] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        self.tablero.tablero[23] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]

        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [2], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_puede_mover_todas_se_pasan_no_zona_ganancia(self):
        """Fichas se pasan pero hay opciones válidas"""
        for i in range(24):
            self.tablero.tablero[i] = []

        self.tablero.tablero[0] = [Ficha(TipoFicha.ROJA.value)]
        self.tablero.tablero[1] = [Ficha(TipoFicha.ROJA.value)]
        self.tablero.tablero[10] = [Ficha(TipoFicha.ROJA.value)]

        resultado = self.estrategia.puede_mover(
            TipoFicha.ROJA.value, [6], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)

    def test_puede_mover_ninguna_atras_roja(self):
        """Ficha roja con ninguna atrás puede ganar"""
        for i in range(24):
            self.tablero.tablero[i] = []

        self.tablero.fichas_ganadas = [Ficha(TipoFicha.ROJA.value) for _ in range(14)]
        self.tablero.tablero[3] = [Ficha(TipoFicha.ROJA.value)]

        resultado = self.estrategia.puede_mover(
            TipoFicha.ROJA.value, [6, 5], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)

    def test_puede_mover_ninguna_atras_negra(self):
        """Ficha negra con ninguna atrás puede ganar"""
        for i in range(24):
            self.tablero.tablero[i] = []

        self.tablero.fichas_ganadas = [Ficha(TipoFicha.NEGRA.value) for _ in range(14)]
        self.tablero.tablero[22] = [Ficha(TipoFicha.NEGRA.value)]

        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [6, 5], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)

    def test_no_puede_mover_ficha_se_pasa_por_tener_atras_bloqueado(self):
        """Ficha no puede pasar porque hay fichas atrás bloqueadas"""
        for i in range(24):
            self.tablero.tablero[i] = []

        self.tablero.tablero[19] = [Ficha(TipoFicha.NEGRA.value)]
        self.tablero.tablero[21] = [Ficha(TipoFicha.ROJA.value), Ficha(TipoFicha.ROJA.value)]
        self.tablero.tablero[22] = [Ficha(TipoFicha.ROJA.value), Ficha(TipoFicha.ROJA.value)]
        self.tablero.fichas_ganadas = [Ficha(TipoFicha.NEGRA.value) for _ in range(13)]
        self.tablero.tablero[23] = [Ficha(TipoFicha.NEGRA.value)]

        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [2, 3], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)



if __name__ == '__main__':
    unittest.main()