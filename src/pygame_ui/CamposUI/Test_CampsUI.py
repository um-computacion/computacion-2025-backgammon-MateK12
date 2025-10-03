import unittest
from unittest.mock import patch, MagicMock
from src.core.enums.TipoFicha import TipoFicha

class TestCampsUI(unittest.TestCase):
    @patch('pygame_gui.UIManager')
    @patch('pygame.font.Font')
    def setUp(self, mock_font, mock_ui_manager):
        mock_font_instance = MagicMock()
        mock_font.return_value = mock_font_instance
        
        mock_manager_instance = MagicMock()
        mock_ui_manager.return_value = mock_manager_instance
        from src.pygame_ui.CamposUI.camposUI import CamposUi
        self.campos_ui = CamposUi(1500, 700)
        self.campos_ui.dados_actuales = [1, 2]
    @patch('pygame_gui.elements.UIDropDownMenu')
    @patch('pygame_gui.elements.UIButton')
    def test_construir_elementos(self, mock_button, mock_dropdown):
        self.assertFalse(self.campos_ui.elementos_creados)
        self.campos_ui._CamposUi__crear_elementos()
        self.assertIsNotNone(self.campos_ui.select_triangulo)
        self.assertIsNotNone(self.campos_ui.select_dado)
        self.assertIsNotNone(self.campos_ui.boton_mover)
        self.assertIsNotNone(self.campos_ui._CamposUi__text_triangulo)
        self.assertIsNotNone(self.campos_ui._CamposUi__text_dado)
        self.assertIsNotNone(self.campos_ui._CamposUi__text_turno)
    @patch('pygame_gui.elements.UIDropDownMenu')
    @patch('pygame_gui.elements.UIButton')
    def test_elementos_no_duplicados(self, mock_button, mock_dropdown):
        
        
        self.campos_ui._CamposUi__crear_elementos()
        self.campos_ui._CamposUi__crear_elementos()
        self.assertEqual(mock_dropdown.call_count, 2)
        
        self.assertEqual(mock_button.call_count, 1)
        
        self.assertIsNotNone(self.campos_ui.select_triangulo)
        self.assertIsNotNone(self.campos_ui.select_dado)
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
        casos_dados = [[1, 2],[6, 6, 6, 6],[1],[]]
        
        for dados in casos_dados:
            with self.subTest(dados=dados):
                self.campos_ui.dados_actuales = dados
                self.assertEqual(self.campos_ui.dados_actuales, dados)

    def test_boton_mover_despues_crear_elementos(self):
        with patch('pygame.font.Font') as mock_font, \
         patch('pygame_gui.elements.UIDropDownMenu') as mock_dropdown, \
         patch('pygame_gui.elements.UIButton') as mock_button:
            
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

if __name__ == '__main__':
    unittest.main()