import unittest
import pygame
from src.pygame_ui.ui import BackgammonUI,WINDOW_HEIGHT,WINDOW_WIDTH
from unittest.mock import Mock, MagicMock,patch
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.NingunMovimientoPosible import NingunMovimientoPosible
import pygame_gui
class Test_Ui(unittest.TestCase):
    def setUp(self):
        pygame.init()

        self.mock_backgammon = MagicMock()
        self.mock_tablero_ui = MagicMock()
        self.mock_campos_ui = MagicMock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.mock_cartel_error = MagicMock()
        self.mock_cartel_victoria = MagicMock()
        
        self.mock_backgammon.dados.tirar_dados.return_value = [3, 5]
        self.mock_backgammon.turno = 1 
        self.mock_backgammon.hay_ganador.return_value = False
        self.mock_campos_ui.get_dado_seleccionado.return_value = 3
        self.mock_campos_ui.get_seleccion_triangulo.return_value = 5
        self.mock_campos_ui.manager = MagicMock()
        self.mock_campos_ui.boton_mover = MagicMock()
        
        self.ui = BackgammonUI(
            backgammon=self.mock_backgammon,
            tableroUI=self.mock_tablero_ui,
            camposUi=self.mock_campos_ui,
            surface=self.screen,
            cartel_error=self.mock_cartel_error,
            cartel_victoria=self.mock_cartel_victoria
        )
    @patch('src.pygame_ui.ui.BackgammonUI')
    @patch('src.pygame_ui.ui.pygame.display.set_mode')
    def test_main_function(self, mock_display, mock_ui):
        """Test de la función main"""
        from src.pygame_ui.ui import main
        
        mock_ui_instance = MagicMock()
        mock_ui.return_value = mock_ui_instance
        
        main()
        
        mock_ui.assert_called_once()
        mock_ui_instance.jugar.assert_called_once()
    def test_tirar_dados(self):
        self.ui.tirar_dados()
        self.mock_backgammon.dados.tirar_dados.assert_called_once()
        self.assertTrue(self.ui._BackgammonUI__dados_tirados)
        self.assertEqual(self.mock_campos_ui.dados_actuales, [3, 5])
    def test_tirar_dados_no_repite(self):
        self.ui.tirar_dados()
        self.ui.tirar_dados()
        self.mock_backgammon.dados.tirar_dados.assert_called_once()

    def test_actualizar_tablero_ui(self):
        self.ui.actualizar_tablero_ui(0.016)
        self.mock_campos_ui.manager.update.assert_called_once_with(0.016)
        self.assertEqual(self.mock_tablero_ui.tablero, self.mock_backgammon.tablero)
        self.mock_campos_ui.dibujar_campos.assert_called_once_with(self.screen)
        self.mock_tablero_ui.dibujar_tablero.assert_called_once_with(self.screen)
        self.mock_cartel_error.actualizar_y_dibujar.assert_called_once_with(self.screen)
        self.mock_cartel_victoria.actualizar_y_dibujar.assert_called_once_with(self.screen)
    def test_realizar_movimiento_normal(self):
        self.mock_backgammon.hay_fichas_comidas.return_value = False
        self.ui._BackgammonUI__dados_disponibles = [3, 5]
        self.ui.realizar_movimiento()
        self.mock_backgammon.mover_ficha.assert_called_once_with(5, 3)
        self.assertEqual(self.ui._BackgammonUI__dados_disponibles, [5])
        self.assertEqual(self.mock_campos_ui.dados_actuales, [5])

    def test_realizar_movimiento_con_fichas_comidas(self):
        self.mock_backgammon.hay_fichas_comidas.return_value = True
        self.ui._BackgammonUI__dados_disponibles = [3, 5]
        self.ui.realizar_movimiento()
        self.mock_backgammon.mover_ficha_comida.assert_called_once_with(3)
        self.assertEqual(self.ui._BackgammonUI__dados_disponibles, [5])
        self.assertEqual(self.mock_campos_ui.dados_actuales, [5])

    def test_cambiar_turno(self):
        self.ui.cambiar_turno()


        self.mock_backgammon.turnero.cambiar_turno.assert_called_once()
        self.assertFalse(self.ui._BackgammonUI__dados_tirados)

    def mostrar_ganador_rojo(self):
        self.mock_backgammon.hay_ganador.return_value = TipoFicha.ROJA
        self.ui.mostrar_ganador()
        self.mock_cartel_victoria.mostrar_cartel.assert_called_once_with("¡El jugador Rojo ha ganado!",5.0,titulo="Ganador")
    def mostrar_ganador_negro(self):
        self.mock_backgammon.hay_ganador.return_value = TipoFicha.NEGRA
        self.ui.mostrar_ganador()
        self.mock_cartel_victoria.mostrar_cartel.assert_called_once_with("¡El jugador Negro ha ganado!",5.0,titulo="Ganador")

    def test_puede_hacer_algun_movimiento_true(self):
        self.ui._BackgammonUI__dados_disponibles = [3, 5]
        self.mock_backgammon.turno = TipoFicha.ROJA.value
        self.mock_backgammon.puede_mover_ficha = MagicMock(side_effect=[False, True])
        resultado = self.ui.puede_hacer_algun_movimiento()
        self.assertTrue(resultado)
        call_count = self.mock_backgammon.puede_mover_ficha.call_count
        self.assertEqual(call_count, 2)
    def test_puede_hacer_algun_movimiento_false(self):
        self.ui._BackgammonUI__dados_disponibles = [3, 5]
        self.mock_backgammon.turno = TipoFicha.ROJA.value
        self.mock_backgammon.puede_mover_ficha = MagicMock(side_effect=[False, False])
        with self.assertRaises(NingunMovimientoPosible):
            self.ui.puede_hacer_algun_movimiento()
            call_count = self.mock_backgammon.puede_mover_ficha.call_count
            self.assertEqual(call_count, 2)


    @patch('src.pygame_ui.ui.pygame.time.get_ticks')
    @patch('src.pygame_ui.ui.pygame.time.Clock')
    @patch('src.pygame_ui.ui.pygame.event.get')
    def test_mostrar_ganador_loop_actualiza_hasta_timeout(self, mock_event_get, mock_clock_cls, mock_get_ticks):
        self.mock_backgammon.hay_ganador.return_value = TipoFicha.ROJA.value
        mock_get_ticks.side_effect = [1000, 2000, 3000, 6001]
        mock_clock = Mock()
        mock_clock.tick.return_value = 16
        mock_clock_cls.return_value = mock_clock
        mock_event_get.return_value = []

        with patch.object(self.ui, 'actualizar_tablero_ui') as mock_update:
            self.ui.mostrar_ganador()
            self.mock_cartel_victoria.mostrar_cartel.assert_called_once_with(
                "¡El jugador Rojo ha ganado!", duracion=5.0, titulo="Ganador"
            )
            self.assertGreaterEqual(mock_update.call_count, 2)

    @patch('src.pygame_ui.ui.pygame.time.get_ticks')
    @patch('src.pygame_ui.ui.pygame.time.Clock')
    @patch('src.pygame_ui.ui.pygame.event.get')
    def test_mostrar_ganador_loop_actualiza_hasta_timeout_Negro(self, mock_event_get, mock_clock_cls, mock_get_ticks):
        self.mock_backgammon.hay_ganador.return_value = TipoFicha.NEGRA.value
        mock_get_ticks.side_effect = [1000, 2000, 3000, 6001]
        mock_clock = Mock()
        mock_clock.tick.return_value = 16
        mock_clock_cls.return_value = mock_clock
        mock_event_get.return_value = []

        with patch.object(self.ui, 'actualizar_tablero_ui') as mock_update:
            self.ui.mostrar_ganador()
            self.mock_cartel_victoria.mostrar_cartel.assert_called_once_with(
                "¡El jugador Negro ha ganado!", duracion=5.0, titulo="Ganador"
            )
            self.assertGreaterEqual(mock_update.call_count, 2)


    def tearDown(self):
        pygame.quit()
if __name__ == "__main__":
    unittest.main()