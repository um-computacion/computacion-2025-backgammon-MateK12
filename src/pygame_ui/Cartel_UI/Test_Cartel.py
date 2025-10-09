import unittest
from src.pygame_ui.Cartel_UI.Cartel_UI import Cartel_UI
from unittest.mock import MagicMock, patch
import pygame
import time


class TestCartel(unittest.TestCase):
    def setUp(self):
        pygame.init()

        self.cartel = Cartel_UI((800, 600))
        self.screen = pygame.Surface((800, 600))

    def test_mensaje_activo_inicial(self):
        self.assertFalse(self.cartel.mensaje_activo)
        
    def test_mostrar_cartel(self):
        self.cartel.mostrar_cartel("Test Message", duracion=2.0,titulo="Test")
        self.assertEqual(self.cartel._Cartel_UI__mensaje ,"Test Message")
        self.assertEqual(self.cartel._Cartel_UI__titulo ,"Test")
        self.assertEqual(self.cartel._Cartel_UI__duracion, 2.0)
        self.assertTrue(self.cartel.mensaje_activo)


    def test_dibujar_mensaje_se_llama_si_activo(self):
        self.cartel.mostrar_cartel("Mensaje de prueba", duracion=5.0)
        with patch.object(self.cartel, '_Cartel_UI__dibujar_mensaje') as mock_dibujar:
            self.cartel.actualizar_y_dibujar(self.screen)
            mock_dibujar.assert_called_once_with(self.screen)

    def test_dibujar_mensaje_no_se_llama_si_no_activo(self):
        with patch.object(self.cartel, '_Cartel_UI__dibujar_mensaje') as mock_dibujar:
            self.cartel.actualizar_y_dibujar(self.screen)
            mock_dibujar.assert_not_called()

    def test_dibujar_mensaje_no_se_llama_si_expirado(self):
        self.cartel.mostrar_cartel("Mensaje corto", duracion=3)
        time.sleep(3.1)
        with patch.object(self.cartel, '_Cartel_UI__dibujar_mensaje') as mock_dibujar:
            self.cartel.actualizar_y_dibujar(self.screen)
            mock_dibujar.assert_not_called()

    def test_dividir_mensaje(self):
        mensaje_largo = "Este es un mensaje de prueba que debería dividirse en varias líneas para caber en el cartel."
        lineas = self.cartel._Cartel_UI__dividir_mensaje(mensaje_largo,  40)
        self.assertTrue(len(lineas) > 1)
        self.assertEqual(lineas[0], "Este es un mensaje de prueba que")
        self.assertEqual(lineas[1], "debería dividirse en varias líneas para")
        self.assertEqual(lineas[2], "caber en el cartel.")

    @patch('pygame.draw.rect')
    def test_dibujar_cartel(self, mock_draw_rect):
        mock_screen = MagicMock()
        self.cartel.mostrar_cartel("Test mensaje", duracion=5.0, titulo="Test Titulo")
        self.cartel.actualizar_y_dibujar(mock_screen)
        mock_draw_rect.assert_called_once()
        with patch.object(self.cartel, '_Cartel_UI__dibujar_mensaje') as mock_dibujar:
            self.cartel.actualizar_y_dibujar(mock_screen)
            mock_dibujar.assert_called_once_with(mock_screen)
        with patch.object(self.cartel, '_Cartel_UI__dividir_mensaje') as mock_dividir:
            self.cartel.actualizar_y_dibujar(mock_screen)
            mock_dividir.assert_called()
if __name__ == '__main__':
    unittest.main()