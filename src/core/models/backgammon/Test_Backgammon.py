import unittest
from unittest.mock import Mock, patch
from src.core.models.backgammon.backgammon import Backgammon
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.NoHayFichaEnTriangulo import NoHayFichaEnTriangulo
from src.core.models.ficha.Ficha import Ficha
from src.core.models.dado.Dados import Dados
from src.core.models.tablero.Tablero import Tablero
from src.core.models.tablero.Tablero import Tablero_Validador
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador
# pylint: disable=C0116,W0212


class TestBackgammon(unittest.TestCase):
    def setUp(self):

        self.game = Backgammon(Tablero(Tablero_inicializador.inicializar_tablero(), Tablero_Validador()), Dados(),)

    def test_tirar_dados(self):
        with patch("src.core.models.dado.Dados.Dados.tirar_dados") as mock_dados:
            mock_dados.return_value = {"dado1": 4, "dado2": 6, "doble": False}
            resultado = self.game.tirar_dados()
            self.assertEqual(resultado, {"dado1": 4, "dado2": 6, "doble": False})

    def test_tirar_dados_dobles(self):
        with patch("src.core.models.dado.Dados.Dados.tirar_dados") as mock_dados:
            mock_dados.return_value = {"dado1": 6, "dado2": 6, "doble": True}
            resultado = self.game.tirar_dados()
            self.assertEqual(resultado, {"dado1": 6, "dado2": 6, "doble": True})

    def test_get_tablero(self):
        resultado = self.game.tablero
        self.assertIsNotNone(resultado)

    def test_cambiar_turno(self):
        self.game.quien_empieza()
        turno_anterior = self.game.turno
        self.game.cambiar_turno()
        self.assertNotEqual(self.game.turno, turno_anterior)

    def test_dados_property(self):
        self.assertIsNotNone(self.game.dados)

    def test_hay_fichas_comidas_sin_fichas(self):
        self.game.quien_empieza()
        self.game.__tablero__.fichas_comidas = []
        resultado = self.game.hay_fichas_comidas()
        self.assertFalse(resultado)

    def test_hay_fichas_comidas_con_fichas(self):
        self.game.quien_empieza()
        tipo_ficha = (
            TipoFicha.NEGRA.value
            if self.game.turno == TipoFicha.NEGRA.value
            else TipoFicha.ROJA.value
        )
        ficha_comida = Ficha(tipo_ficha)
        self.game.__tablero__.fichas_comidas = [ficha_comida]
        resultado = self.game.hay_fichas_comidas()
        self.assertTrue(resultado)

    def test_hay_fichas_comidas_con_fichas_del_otro_color(self):
        self.game.quien_empieza()
        tipo_ficha = (
            TipoFicha.ROJA.value
            if self.game.turno == TipoFicha.NEGRA.value
            else TipoFicha.NEGRA.value
        )
        ficha_comida = Ficha(tipo_ficha)
        self.game.__tablero__.fichas_comidas = [ficha_comida]
        self.assertFalse(self.game.hay_fichas_comidas())

    def test_seleccionar_ficha_existente(self):
        resultado = self.game.seleccionar_ficha(0, TipoFicha.NEGRA.value)
        self.assertIsNot(resultado, None)

    def test_hay_ganador_none_si_no_hay_ganador(self):
        resultado = self.game.hay_ganador()
        self.assertIsNone(resultado)

    def test_hay_ganador_Rojo(self):
        self.game.__tablero__.fichas_ganadas = [Ficha(TipoFicha.ROJA.value) for _ in range(15)]
        self.assertEqual(self.game.hay_ganador(), TipoFicha.ROJA.value)

    def test_hay_ganador_Negra(self):
        self.game.__tablero__.fichas_ganadas = [Ficha(TipoFicha.NEGRA.value) for _ in range(15)]
        self.assertEqual(self.game.hay_ganador(), TipoFicha.NEGRA.value)

    def test_casi_ganador(self):
        self.game.__tablero__.fichas_ganadas = [Ficha(TipoFicha.ROJA.value) for _ in range(14)]
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

    @patch.object(Backgammon, "tirar_dados")
    def test_mover_ficha_comida(self, mock_tirar_dados):
        mock_tirar_dados.return_value = [1, 2]
        self.game.quien_empieza()
        self.game.__tablero__.fichas_comidas = [Ficha(self.game.turno)]
        self.game.mover_ficha_comida(2)
        self.assertEqual(len(self.game.__tablero__.fichas_comidas), 0)
        if self.game.turno == TipoFicha.NEGRA.value:
            self.assertEqual(len(self.game.tablero.tablero[1]), 1)
            self.assertEqual(
                self.game.tablero.tablero[1][0].tipo, TipoFicha.NEGRA.value
            )
        else:
            self.assertEqual(len(self.game.tablero.tablero[-2]), 1)
            self.assertEqual(
                self.game.tablero.tablero[-2][0].tipo, TipoFicha.ROJA.value
            )

    @patch.object(Backgammon, "tirar_dados")
    def test_mover_ficha(self, mock_tirar_dados):
        mock_tirar_dados.return_value = [1, 2]
        self.game.quien_empieza()

        self.game.mover_ficha(0, 1)
        self.assertEqual(len(self.game.tablero.tablero[0]), 1)
        self.assertEqual(len(self.game.tablero.tablero[1]), 1)
        self.assertEqual(self.game.tablero.tablero[1][0].tipo, TipoFicha.NEGRA.value)

    @patch.object(Backgammon, "tirar_dados")
    def test_quien_empieza_roja_gana(self, mock_tirar_dados):
        mock_tirar_dados.return_value = [5, 3]
        self.game.quien_empieza()
        self.assertEqual(self.game.turno, TipoFicha.ROJA.value)

    @patch.object(Backgammon, "tirar_dados")
    def test_quien_empieza_negra_gana(self, mock_tirar_dados):
        mock_tirar_dados.return_value = [2, 6]
        self.game.quien_empieza()
        self.assertEqual(self.game.turno, TipoFicha.NEGRA.value)

    @patch.object(Backgammon, "tirar_dados")
    def test_quien_empieza_empate_luego_negra(self, mock_tirar_dados):
        mock_tirar_dados.side_effect = [[3, 3], [1, 5]]
        self.game.quien_empieza()
        self.assertEqual(self.game.turno, TipoFicha.NEGRA.value)
        self.assertEqual(mock_tirar_dados.call_count, 2)

    # region puede_mover_ficha
    def test_puede_mover_ficha_todas_posiciones_bloqueadas(self):
        """Test cuando todas las posiciones están bloqueadas por fichas rivales"""
        self.game._Backgammon__turno = TipoFicha.NEGRA.value

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
        self.game._Backgammon__turno = TipoFicha.ROJA.value

        # Limpiar tablero
        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[5] = [Ficha(TipoFicha.ROJA.value)]
        resultado = self.game.puede_mover_ficha(TipoFicha.ROJA.value, 6)
        self.assertTrue(resultado)
    def test_puede_mover_ficha_fichas_comidas_no_pueden_entrar(self):
        """Test cuando hay fichas comidas pero no pueden entrar al tablero"""
        self.game._Backgammon__turno = TipoFicha.NEGRA.value

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
        self.game._Backgammon__turno = TipoFicha.ROJA.value

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
        self.game._Backgammon__turno = TipoFicha.ROJA.value

        ficha_comida = Ficha(TipoFicha.ROJA.value)
        self.game.tablero.fichas_comidas.append(ficha_comida)

        self.game.tablero.tablero[22] = [
                Ficha(TipoFicha.NEGRA.value),
                Ficha(TipoFicha.NEGRA.value),
            ]

        resultado = self.game.puede_mover_ficha(TipoFicha.ROJA.value, 2)
        self.assertFalse(resultado)
    def test_puede_mover_ficha_negra_unica_opcion_bloqueada_comida(self):
        self.game._Backgammon__turno = TipoFicha.NEGRA.value

        ficha_comida = Ficha(TipoFicha.NEGRA.value)
        self.game.tablero.fichas_comidas.append(ficha_comida)

        self.game.tablero.tablero[1] = [
                Ficha(TipoFicha.ROJA.value),
                Ficha(TipoFicha.ROJA.value),
            ]

        resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, 2)
        self.assertFalse(resultado)


    def test_puede_mover_ficha_se_pasa_sin_poder_ganar(self):
        """Test cuando el movimiento se pasa del tablero y no puede ganar"""
        self.game._Backgammon__turno = TipoFicha.ROJA.value

        # Limpiar tablero
        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[2] = [Ficha(TipoFicha.ROJA.value)]
        self.game.tablero.tablero[15] = [Ficha(TipoFicha.ROJA.value)]

        resultado = self.game.puede_mover_ficha(TipoFicha.ROJA.value, 6)
        self.assertTrue(resultado)

    def test_puede_mover_ficha_completamente_bloqueado_negro(self):
        self.game._Backgammon__turno = TipoFicha.NEGRA.value

        for i in range(24):
            self.game.tablero.tablero[i] = []

        self.game.tablero.tablero[22] = [Ficha(TipoFicha.NEGRA.value)]

        self.game.tablero.tablero[10] = [Ficha(TipoFicha.NEGRA.value)]

        resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, 3)
        self.assertTrue(resultado)

    def test_puede_mover_ficha_solo_una_ficha_completamente_bloqueada(self):
        """Test con una sola ficha que no se puede mover por estar bloqueada"""
        self.game._Backgammon__turno = TipoFicha.NEGRA.value

        # Limpiar tablero completamente
        for i in range(24):
            self.game.tablero.tablero[i] = []

        # Colocar UNA SOLA ficha negra
        self.game.tablero.tablero[5] = [Ficha(TipoFicha.NEGRA.value)]

        # Bloquear su único destino posible con dado 2 (posición 7)
        self.game.tablero.tablero[7] = [
            Ficha(TipoFicha.ROJA.value),
            Ficha(TipoFicha.ROJA.value),
        ]

        resultado = self.game.puede_mover_ficha(TipoFicha.NEGRA.value, 2)
        self.assertFalse(resultado)

    def test_puede_mover_ficha_pared_completa_bloqueo(self):
        self.game._Backgammon__turno = TipoFicha.NEGRA.value

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
        self.game._Backgammon__turno = TipoFicha.ROJA.value

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
