import unittest
from unittest.mock import Mock
from src.core.models.backgammon.Estrategias.EstrategiaUnicaFicha import EstrategiaUnicaFicha
from src.core.enums.TipoFicha import TipoFicha
from src.core.models.ficha.Ficha import Ficha
from src.core.models.tablero.Tablero import Tablero
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador

# pylint: disable=C0116,W0212,C0303


class TestEstrategiaUnicaFicha(unittest.TestCase):
    def setUp(self):
        self.estrategia = EstrategiaUnicaFicha()
        self.tablero = Tablero(
            Tablero_inicializador.inicializar_tablero(),
            Tablero_Validador()
        )
        self.backgammon_mock = Mock()
        self.backgammon_mock.mover_ficha = Mock()
        self.backgammon_mock.hay_fichas_comidas = Mock(return_value=False)
    def test_no_aplica_no_hay_dos_dados(self):
        """Estrategia no aplica si no hay exactamente 2 dados"""
        resultado = self.estrategia.puede_mover(
            TipoFicha.ROJA.value, [3], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_no_aplica_puede_mover_con_suma(self):
        """No aplica si puede mover con la suma de ambos dados"""
        for i in range(24):
            self.tablero.tablero[i] = []
        
        self.tablero.tablero[10] = [Ficha(TipoFicha.ROJA.value)]
        
        resultado = self.estrategia.puede_mover(
            TipoFicha.ROJA.value, [3, 2], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_no_aplica_puede_con_ambos_dados(self):
        """No aplica si puede mover con ambos dados individuales"""
        for i in range(24):
            self.tablero.tablero[i] = []
        
        self.tablero.tablero[10] = [Ficha(TipoFicha.ROJA.value)]
        self.tablero.tablero[20] = [Ficha(TipoFicha.ROJA.value)]
        
        resultado = self.estrategia.puede_mover(
            TipoFicha.ROJA.value, [3, 2], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_aplica_unica_opcion_es_dado_mayor(self):
        """Aplica: una ficha solo puede moverse con el dado mayor"""
        for i in range(24):
            self.tablero.tablero[i] = []
        
        self.tablero.tablero[10] = [Ficha(TipoFicha.ROJA.value)]
        self.tablero.tablero[5] = [Ficha(TipoFicha.NEGRA.value), Ficha(TipoFicha.NEGRA.value)]
        resultado = self.estrategia.puede_mover(
            TipoFicha.ROJA.value, [3, 2], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)
        self.backgammon_mock.mover_ficha.assert_called_with(10, 3)

    def test_no_aplica_unica_opcion_no_es_dado_mayor(self):
        """No aplica: una ficha puede moverse pero no con el dado mayor"""
        for i in range(24):
            self.tablero.tablero[i] = []
        
        self.tablero.tablero[10] = [Ficha(TipoFicha.ROJA.value)]
        self.tablero.tablero[7] = [Ficha(TipoFicha.NEGRA.value), Ficha(TipoFicha.NEGRA.value)]
        
        resultado = self.estrategia.puede_mover(
            TipoFicha.ROJA.value, [3, 2], self.tablero, self.backgammon_mock
        )
        self.assertFalse(resultado)

    def test_aplica_unica_ficha_negra_con_dado_mayor(self):
        """Aplica para ficha negra cuando solo puede moverse con dado mayor"""
        for i in range(24):
            self.tablero.tablero[i] = []
        self.tablero.tablero[15] = [Ficha(TipoFicha.NEGRA.value)]
        self.tablero.tablero[18] = [Ficha(TipoFicha.ROJA.value), Ficha(TipoFicha.ROJA.value)]
        
        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [1, 2], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)
        self.backgammon_mock.mover_ficha.assert_called_with(15, 2)

    def test_ejecutar_mueve_con_dado_mayor(self):
        """Ejecutar mueve con el dado mayor"""
        for i in range(24):
            self.tablero.tablero[i] = []
        
        self.tablero.tablero[10] = [Ficha(TipoFicha.ROJA.value)]
        
        self.estrategia.ejecutar(
            [3, 2], 10, self.backgammon_mock
        )
        
        self.backgammon_mock.mover_ficha.assert_called_once_with(10, 3)

    def test_puede_mover_suma_dobles_invalida(self):
        """Suma con dobles inválida aplica estrategia"""
        for i in range(24):
            self.tablero.tablero[i] = []
        
        self.tablero.tablero[10] = [Ficha(TipoFicha.NEGRA.value)]
        self.tablero.tablero[14] = [Ficha(TipoFicha.ROJA.value), Ficha(TipoFicha.ROJA.value)]
        resultado = self.estrategia.puede_mover(
            TipoFicha.NEGRA.value, [3, 1], self.tablero, self.backgammon_mock
        )
        self.assertTrue(resultado)
        self.backgammon_mock.mover_ficha.assert_called_once_with(10, 3)



if __name__ == '__main__':
    unittest.main()