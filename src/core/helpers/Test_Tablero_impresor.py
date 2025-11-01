import unittest
from unittest.mock import patch, MagicMock
from src.core.models.ficha.Ficha import Ficha
from src.core.models.tablero.Tablero import Tablero
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.enums.TipoFicha import TipoFicha
from src.core.helpers.Tablero_Impresor import Tablero_Impresor

# pylint: disable=C0116,C0303


class TestTableroImpresor(unittest.TestCase):
    def setUp(self):
        self.validador = MagicMock()
        tablero_vacio = [[] for _ in range(24)]
        self.tablero_vacio = Tablero(tablero_vacio, self.validador)
        

    @patch('builtins.print')
    def test_imprimir_tablero_con_fichas_negras(self, mock_print):
        """Test imprimir tablero con fichas negras"""
        tablero_con_fichas = [[] for _ in range(24)]
        tablero_con_fichas[0] = [Ficha(TipoFicha.NEGRA.value) for _ in range(3)]
        tablero_con_fichas[12] = [Ficha(TipoFicha.NEGRA.value) for _ in range(2)]
        
        tablero = Tablero(tablero_con_fichas, self.validador)
        Tablero_Impresor.imprimir_tablero(tablero)
        
        self.assertGreater(mock_print.call_count, 0)

    @patch('builtins.print')
    def test_imprimir_tablero_con_fichas_rojas(self, mock_print):
        """Test imprimir tablero con fichas rojas"""
        tablero_con_fichas = [[] for _ in range(24)]
        tablero_con_fichas[5] = [Ficha(TipoFicha.ROJA.value) for _ in range(4)]
        tablero_con_fichas[23] = [Ficha(TipoFicha.ROJA.value) for _ in range(1)]
        
        tablero = Tablero(tablero_con_fichas, self.validador)
        Tablero_Impresor.imprimir_tablero(tablero)
        
        self.assertGreater(mock_print.call_count, 0)

    @patch('builtins.print')
    def test_imprimir_tablero_con_fichas_comidas(self, mock_print):
        """Test imprimir tablero con fichas comidas"""
        tablero_vacio = [[] for _ in range(24)]
        tablero = Tablero(tablero_vacio, self.validador)
        tablero.fichas_comidas = [Ficha(TipoFicha.NEGRA.value), Ficha(TipoFicha.ROJA.value)]
        
        Tablero_Impresor.imprimir_tablero(tablero)
        
        calls = [str(call) for call in mock_print.call_args_list]
        calls_str = " ".join(calls)
        self.assertIn("Fichas comidas", calls_str)
        self.assertIn("●", calls_str)

    @patch('builtins.print')
    def test_imprimir_tablero_con_fichas_ganadas(self, mock_print):
        """Test imprimir tablero con fichas ganadas"""
        tablero_vacio = [[] for _ in range(24)]
        tablero = Tablero(tablero_vacio, self.validador)
        tablero.fichas_ganadas = [Ficha(TipoFicha.NEGRA.value) for _ in range(15)]
        
        Tablero_Impresor.imprimir_tablero(tablero)
        
        calls = [str(call) for call in mock_print.call_args_list]
        calls_str = " ".join(calls)
        self.assertIn("Fichas ganadas", calls_str)
        self.assertIn("●", calls_str)

    @patch('builtins.print')
    def test_imprimir_tablero_con_fichas_comidas_y_ganadas(self, mock_print):
        """Test imprimir tablero con fichas comidas y ganadas simultáneamente"""
        tablero_con_fichas = [[] for _ in range(24)]
        tablero_con_fichas[0] = [Ficha(TipoFicha.NEGRA.value) for _ in range(5)]
        
        tablero = Tablero(tablero_con_fichas, self.validador)
        tablero.fichas_comidas = [Ficha(TipoFicha.ROJA.value)]
        tablero.fichas_ganadas = [Ficha(TipoFicha.NEGRA.value) for _ in range(10)]
        
        Tablero_Impresor.imprimir_tablero(tablero)
        
        calls = [str(call) for call in mock_print.call_args_list]
        calls_str = " ".join(calls)
        self.assertIn("Fichas comidas", calls_str)
        self.assertIn("Fichas ganadas", calls_str)

        self.assertIn("●", calls_str)

    @patch('builtins.print')
    def test_imprimir_tablero_altura_maxima(self, mock_print):
        """Test imprimir tablero con altura máxima variada en diferentes puntos"""
        tablero_con_fichas = [[] for _ in range(24)]
        tablero_con_fichas[0] = [Ficha(TipoFicha.NEGRA.value) for _ in range(10)]
        tablero_con_fichas[6] = [Ficha(TipoFicha.ROJA.value) for _ in range(5)]
        tablero_con_fichas[18] = [Ficha(TipoFicha.NEGRA.value) for _ in range(8)]
        
        tablero = Tablero(tablero_con_fichas, self.validador)
        Tablero_Impresor.imprimir_tablero(tablero)
        
        self.assertEqual(mock_print.call_count, 333)

    @patch('builtins.print')
    def test_imprimir_tablero_puntos_iniciales(self, mock_print):
        """Test verificar que se imprimen todos los puntos del tablero"""
        tablero_vacio = [[] for _ in range(24)]
        tablero = Tablero(tablero_vacio, self.validador)
        
        Tablero_Impresor.imprimir_tablero(tablero)
        
        calls = [str(call) for call in mock_print.call_args_list]
        calls_str = " ".join(calls)
        
        self.assertIn("Puntos 11-0", calls_str)
        self.assertIn("Puntos 12-23", calls_str)
        self.assertNotIn("●", calls_str)


if __name__ == '__main__':
    unittest.main()