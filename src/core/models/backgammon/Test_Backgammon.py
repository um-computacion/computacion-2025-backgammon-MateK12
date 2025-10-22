import unittest
from unittest.mock import Mock, patch
from src.core.models.backgammon.backgammon import Backgammon
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.NoHayFichaEnTriangulo import NoHayFichaEnTriangulo
from src.core.models.ficha.Ficha import Ficha
from src.core.models.dado.Dados import Dados
from src.core.models.tablero.Tablero import Tablero
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador
from src.core.models.backgammon.Backgammon_Turnos import Backgammon_Turnos
from src.core.exceptions.SeleccionDadoInvalida import SeleccionDadoInvalida
from src.core.exceptions.SeleccionTrianguloInvalida import SeleccionTrianguloInvalida
from src.core.exceptions.NingunMovimientoPosible import NingunMovimientoPosible

# pylint: disable=C0116,W0212


class TestBackgammon(unittest.TestCase):
    def setUp(self):
        self.game = Backgammon(
            Tablero(Tablero_inicializador.inicializar_tablero(), Tablero_Validador()),
            Dados(),
            Backgammon_Turnos(Dados()),
        )

    def test_get_tablero(self):
        resultado = self.game.tablero
        self.assertIsNotNone(resultado)

    def test_dados_property(self):
        self.assertIsNotNone(self.game.dados)

    #region hay_fichas_comidas
    def test_hay_fichas_comidas_sin_fichas(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value
        self.game.tablero.fichas_comidas = []
        resultado = self.game.hay_fichas_comidas()
        self.assertFalse(resultado)

    def test_hay_fichas_comidas_con_fichas(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value
        tipo_ficha = (
            TipoFicha.NEGRA.value
            if self.game.turnero.turno == TipoFicha.NEGRA.value
            else TipoFicha.ROJA.value
        )
        ficha_comida = Ficha(tipo_ficha)
        self.game.tablero.fichas_comidas = [ficha_comida]
        resultado = self.game.hay_fichas_comidas()
        self.assertTrue(resultado)

    def test_hay_fichas_comidas_con_fichas_del_otro_color(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value
        tipo_ficha = (
            TipoFicha.ROJA.value
            if self.game.turnero.turno == TipoFicha.NEGRA.value
            else TipoFicha.NEGRA.value
        )
        ficha_comida = Ficha(tipo_ficha)
        self.game.tablero.__Tablero__fichas_comidas = [ficha_comida]
        self.assertFalse(self.game.hay_fichas_comidas())
    # endregion
    #region hay_ganador
    def test_hay_ganador_none_si_no_hay_ganador(self):
        resultado = self.game.hay_ganador()
        self.assertIsNone(resultado)

    def test_hay_ganador_Rojo(self):
        self.game.tablero.fichas_ganadas = [
            Ficha(TipoFicha.ROJA.value) for _ in range(15)
        ]
        self.assertEqual(self.game.hay_ganador(), TipoFicha.ROJA.value)

    def test_hay_ganador_Negra(self):
        self.game.tablero.fichas_ganadas = [
            Ficha(TipoFicha.NEGRA.value) for _ in range(15)
        ]
        self.assertEqual(self.game.hay_ganador(), TipoFicha.NEGRA.value)

    def test_casi_ganador(self):
        self.game.tablero.fichas_ganadas = [
            Ficha(TipoFicha.ROJA.value) for _ in range(14)
        ]
        self.assertIsNone(self.game.hay_ganador())
    # endregion
    # region test seleccionar ficha
    def test_seleccionar_ficha_no_existente(self):
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.tablero.tablero[1] = []
            self.game.seleccionar_ficha(1, TipoFicha.NEGRA.value)

    def test_seleccionar_ficha_color_incorrecto(self):
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.tablero.tablero[0] = [Ficha(TipoFicha.NEGRA.value)]
            self.game.seleccionar_ficha(0, TipoFicha.ROJA.value)

    def test_seleccionar_ficha_triangulo_invalido(self):
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.game.seleccionar_ficha(-1, TipoFicha.NEGRA.value)

    def test_seleccionar_ficha_triangulo_mayor_23(self):
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.game.seleccionar_ficha(24, TipoFicha.NEGRA.value)
    def test_seleccionar_ficha_existente(self):
        resultado = self.game.seleccionar_ficha(0, TipoFicha.NEGRA.value)
        self.assertIsNot(resultado, None)
    # endregion
    #region mover ficha comida
    def test_mover_ficha_comida(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value
        self.game.tablero.fichas_comidas = [Ficha(self.game.turnero.turno)]
        self.game.mover_ficha_comida(2)
        self.assertEqual(len(self.game.tablero.fichas_comidas), 0)
        self.assertEqual(len(self.game.tablero.tablero[1]), 1)
        self.assertEqual(
            self.game.tablero.tablero[1][0].tipo, TipoFicha.NEGRA.value
        )
    def test_mover_ficha_comida_roja(self):
        self.game.turnero.turno = TipoFicha.ROJA.value
        self.game.tablero.fichas_comidas = [Ficha(self.game.turnero.turno)]
        self.game.mover_ficha_comida(2)
        self.assertEqual(len(self.game.tablero.fichas_comidas), 0)
        self.assertEqual(len(self.game.tablero.tablero[22]), 1)
        self.assertEqual(
            self.game.tablero.tablero[22][0].tipo, TipoFicha.ROJA.value
        )
    # endregion
    #region mover ficha
    def test_mover_ficha(
        self,
    ):
        self.game.turnero.turno = TipoFicha.NEGRA.value
        self.game.mover_ficha(0, 1)
        self.assertEqual(len(self.game.tablero.tablero[0]), 1)
        self.assertEqual(len(self.game.tablero.tablero[1]), 1)
        self.assertEqual(self.game.tablero.tablero[1][0].tipo, TipoFicha.NEGRA.value)
    def test_mover_ficha_triangulo_invalido(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value
        self.game.tablero.tablero[1] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.game.mover_ficha(-1, 1)
    def test_mover_ficha_dado_invalido(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value
        self.game.tablero.tablero[1] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        with self.assertRaises(SeleccionDadoInvalida):
            self.game.mover_ficha(0, 7)

    #endregion
    # region puede_mover_ficha
    def test_puede_mover_ficha_todas_posiciones_bloqueadas(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[10] = [Ficha(TipoFicha.NEGRA.value)]
        self.game.tablero.tablero[15] = [Ficha(TipoFicha.NEGRA.value)]

        self.game.tablero.tablero[13] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        self.game.tablero.tablero[19] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        self.game.tablero.tablero[18] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        self.game.tablero.tablero[14] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        with self.assertRaises(NingunMovimientoPosible):
            self.game.puede_mover_ficha(TipoFicha.NEGRA.value, [3, 4])

    def test_puede_mover_ficha_roja_desde_5_para_ganar(self):
        self.game.turnero.turno = TipoFicha.ROJA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []
        self.game.tablero.tablero[4] = [Ficha(TipoFicha.ROJA.value) for _ in range(14)]
        self.game.tablero.tablero[5] = [Ficha(TipoFicha.ROJA.value)]
        resultado = self.game.puede_mover_ficha(TipoFicha.ROJA.value, [6])
        self.assertTrue(resultado)

    def test_puede_mover_ficha_fichas_comidas_no_pueden_entrar(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value

        ficha_comida = Ficha(TipoFicha.NEGRA.value)
        ficha_comida.comida = True
        self.game.tablero.fichas_comidas.append(ficha_comida)

        for i in range(6):
            self.game.tablero.tablero[i] = [
                Ficha(TipoFicha.ROJA.value),
                Ficha(TipoFicha.ROJA.value),
            ]

        for dado in range(1, 7):
            with self.assertRaises(NingunMovimientoPosible):
                self.game.puede_mover_ficha(TipoFicha.NEGRA.value, [dado])

    def test_puede_mover_ficha_roja_fichas_comidas_bloqueadas(self):
        self.game.turnero.turno = TipoFicha.ROJA.value

        ficha_comida = Ficha(TipoFicha.ROJA.value)
        ficha_comida.comida = True
        self.game.tablero.fichas_comidas.append(ficha_comida)

        for i in range(18, 24):
            self.game.tablero.tablero[i] = [
                Ficha(TipoFicha.NEGRA.value),
                Ficha(TipoFicha.NEGRA.value),
            ]

        with self.assertRaises(NingunMovimientoPosible):
            self.game.puede_mover_ficha(TipoFicha.ROJA.value, [2])

    def test_puede_mover_ficha_roja_unica_opcion_bloqueada_comida(self):
        self.game.turnero.turno = TipoFicha.ROJA.value

        ficha_comida = Ficha(TipoFicha.ROJA.value)
        self.game.tablero.fichas_comidas.append(ficha_comida)

        self.game.tablero.tablero[22] = [
            Ficha(TipoFicha.NEGRA.value),
            Ficha(TipoFicha.NEGRA.value),
        ]

        with self.assertRaises(NingunMovimientoPosible):
            self.game.puede_mover_ficha(TipoFicha.ROJA.value, [2])
    def test_puede_mover_ficha_negra_comida_un_solo_movimiento(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value

        ficha_comida = Ficha(TipoFicha.NEGRA.value)
        self.game.tablero.fichas_comidas.append(ficha_comida)
        self.game.tablero.tablero[0] = [Ficha(TipoFicha.ROJA.value),Ficha(TipoFicha.ROJA.value) ]
        self.game.tablero.tablero[1] = []

        resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, [2,1])
        self.assertTrue(resultado)
    def test_puede_mover_ficha_negra_comida_dos_movimientos(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value

        ficha_comida = Ficha(TipoFicha.NEGRA.value)
        self.game.tablero.fichas_comidas.append(ficha_comida)

        self.game.tablero.tablero[1] = []

        resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, [2,1])
        self.assertTrue(resultado)

    def test_puede_mover_ficha_negra_unica_opcion_bloqueada_comida(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value

        ficha_comida = Ficha(TipoFicha.NEGRA.value)
        self.game.tablero.fichas_comidas.append(ficha_comida)

        self.game.tablero.tablero[1] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]

        with self.assertRaises(NingunMovimientoPosible):
            self.game.puede_mover_ficha(TipoFicha.NEGRA.value, [2])

    def test_puede_mover_ficha_se_pasa_sin_poder_ganar(self):
        self.game.turnero.turno = TipoFicha.ROJA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[2] = [Ficha(TipoFicha.ROJA.value)]
        self.game.tablero.tablero[15] = [Ficha(TipoFicha.ROJA.value)]

        resultado = self.game.puede_mover_ficha(TipoFicha.ROJA.value, [6])
        self.assertTrue(resultado)

    def test_puede_mover_ficha_completamente_bloqueado_negro(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[22] = [Ficha(TipoFicha.NEGRA.value)]

        self.game.tablero.tablero[10] = [Ficha(TipoFicha.NEGRA.value)]

        resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, [3])
        self.assertTrue(resultado)

    def test_puede_mover_ficha_solo_una_ficha_completamente_bloqueada(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[5] = [Ficha(TipoFicha.NEGRA.value)]

        self.game.tablero.tablero[7] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]

        with self.assertRaises(NingunMovimientoPosible):
            self.game.puede_mover_ficha(TipoFicha.NEGRA.value, [2])

    def test_puede_mover_ficha_pared_completa_bloqueo(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[20] = [Ficha(TipoFicha.NEGRA.value)]
        self.game.tablero.tablero[21] = [Ficha(TipoFicha.NEGRA.value)]

        self.game.tablero.tablero[22] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        self.game.tablero.tablero[23] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]

        with self.assertRaises(NingunMovimientoPosible):
            self.game.puede_mover_ficha(TipoFicha.NEGRA.value, [2])

    def test_puede_mover_ficha_todas_se_pasan_no_zona_ganancia(self):
        self.game.turnero.turno = TipoFicha.ROJA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[0] = [Ficha(TipoFicha.ROJA.value)]
        self.game.tablero.tablero[1] = [Ficha(TipoFicha.ROJA.value)]

        self.game.tablero.tablero[10] = [Ficha(TipoFicha.ROJA.value)]

        resultado = self.game.puede_mover_ficha(TipoFicha.ROJA.value, [6])
        self.assertTrue(resultado)
    def test_no_puede_mover_ficahas_todas_se_pasan_home_lleno(self):
        self.game.turnero.turno = TipoFicha.ROJA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[0] = [Ficha(TipoFicha.ROJA.value)]
        self.game.tablero.tablero[1] = [Ficha(TipoFicha.ROJA.value)]
        self.game.tablero.fichas_ganadas = [Ficha(TipoFicha.ROJA.value) for _ in range(12)]

        with self.assertRaises(NingunMovimientoPosible):
            self.game.puede_mover_ficha(TipoFicha.ROJA.value, [6,4])
    def test_no_puede_mover_no_puede_ganar(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[7] = [Ficha(TipoFicha.NEGRA.value)]
        self.game.tablero.tablero[8] = [Ficha(TipoFicha.ROJA.value),Ficha(TipoFicha.ROJA.value)]

        self.game.tablero.tablero[23] = [Ficha(TipoFicha.NEGRA.value)]

        with self.assertRaises(NingunMovimientoPosible):
            self.game.puede_mover_ficha(TipoFicha.NEGRA.value, [1,1,1,1])
    # end region
    #region test seleccion dado valido
    def test_seleccion_dado_valida_valido(self):
        dado = 3
        resultado = self.game.seleccion_dado_valida(dado)
        self.assertTrue(resultado)

    def test_seleccion_dado_valida_no_entero(self):
        dado = "a"
        with self.assertRaises(SeleccionDadoInvalida):
            self.game.seleccion_dado_valida(dado)

    def test_dado_mayor_a_6(self):
        dado = 7
        with self.assertRaises(SeleccionDadoInvalida):
            self.game.seleccion_dado_valida(dado)

    def test_dado_menor_a_1(self):
        dado = 0
        with self.assertRaises(SeleccionDadoInvalida):
            self.game.seleccion_dado_valida(dado)

    def test_dado_indefinido(self):
        dado = None
        with self.assertRaises(SeleccionDadoInvalida):
            self.game.seleccion_dado_valida(dado)
    #endregion
    #region test triangulo valido
    def test_triangulo_valido(self):
        for i in range(24):
            resultado = self.game.seleccion_triangulo_valida(i)
            self.assertTrue(resultado)

    def test_triangulo_menor_a_0(self):
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.game.seleccion_triangulo_valida(-1)

    def test_triangulo_mayor_a_23(self):
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.game.seleccion_triangulo_valida(24)

    def test_triangulo_no_entero(self):
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.game.seleccion_triangulo_valida("a")

    def test_triangulo_indefinido(self):
        with self.assertRaises(SeleccionTrianguloInvalida):
            triangulo = None
            self.game.seleccion_triangulo_valida(triangulo)
    #endregion

if __name__ == "__main__":
    unittest.main()
