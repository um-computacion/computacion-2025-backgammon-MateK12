import unittest 
from src.core.models.jugador.Jugador import Jugador
from src.core.enums.TipoFicha import TipoFicha
from src.cli.cli import CLI
class TestCli(unittest.TestCase):
    def setUp(self):
        self.jugador1 = Jugador('Juan')
        self.jugador2 = Jugador('Maria')
        self.cli = CLI(self.jugador1, self.jugador2)
    def test_getterJugador_1(self):
        self.assertEqual(self.cli.jugador_rojo, self.jugador1)

    def test_getterJugador_2(self):
        self.assertEqual(self.cli.jugador_negro, self.jugador2)
    def test_getterDadosDisponibles(self):
        self.assertEqual(self.cli.dados_disponibles, [])
if __name__=="__main__":
    unittest.main()
