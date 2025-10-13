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
# pylint: disable=C0116,W0212


class TestBackgammon(unittest.TestCase):
    def setUp(self):
        self.game = Backgammon(Tablero(Tablero_inicializador.inicializar_tablero(), Tablero_Validador()), Dados(),Backgammon_Turnos(Dados()))


    def test_get_tablero(self):
        resultado = self.game.tablero
        self.assertIsNotNone(resultado)


    def test_dados_property(self):
        self.assertIsNotNone(self.game.dados)

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

    def test_seleccionar_ficha_existente(self):
        resultado = self.game.seleccionar_ficha(0, TipoFicha.NEGRA.value)
        self.assertIsNot(resultado, None)

    def test_hay_ganador_none_si_no_hay_ganador(self):
        resultado = self.game.hay_ganador()
        self.assertIsNone(resultado)

    def test_hay_ganador_Rojo(self):
        self.game.tablero.fichas_ganadas = [Ficha(TipoFicha.ROJA.value) for _ in range(15)]
        self.assertEqual(self.game.hay_ganador(), TipoFicha.ROJA.value)

    def test_hay_ganador_Negra(self):
        self.game.tablero.fichas_ganadas = [Ficha(TipoFicha.NEGRA.value) for _ in range(15)]
        self.assertEqual(self.game.hay_ganador(), TipoFicha.NEGRA.value)

    def test_casi_ganador(self):
        self.game.tablero.fichas_ganadas = [Ficha(TipoFicha.ROJA.value) for _ in range(14)]
        self.assertIsNone(self.game.hay_ganador())
    
    def test_seleccionar_ficha_no_existente(self):
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.seleccionar_ficha(1, TipoFicha.NEGRA.value)

    def test_seleccionar_ficha_color_incorrecto(self):
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.seleccionar_ficha(0, TipoFicha.ROJA.value)

    def test_seleccionar_ficha_triangulo_invalido(self):
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.seleccionar_ficha(-1, TipoFicha.NEGRA.value)

    def test_seleccionar_ficha_triangulo_mayor_23(self):
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.seleccionar_ficha(24, TipoFicha.NEGRA.value)

    def test_mover_ficha_comida(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value
        self.game.tablero.fichas_comidas = [Ficha(self.game.turnero.turno)]
        self.game.mover_ficha_comida(2)
        self.assertEqual(len(self.game.tablero.fichas_comidas), 0)
        if self.game.turnero.turno == TipoFicha.NEGRA.value:
            self.assertEqual(len(self.game.tablero.tablero[1]), 1)
            self.assertEqual(
                self.game.tablero.tablero[1][0].tipo, TipoFicha.NEGRA.value
            )
        else:
            self.assertEqual(len(self.game.tablero.tablero[-2]), 1)
            self.assertEqual(
                self.game.tablero.tablero[-2][0].tipo, TipoFicha.ROJA.value
            )

    def test_mover_ficha(self, ):
        self.game.turnero.turno = TipoFicha.NEGRA.value
        self.game.mover_ficha(0, 1)
        self.assertEqual(len(self.game.tablero.tablero[0]), 1)
        self.assertEqual(len(self.game.tablero.tablero[1]), 1)
        self.assertEqual(self.game.tablero.tablero[1][0].tipo, TipoFicha.NEGRA.value)

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
        self.game.tablero.tablero[18] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]

        resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, 3)
        self.assertFalse(resultado)

    def test_puede_mover_ficha_roja_desde_5(self):
        self.game.turnero.turno = TipoFicha.ROJA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[5] = [Ficha(TipoFicha.ROJA.value)]
        resultado = self.game.puede_mover_ficha(TipoFicha.ROJA.value, 6)
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
            resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, dado)
            self.assertFalse(resultado)

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

        resultado = self.game.puede_mover_ficha(TipoFicha.ROJA.value, 2)
        self.assertFalse(resultado)

    def test_puede_mover_ficha_roja_unica_opcion_bloqueada_comida(self):
        self.game.turnero.turno = TipoFicha.ROJA.value

        ficha_comida = Ficha(TipoFicha.ROJA.value)
        self.game.tablero.fichas_comidas.append(ficha_comida)

        self.game.tablero.tablero[22] = [
                Ficha(TipoFicha.NEGRA.value),
                Ficha(TipoFicha.NEGRA.value),
            ]

        resultado = self.game.puede_mover_ficha(TipoFicha.ROJA.value, 2)
        self.assertFalse(resultado)

    def test_puede_mover_ficha_negra_unica_opcion_bloqueada_comida(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value

        ficha_comida = Ficha(TipoFicha.NEGRA.value)
        self.game.tablero.fichas_comidas.append(ficha_comida)

        self.game.tablero.tablero[1] = [
                Ficha(TipoFicha.ROJA.value),
                Ficha(TipoFicha.ROJA.value),
            ]

        resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, 2)
        self.assertFalse(resultado)

    def test_puede_mover_ficha_se_pasa_sin_poder_ganar(self):
        self.game.turnero.turno = TipoFicha.ROJA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[2] = [Ficha(TipoFicha.ROJA.value)]
        self.game.tablero.tablero[15] = [Ficha(TipoFicha.ROJA.value)]

        resultado = self.game.puede_mover_ficha(TipoFicha.ROJA.value, 6)
        self.assertTrue(resultado)

    def test_puede_mover_ficha_completamente_bloqueado_negro(self):
        self.game.turnero.turno = TipoFicha.NEGRA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[22] = [Ficha(TipoFicha.NEGRA.value)]

        self.game.tablero.tablero[10] = [Ficha(TipoFicha.NEGRA.value)]

        resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, 3)
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

        resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, 2)
        self.assertFalse(resultado)

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

        resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, 2)
        self.assertFalse(resultado)

    def test_puede_mover_ficha_todas_se_pasan_no_zona_ganancia(self):
        self.game.turnero.turno = TipoFicha.ROJA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[0] = [Ficha(TipoFicha.ROJA.value)]
        self.game.tablero.tablero[1] = [Ficha(TipoFicha.ROJA.value)]

        self.game.tablero.tablero[10] = [Ficha(TipoFicha.ROJA.value)]

        resultado = self.game.puede_mover_ficha(TipoFicha.ROJA.value, 6)
        self.assertTrue(resultado)

# end region

if __name__ == "__main__":
    unittest.main()