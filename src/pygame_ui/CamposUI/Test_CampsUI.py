import unittest
from unittest.mock import patch, MagicMock
from src.core.enums.TipoFicha import TipoFicha
from src.core.models.ficha.Ficha import Ficha
import os

os.environ['SDL_VIDEODRIVER'] = 'dummy' 
os.environ['SDL_AUDIODRIVER'] = 'dummy'
os.environ['SDL_HIDDEN'] = '1'
# pylint: disable=C0116

class TestCampsUI(unittest.TestCase):
    @patch("pygame_gui.UIManager")
    @patch("pygame.font.Font")
    @patch('pygame.display.set_mode')
    @patch('pygame.init')
    def setUp(self, mock_font, mock_ui_manager, mock_set_mode, mock_pygame_init):
        mock_font_instance = MagicMock()
        mock_font.return_value = mock_font_instance
        mock_manager_instance = MagicMock()
        mock_ui_manager.return_value = mock_manager_instance
        from src.pygame_ui.CamposUI.camposUI import CamposUi

        self.campos_ui = CamposUi(1500, 700)
        self.campos_ui.dados_actuales = [1, 2]

    @patch("pygame_gui.elements.UIDropDownMenu")
    @patch("pygame_gui.elements.UIButton")
    def test_construir_elementos(self, mock_button, mock_dropdown):
        self.assertFalse(self.campos_ui.elementos_creados)
        self.campos_ui._CamposUi__crear_elementos()
        self.assertIsNotNone(self.campos_ui.select_triangulo)
        self.assertIsNotNone(self.campos_ui._CamposUi__select_dado)
        self.assertIsNotNone(self.campos_ui.boton_mover)
        self.assertIsNotNone(self.campos_ui._CamposUi__text_triangulo)
        self.assertIsNotNone(self.campos_ui._CamposUi__text_dado)
        self.assertIsNotNone(self.campos_ui._CamposUi__text_turno)

    @patch("pygame_gui.elements.UIDropDownMenu")
    @patch("pygame_gui.elements.UIButton")
    def test_elementos_no_duplicados(self, mock_button, mock_dropdown):

        self.campos_ui._CamposUi__crear_elementos()
        self.campos_ui._CamposUi__crear_elementos()
        self.assertEqual(mock_dropdown.call_count, 2)

        self.assertEqual(mock_button.call_count, 1)

        self.assertIsNotNone(self.campos_ui.select_triangulo)
        self.assertIsNotNone(self.campos_ui._CamposUi__select_dado)
        self.assertIsNotNone(self.campos_ui.boton_mover)

    def test_manager_getter(self):
        manager = self.campos_ui.manager
        self.assertIsNotNone(manager)
        self.assertEqual(manager, self.campos_ui.manager)

    def test_elementos_creados_getter(self):
        self.assertFalse(self.campos_ui.elementos_creados)

    def test_turno_actual_getter_setter(self):
        self.assertIsNone(self.campos_ui.turno_actual)

        self.campos_ui.turno_actual = TipoFicha.ROJA.value
        self.assertEqual(self.campos_ui.turno_actual, TipoFicha.ROJA.value)

        self.campos_ui.turno_actual = TipoFicha.NEGRA.value
        self.assertEqual(self.campos_ui.turno_actual, TipoFicha.NEGRA.value)

    def test_boton_mover_getter(self):
        self.assertIsNone(self.campos_ui.boton_mover)

    def test_dados_actuales_setter_tipo_correcto(self):
        casos_dados = [[1, 2], [6, 6, 6, 6], [1], []]

        for dados in casos_dados:
            with self.subTest(dados=dados):
                self.campos_ui.dados_actuales = dados
                self.assertEqual(self.campos_ui.dados_actuales, dados)

    def test_boton_mover_despues_crear_elementos(self):
        with patch("pygame.font.Font") as mock_font, patch(
            "pygame_gui.elements.UIDropDownMenu"
        ) as mock_dropdown, patch("pygame_gui.elements.UIButton") as mock_button:

            mock_button_instance = MagicMock()
            mock_button.return_value = mock_button_instance
            mock_dropdown.return_value = MagicMock()
            mock_font.return_value = MagicMock()

            self.campos_ui.dados_actuales = [1, 2]

            self.campos_ui._CamposUi__crear_elementos()

            self.assertIsNotNone(self.campos_ui.boton_mover)
            self.assertEqual(self.campos_ui.boton_mover, mock_button_instance)

    def test_get_text_turno_rojo(self):
        self.campos_ui.turno_actual = TipoFicha.ROJA.value
        texto = self.campos_ui._CamposUi__get_text_turno()
        self.assertEqual(texto, "Turno del jugador Rojo")

    def test_get_text_turno_negro(self):
        self.campos_ui.turno_actual = TipoFicha.NEGRA.value
        texto = self.campos_ui._CamposUi__get_text_turno()
        self.assertEqual(texto, "Turno del jugador Negro")

    def test_dibujar_textos(self):
        screen = MagicMock()
        self.campos_ui._CamposUi__text_dado = MagicMock()
        self.campos_ui._CamposUi__text_turno = MagicMock()
        self.campos_ui._CamposUi__text_triangulo = MagicMock()
        self.campos_ui._CamposUi__dibujar_textos(screen)
        screen.blit.assert_called()
        self.assertEqual(screen.blit.call_count, 3)

    def test_get_dado_seleccionado(self):
        self.campos_ui._CamposUi__select_dado = MagicMock()
        self.campos_ui._CamposUi__select_dado.selected_option = ("Dado 1: 3", None)
        dado = self.campos_ui.get_dado_seleccionado()
        self.assertEqual(dado, 3)

    def test_get_dado_no_seleccionado(self):
        self.campos_ui._CamposUi__select_dado = MagicMock()
        self.campos_ui._CamposUi__select_dado.selected_option = None
        dado = self.campos_ui.get_dado_seleccionado()
        self.assertIsNone(dado)

    def test_get_text_fichas_comidas(self):
        self.campos_ui.fichas_comidas = [
            Ficha(TipoFicha.NEGRA.value),
            Ficha(TipoFicha.NEGRA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        texto = self.campos_ui._CamposUi__get_text_fichas_comidas()
        self.assertEqual(texto, "Fichas comidas - Negras: 2 Rojas: 1")

    def test_get_text_fichas_comidas_vacio(self):
        self.campos_ui.fichas_comidas = []
        texto = self.campos_ui._CamposUi__get_text_fichas_comidas()
        self.assertEqual(texto, "Fichas comidas - Negras: 0 Rojas: 0")

    def test_getter_fichas_comidas(self):
        self.campos_ui.fichas_comidas = [
            Ficha(TipoFicha.NEGRA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        self.assertEqual(len(self.campos_ui.fichas_comidas), 2)
        self.assertEqual(self.campos_ui.fichas_comidas[0].tipo, TipoFicha.NEGRA.value)
        self.assertEqual(self.campos_ui.fichas_comidas[1].tipo, TipoFicha.ROJA.value)

    def test_setter_fichas_comidas(self):
        self.campos_ui.fichas_comidas = [
            Ficha(TipoFicha.NEGRA.value),
            Ficha(TipoFicha.ROJA.value),
        ]
        self.assertEqual(len(self.campos_ui.fichas_comidas), 2)
        self.campos_ui.fichas_comidas = [Ficha(TipoFicha.NEGRA.value)]
        self.assertEqual(len(self.campos_ui.fichas_comidas), 1)

    def test_getter_select_dado(self):
        self.campos_ui._CamposUi__select_dado = MagicMock()
        self.assertIsNotNone(self.campos_ui.select_dado)
        self.assertEqual(
            self.campos_ui.select_dado, self.campos_ui._CamposUi__select_dado
        )


if __name__ == "__main__":
    unittest.main()
