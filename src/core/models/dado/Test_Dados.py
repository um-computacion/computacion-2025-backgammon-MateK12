import unittest
from unittest.mock import patch
from src.core.models.dado.Dados import Dados

class TestDados(unittest.TestCase):
    
    def setUp(self):
        self.dados = Dados()

    def test_dados_diferentes_no_dobles(self):
        with patch('random.randint', side_effect=[3, 4]):
            resultado = self.dados.tirar_dados()
            self.assertEqual(resultado['dado1'], 3)
            self.assertEqual(resultado['dado2'], 4)
            self.assertFalse(self.dados.doble)

    def test_dados_iguales_son_dobles(self):
        with patch('random.randint', side_effect=[5, 5]):
            resultado = self.dados.tirar_dados()
            self.assertEqual(resultado['dado1'], 5)
            self.assertEqual(resultado['dado2'], 5)
            self.assertTrue(self.dados.doble)

    def test_rango_dados_valido(self):
        resultado = self.dados.tirar_dados()
        self.assertTrue(1 <= resultado['dado1'] <= 6)
        self.assertTrue(1 <= resultado['dado2'] <= 6)

if __name__ == '__main__':
    unittest.main()