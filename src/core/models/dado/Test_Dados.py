import unittest
from unittest.mock import patch
from src.core.models.dado.Dados import Dados

# pylint: disable=C0116
class TestDados(unittest.TestCase):

    def setUp(self):
        self.dados = Dados()

    def test_dados_diferentes_no_dobles(self):
        with patch("random.randint", side_effect=[3, 4]):
            resultado = self.dados.tirar_dados()
            self.assertEqual(resultado[0], 3)
            self.assertEqual(resultado[1], 4)
            self.assertFalse(self.dados.doble)

    def test_dados_iguales_son_dobles(self):
        with patch("random.randint", side_effect=[5, 5]):
            resultado = self.dados.tirar_dados()
            self.assertEqual(resultado[0], 5)
            self.assertEqual(resultado[1], 5)
            self.assertTrue(self.dados.doble)

    def test_rango_dados_valido(self):
        resultado = self.dados.tirar_dados()
        self.assertTrue(1 <= resultado[0] <= 6)
        self.assertTrue(1 <= resultado[1] <= 6)

    def test_dados_iguales_son_dobles(self):
        with patch("random.randint", side_effect=[5, 5]):
            resultado = self.dados.tirar_dados()
            self.assertEqual(resultado[0], 5)
            self.assertEqual(resultado[1], 5)
            self.assertTrue(self.dados.doble)

    def test_doble_false_principio_true_final(self):
        with patch("random.randint", side_effect=[5, 5]):
            resultado = self.dados.tirar_dados()
            self.assertEqual(resultado[0], 5)
            self.assertEqual(resultado[1], 5)
            self.assertTrue(self.dados.doble)
        with patch("random.randint", side_effect=[3, 4]):
            resultado = self.dados.tirar_dados()
            self.assertEqual(resultado[0], 3)
            self.assertEqual(resultado[1], 4)
            self.assertFalse(self.dados.doble)

    def test_longitud_correcta_dados_dobles(self):
        with patch("random.randint", side_effect=[2, 2]):
            resultado = self.dados.tirar_dados()
            self.assertEqual(len(resultado), 4)


if __name__ == "__main__":
    unittest.main()
