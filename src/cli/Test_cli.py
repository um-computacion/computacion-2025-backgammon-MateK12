import unittest 
from src.core.models.jugador.Jugador import Jugador
from src.core.enums.TipoFicha import TipoFicha
from src.cli.cli import CLI
from unittest.mock import patch, Mock
from src.core.exceptions.SeleccionDadoInvalida import SeleccionDadoInvalida
from src.core.exceptions.SeleccionTrianguloInvalida import SeleccionTrianguloInvalida
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
    def test_setter_dados_disponibles(self):
        """Test setter de dados_disponibles"""
        nuevos_dados = [1, 2, 3, 4]
        self.cli.dados_disponibles = nuevos_dados
        self.assertEqual(self.cli.dados_disponibles, nuevos_dados)
    def test_seleccion_dado_valida_correcta(self):
        """Test selección de dado válida"""
        self.cli.dados_disponibles = [1, 2, 3]
        self.assertTrue(self.cli.seleccion_dado_valida('0'))
        self.assertTrue(self.cli.seleccion_dado_valida('1'))
        self.assertTrue(self.cli.seleccion_dado_valida('2'))
    #region dado_seleccion valida
    def test_seleccion_dado_invalida_fuera_rango(self):
        """Test selección de dado inválida - fuera de rango"""
        self.cli.dados_disponibles = [1, 2]
        with self.assertRaises(SeleccionDadoInvalida):
            self.cli.seleccion_dado_valida('3')

    def test_seleccion_dado_invalida_negativa(self):
        """Test selección de dado inválida - número negativo"""
        self.cli.dados_disponibles = [1, 2]
        with self.assertRaises(SeleccionDadoInvalida):
            self.cli.seleccion_dado_valida('-1')

    def test_seleccion_dado_invalida_no_numerico(self):
        """Test selección de dado inválida - no numérico"""
        self.cli.dados_disponibles = [1, 2]
        with self.assertRaises(SeleccionDadoInvalida):
            self.cli.seleccion_dado_valida('a')

    def test_seleccion_dado_invalida_vacio(self):
        """Test selección de dado inválida - string vacío"""
        self.cli.dados_disponibles = [1, 2]
        with self.assertRaises(SeleccionDadoInvalida):
            self.cli.seleccion_dado_valida('')
    #endsregion
    #region triangulo_seleccion valida
    def test_seleccion_triangulo_valida_correcta(self):
        """Test selección de triángulo válida"""
        self.assertTrue(self.cli.seleccion_triangulo_valida('0'))
        self.assertTrue(self.cli.seleccion_triangulo_valida('12'))
        self.assertTrue(self.cli.seleccion_triangulo_valida('23'))

    def test_seleccion_triangulo_invalida_fuera_rango(self):
        """Test selección de triángulo inválida - fuera de rango"""
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.cli.seleccion_triangulo_valida('24')
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.cli.seleccion_triangulo_valida('-1')

    def test_seleccion_triangulo_invalida_no_numerico(self):
        """Test selección de triángulo inválida - no numérico"""
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.cli.seleccion_triangulo_valida('abc')

    def test_seleccion_triangulo_invalida_vacio(self):
        """Test selección de triángulo inválida - string vacío"""
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.cli.seleccion_triangulo_valida('')
    #endregion
    #region inicializar_juego
    def test_inicializar_juego(self):
        """Test inicialización del juego"""
        with patch('builtins.input', side_effect=['Jugador1', 'Jugador2']), \
             patch.object(self.cli.backgammon, 'quien_empieza') as mock_quien_empieza, \
             patch('builtins.print'):
            
            self.cli.inicializar_juego()
            
            self.assertEqual(self.cli.jugador_rojo.__repr__(), 'Jugador1')
            self.assertEqual(self.cli.jugador_negro.__repr__(), 'Jugador2')
            mock_quien_empieza.assert_called_once()

if __name__=="__main__":
    unittest.main()
