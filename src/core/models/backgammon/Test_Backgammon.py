import unittest
from unittest.mock import Mock, patch
from src.core.models.backgammon.backgammon import Backgammon
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.NoHayFichaEnTriangulo import NoHayFichaEnTriangulo
from src.core.models.ficha.Ficha import Ficha

class TestBackgammon(unittest.TestCase):
    def setUp(self):
        self.game = Backgammon()

    def test_tirar_dados(self):
        with patch('src.core.models.dado.Dados.Dados.tirar_dados') as mock_dados:
            mock_dados.return_value = {'dado1': 4, 'dado2': 6,'doble': False}
            resultado = self.game.tirar_dados()
            self.assertEqual(resultado, {'dado1': 4, 'dado2': 6,'doble': False})
    def test_tirar_dados_dobles(self):
        with patch('src.core.models.dado.Dados.Dados.tirar_dados') as mock_dados:
            mock_dados.return_value = {'dado1': 6, 'dado2': 6,'doble': True}
            resultado = self.game.tirar_dados()
            self.assertEqual(resultado, {'dado1': 6, 'dado2': 6,'doble': True})

    def test_get_tablero(self):
        resultado = self.game.tablero
        self.assertIsNotNone(resultado)
    def test_cambiar_turno(self):
        self.game.quien_empieza()
        turno_anterior = self.game.turno
        self.game.cambiar_turno()
        self.assertNotEqual(self.game.turno,turno_anterior)
    # def test_mover_ficha(self):
    #     self.game.__tablero__.mover_ficha()
    #     self.game.mover_ficha()

    # def test_seleccionar_ficha(self):
    #     with self.assertRaises(AttributeError):
    #         self.game.seleccionar_ficha(0, TipoFicha.NEGRA)
    def test_dados_property(self):
        self.assertIsNotNone(self.game.dados)
    def test_hay_fichas_comidas_sin_fichas(self):
        self.game.quien_empieza()
        self.game.__tablero__.fichas_comidas = []
        resultado = self.game.hay_fichas_comidas()
        self.assertFalse(resultado)

    def test_hay_fichas_comidas_con_fichas(self):
        self.game.quien_empieza()
        tipo_ficha = TipoFicha.NEGRA.value if self.game.turno == TipoFicha.NEGRA.value else TipoFicha.ROJA.value
        ficha_comida = Ficha(tipo_ficha)
        self.game.__tablero__.fichas_comidas = [ficha_comida]
        resultado = self.game.hay_fichas_comidas()
        self.assertTrue(resultado)

    def test_seleccionar_ficha_existente(self):
        resultado = self.game.seleccionar_ficha(0, TipoFicha.NEGRA.value)
        self.assertIsNot(resultado, None)
    def test_hay_ganador_none_si_no_hay_ganador(self):
        resultado = self.game.hay_ganador()
        self.assertIsNone(resultado)
    def test_seleccionar_ficha_no_existente(self):
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.seleccionar_ficha(1, TipoFicha.NEGRA.value)

    def test_seleccionar_ficha_color_incorrecto(self):
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.seleccionar_ficha(0, TipoFicha.ROJA.value)
    def test_inicializar_tablero(self):
        game = Backgammon()
        tablero = game.inicializar_tablero()

        self.assertEqual(len(tablero), 24)

        self.assertEqual(len(tablero[0]), 2)
        self.assertEqual(len(tablero[11]), 5)
        self.assertEqual(len(tablero[16]), 3)
        self.assertEqual(len(tablero[18]), 5)

        self.assertEqual(tablero[0][0].tipo, TipoFicha.NEGRA.value)
        self.assertEqual(tablero[11][0].tipo, TipoFicha.NEGRA.value)
        self.assertEqual(tablero[16][0].tipo, TipoFicha.NEGRA.value)
        self.assertEqual(tablero[18][0].tipo, TipoFicha.NEGRA.value)

        self.assertEqual(len(tablero[23]), 2)
        self.assertEqual(len(tablero[12]), 5)
        self.assertEqual(len(tablero[7]), 3)
        self.assertEqual(len(tablero[5]), 5)

        self.assertEqual(tablero[23][0].tipo, TipoFicha.ROJA.value)
        self.assertEqual(tablero[12][0].tipo, TipoFicha.ROJA.value)
        self.assertEqual(tablero[7][0].tipo, TipoFicha.ROJA.value)
        self.assertEqual(tablero[5][0].tipo, TipoFicha.ROJA.value)

        posiciones_vacias = [1,2,3,4,6,8,9,10,13,14,15,17,19,20,21,22]
        for pos in posiciones_vacias:
            self.assertEqual(len(tablero[pos]), 0)

    def test_seleccionar_ficha_triangulo_invalido(self):
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.seleccionar_ficha(-1, TipoFicha.NEGRA.value)
    def test_seleccionar_ficha_triangulo_mayor_23(self):
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.seleccionar_ficha(24, TipoFicha.NEGRA.value)
    @patch.object(Backgammon, 'tirar_dados')
    def test_mover_ficha(self, mock_tirar_dados):
        mock_tirar_dados.return_value = [1, 2]
        self.game.quien_empieza()

        self.game.mover_ficha(0,1)
        self.assertEqual(len(self.game.tablero.tablero[0]),1)
        self.assertEqual(len(self.game.tablero.tablero[1]),1)
        self.assertEqual(self.game.tablero.tablero[1][0].tipo,TipoFicha.NEGRA.value)
    @patch.object(Backgammon, 'tirar_dados')
    def test_quien_empieza_roja_gana(self, mock_tirar_dados):
        mock_tirar_dados.return_value = [5, 3]
        self.game.quien_empieza()
        self.assertEqual(self.game.turno, TipoFicha.ROJA.value)

    @patch.object(Backgammon, 'tirar_dados')
    def test_quien_empieza_negra_gana(self, mock_tirar_dados):
        mock_tirar_dados.return_value = [2, 6]
        self.game.quien_empieza()
        self.assertEqual(self.game.turno, TipoFicha.NEGRA.value)

    @patch.object(Backgammon, 'tirar_dados')
    def test_quien_empieza_empate_luego_negra(self, mock_tirar_dados):
        mock_tirar_dados.side_effect = [[3, 3], [1, 5]]
        self.game.quien_empieza()
        self.assertEqual(self.game.turno, TipoFicha.NEGRA.value)
        self.assertEqual(mock_tirar_dados.call_count, 2)

if __name__ == '__main__':
    unittest.main()