import unittest
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha


class TestFicha(unittest.TestCase):

    def test_repr_ficha_negra(self):
        ficha = Ficha(TipoFicha.NEGRA.value)
        self.assertEqual(repr(ficha), "\033[30m●\033[0m")

    def test_repr_ficha_roja(self):
        ficha = Ficha(TipoFicha.ROJA.value)
        self.assertEqual(repr(ficha), "\033[31m●\033[0m")

    def test_comida_getter(self):
        ficha = Ficha(TipoFicha.NEGRA.value)
        self.assertFalse(ficha.comida)

    def test_comida_setter(self):
        ficha = Ficha(TipoFicha.NEGRA.value)
        ficha.comida = True
        self.assertTrue(ficha.comida)


if __name__ == "__main__":
    unittest.main()
