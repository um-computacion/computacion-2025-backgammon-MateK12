import unittest
from src.core.models.jugador.Jugador import Jugador
from src.core.enums.TipoFicha import TipoFicha
from src.cli.cli import CLI
from unittest.mock import patch, Mock
from src.core.exceptions.SeleccionDadoInvalida import SeleccionDadoInvalida
from src.core.exceptions.SeleccionTrianguloInvalida import SeleccionTrianguloInvalida
from src.core.models.backgammon.backgammon import Backgammon
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador
from src.core.models.tablero.Tablero import Tablero
from src.core.models.tablero.Tablero import Tablero_Validador
from src.core.models.dado.Dados import Dados
from unittest.mock import patch, MagicMock
from src.core.helpers.Tablero_Impresor import Tablero_Impresor
from src.core.models.backgammon.Backgammon_Turnos import Backgammon_Turnos
from src.core.exceptions.NingunMovimientoPosible import NingunMovimientoPosible
# pylint: disable=C0116
class TestCli(unittest.TestCase):
    def setUp(self):
        self.jugador1 = Jugador("Juan")
        self.jugador2 = Jugador("Maria")
        tablero =Tablero(Tablero_inicializador.inicializar_tablero(), Tablero_Validador())
        turnero = Backgammon_Turnos(Dados())
        backgammon = Backgammon(tablero, Dados(), turnero)
        self.cli = CLI(self.jugador1, self.jugador2, backgammon)
        self.cli.backgammon.turnero.quien_empieza()

    def test_getter_Jugador_1(self):
        self.assertEqual(self.cli.jugador_rojo, self.jugador1)

    def test_getter_Jugador_2(self):
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
        self.assertTrue(self.cli.seleccion_dado_valida("0"))
        self.assertTrue(self.cli.seleccion_dado_valida("1"))
        self.assertTrue(self.cli.seleccion_dado_valida("2"))

    # region dado_seleccion valida
    def test_seleccion_dado_invalida_fuera_rango(self):
        """Test selección de dado inválida - fuera de rango"""
        self.cli.dados_disponibles = [1, 2]
        with self.assertRaises(SeleccionDadoInvalida):
            self.cli.seleccion_dado_valida("3")

    def test_seleccion_dado_invalida_negativa(self):
        """Test selección de dado inválida - número negativo"""
        self.cli.dados_disponibles = [1, 2]
        with self.assertRaises(SeleccionDadoInvalida):
            self.cli.seleccion_dado_valida("-1")

    def test_seleccion_dado_invalida_no_numerico(self):
        """Test selección de dado inválida - no numérico"""
        self.cli.dados_disponibles = [1, 2]
        with self.assertRaises(SeleccionDadoInvalida):
            self.cli.seleccion_dado_valida("a")

    def test_seleccion_dado_invalida_vacio(self):
        """Test selección de dado inválida - string vacío"""
        self.cli.dados_disponibles = [1, 2]
        with self.assertRaises(SeleccionDadoInvalida):
            self.cli.seleccion_dado_valida("")

    # endsregion
    # region triangulo_seleccion valida
    def test_seleccion_triangulo_valida_correcta(self):
        """Test selección de triángulo válida"""
        self.assertTrue(self.cli.seleccion_triangulo_valida("0"))
        self.assertTrue(self.cli.seleccion_triangulo_valida("12"))
        self.assertTrue(self.cli.seleccion_triangulo_valida("23"))

    def test_seleccion_triangulo_invalida_fuera_rango(self):
        """Test selección de triángulo inválida - fuera de rango"""
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.cli.seleccion_triangulo_valida("24")
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.cli.seleccion_triangulo_valida("-1")

    def test_seleccion_triangulo_invalida_no_numerico(self):
        """Test selección de triángulo inválida - no numérico"""
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.cli.seleccion_triangulo_valida("abc")

    def test_seleccion_triangulo_invalida_vacio(self):
        """Test selección de triángulo inválida - string vacío"""
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.cli.seleccion_triangulo_valida("")

    # endregion
    # region inicializar_juego
    def test_inicializar_juego(self):
        """Test inicialización del juego"""
        with patch(
            "builtins.input", side_effect=["Jugador1", "Jugador2"]
        ), patch.object(
            self.cli.backgammon.turnero, "quien_empieza"
        ) as mock_quien_empieza, patch(
            "builtins.print"
        ):

            self.cli.inicializar_juego()

            self.assertEqual(self.cli.jugador_rojo.__repr__(), "Jugador1")
            self.assertEqual(self.cli.jugador_negro.__repr__(), "Jugador2")
            mock_quien_empieza.assert_called_once()

    # endregion

    # region realizar_movimiento
    def test_realizar_movimiento_con_fichas_comidas_dado_valido(self):
        """Test realizar movimiento cuando hay fichas comidas y el dado es válido"""
        self.cli.dados_disponibles = [3, 5]

        with patch("builtins.input", return_value="0"), patch(
            "builtins.print"
        ), patch.object(
            self.cli.backgammon, "hay_fichas_comidas", return_value=True
        ), patch.object(
            self.cli.backgammon, "mover_ficha_comida"
        ) as mock_mover_comida, patch(
            "src.core.helpers.Tablero_Impresor.Tablero_Impresor.imprimir_tablero"
        ):

            self.cli.realizar_movimiento()

            mock_mover_comida.assert_called_once_with(3)
            self.assertEqual(self.cli.dados_disponibles, [5])

    def test_realizar_movimiento_sin_fichas_comidas_dado_y_triangulo_validos(self):
        """Test realizar movimiento cuando NO hay fichas comidas, dado y triángulo válidos"""
        self.cli.dados_disponibles = [2, 4]

        with patch("builtins.input", side_effect=["1", "5"]), patch(
            "builtins.print"
        ), patch.object(
            self.cli.backgammon, "hay_fichas_comidas", return_value=False
        ), patch.object(
            self.cli.backgammon, "mover_ficha"
        ) as mock_mover_ficha, patch(
            "src.core.helpers.Tablero_Impresor.Tablero_Impresor.imprimir_tablero"
        ):

            self.cli.realizar_movimiento()

            mock_mover_ficha.assert_called_once_with(5, 4)
            self.assertEqual(self.cli.dados_disponibles, [2])

    def test_realizar_movimiento_dado_invalido(self):
        """Test realizar movimiento con selección de dado inválida"""
        self.cli.dados_disponibles = [1, 3]

        with patch("builtins.input", return_value="5"), patch("builtins.print"):

            with patch.object(
                self.cli.backgammon, "hay_fichas_comidas"
            ) as mock_hay_comidas, patch.object(
                self.cli.backgammon, "mover_ficha_comida"
            ) as mock_mover_comida, patch.object(
                self.cli.backgammon, "mover_ficha"
            ) as mock_mover_ficha:

                with self.assertRaises(SeleccionDadoInvalida):
                    self.cli.realizar_movimiento()

                mock_hay_comidas.assert_not_called()
                mock_mover_comida.assert_not_called()
                mock_mover_ficha.assert_not_called()

    def test_realizar_movimiento_sin_fichas_comidas_triangulo_invalido(self):
        """Test realizar movimiento sin fichas comidas pero triángulo inválido"""
        self.cli.dados_disponibles = [2, 6]

        with patch("builtins.input", side_effect=["0", "25"]), patch(
            "builtins.print"
        ), patch.object(
            self.cli.backgammon, "hay_fichas_comidas", return_value=False
        ), patch.object(
            self.cli.backgammon, "mover_ficha"
        ) as mock_mover_ficha:

            with self.assertRaises(SeleccionTrianguloInvalida):
                self.cli.realizar_movimiento()

            mock_mover_ficha.assert_not_called()
            self.assertEqual(self.cli.dados_disponibles, [2, 6])

    # endregion
    # region tirar_dados
    def test_tirar_dados_sin_dobles(self):
        """Test tirar dados cuando NO salen dobles"""
        with patch.object(
            self.cli.backgammon.dados, "tirar_dados", return_value=[3, 5]
        ), patch("builtins.print"):
            resultado = self.cli.tirar_dados()
            self.assertEqual(resultado, [3, 5])
            self.assertEqual(self.cli.dados_disponibles, [3, 5])

    def test_tirar_dados_dobles(self):
        """Test tirar dados cuando salen dobles"""
        with patch.object(
            self.cli.backgammon.dados, "tirar_dados", return_value=[3, 3, 3, 3]
        ), patch("builtins.print") as mock_print:
            resultado = self.cli.tirar_dados()
            self.assertEqual(resultado, [3, 3, 3, 3])
            mock_print.assert_called_with("Dados tirados: [3, 3, 3, 3]")
            self.assertEqual(self.cli.dados_disponibles, [3, 3, 3, 3])

    # endregion
    def test_mostrar_ganador_rojo(self):
        """Test mostrar ganador cuando gana el jugador rojo"""
        with patch.object(
            self.cli.backgammon, "hay_ganador", return_value=TipoFicha.ROJA.value
        ), patch("builtins.print") as mock_print:
            self.cli.mostrar_ganador()
            mock_print.assert_called_once_with("¡El jugador rojo ha ganado!")
    def test_mostrar_ganador_negro(self):
        """Test mostrar ganador cuando gana el jugador negro"""
        with patch.object(
            self.cli.backgammon, "hay_ganador", return_value=TipoFicha.NEGRA.value
        ), patch("builtins.print") as mock_print:
            self.cli.mostrar_ganador()
            mock_print.assert_called_once_with("¡El jugador negro ha ganado!")
    def test_jugar(self):
        """Test jugar"""
        with patch("builtins.print") as mock_print, patch.object(
            Tablero_Impresor, "imprimir_tablero"
        ) as mock_tablero_impresor, patch.object(self.cli, 'tirar_dados') as mock_tirar_dados, unittest.mock.patch('builtins.input', return_value=''), patch.object(self.cli,'mostrar_ganador') as mock_mostrar_ganador:
            self.cli.backgammon.hay_ganador = MagicMock(side_effect=[None,None, TipoFicha.ROJA])

            self.cli.jugar()
            mock_print.assert_called()
            mock_tablero_impresor.assert_called_once()
            mock_tirar_dados.assert_called()
            mock_mostrar_ganador.assert_called_once()
if __name__ == "__main__":
    unittest.main()
