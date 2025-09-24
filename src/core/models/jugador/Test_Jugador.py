import unittest
from src.core.models.jugador.Jugador import Jugador


class TestDados(unittest.TestCase):

    def setUp(self):
        self.jugador = Jugador("Jugador1")

    def test_repr(self):
        self.assertEqual(repr(self.jugador), "Jugador1")


if __name__ == "__main__":
    unittest.main()
