import unittest
import pygame
from src.pygame_ui.ui import BackgammonUI,WINDOW_HEIGHT,WINDOW_WIDTH
from unittest.mock import Mock, MagicMock,patch
from src.core.enums.TipoFicha import TipoFicha
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


        self.mock_backgammon.cambiar_turno.assert_called_once()
        self.assertFalse(self.ui._BackgammonUI__dados_tirados)

    def mostrar_ganador_rojo(self):
        self.mock_backgammon.hay_ganador.return_value = TipoFicha.ROJA
        self.ui.mostrar_ganador()
        self.mock_cartel_victoria.mostrar_cartel.assert_called_once_with("¡El jugador Rojo ha ganado!",5.0,titulo="Ganador")
    def mostrar_ganador_negro(self):
        self.mock_backgammon.hay_ganador.return_value = TipoFicha.NEGRA
        self.ui.mostrar_ganador()
        self.mock_cartel_victoria.mostrar_cartel.assert_called_once_with("¡El jugador Negro ha ganado!",5.0,titulo="Ganador")

    def test_on_move(self):
        with patch.object(self.ui,'puede_hacer_algun_movimiento') as mock_puede_hacer_movimiento, patch.object(self.ui,'realizar_movimiento') as mock_realizar_movimiento:
            self.ui.onMove()
            mock_puede_hacer_movimiento.assert_called_once()
            mock_realizar_movimiento.assert_called_once()
    # @patch('pygame.time.Clock')
    # @patch('pygame.event.get')
    # @patch('pygame.quit')
    # @patch('sys.exit')
    # def test_jugar_maneja_evento_boton_mover(self, mock_exit, mock_quit, mock_events, mock_clock):
    #     """Test que verifica que jugar maneja el evento del botón mover"""
    #     # Setup mocks
    #     mock_clock_instance = MagicMock()
    #     mock_clock.return_value = mock_clock_instance
    #     mock_clock_instance.tick.return_value = 16
        
    #     # Crear evento de botón
    #     mock_event = MagicMock()
    #     mock_event.type = pygame_gui.UI_BUTTON_START_PRESS
    #     mock_event.ui_element = self.mock_campos_ui.boton_mover

    #     mock_events.side_effect = [[mock_event], []]


    #     with patch.object(self.ui, 'onMove') as mock_onMove, patch.object(self.ui.__backgammon.hay_ganador) as mock_hay_ganador:
    #         mock_hay_ganador.side_effect = [None, None, TipoFicha.ROJA]
    #         self.ui.jugar()
    #         mock_onMove.assert_called_once()

    def tearDown(self):
        pygame.quit()
if __name__ == "__main__":
    unittest.main()