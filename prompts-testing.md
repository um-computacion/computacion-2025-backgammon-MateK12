



### modelo
### propmt 
### respuesta    
import unittest
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha

class TestFicha(unittest.TestCase):
    
    def test_repr_ficha_negra(self):
        ficha = Ficha(TipoFicha.NEGRA.value)
        self.assertEqual(repr(ficha), '\033[30m●\033[0m')
        
    def test_repr_ficha_roja(self):
        ficha = Ficha(TipoFicha.ROJA.value)
        self.assertEqual(repr(ficha), '\033[31m●\033[0m')
        
    def test_repr_ficha_invalida(self):
        ficha = Ficha(3)  # Valor inválido
        self.assertEqual(repr(ficha), '●')

if __name__ == '__main__':
    unittest.main()
### cambios
le quite el ultimo tests, ya que el tipado no permite el valor 3 para tipo, solo 1 y 2
### archivos finales
Test_Ficha.py

### modelo
Claude
### propmt 
crea los unit test de esta clase, pon enfasis en el metodo get_punto_position_base ya que defnira como se vera mis trianguos del tablero 
### respuesta    
import unittest
import pygame
from src.pygame_ui.ui import TableroUI, BOARD_WIDTH, BOARD_HEIGHT, BOARD_X, BOARD_Y

class TestTableroUI(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.tablero = TableroUI()
        self.punto_width = (BOARD_WIDTH - 100) // 12
        
    def test_get_punto_position_superior_derecha(self):
        expected_x = BOARD_X + BOARD_WIDTH - self.punto_width
        expected_y = BOARD_Y
        x, y = self.tablero.get_punto_position_base(0)
        self.assertEqual((x, y), (expected_x, expected_y))
        
    def test_get_punto_position_superior_izquierda(self):
        expected_x = BOARD_X + BOARD_WIDTH - (6 * self.punto_width) - 150
        expected_y = BOARD_Y
        x, y = self.tablero.get_punto_position_base(6)
        self.assertEqual((x, y), (expected_x, expected_y))
        
    def test_get_punto_position_inferior_derecha(self):
        punto_index = 12
        expected_x = BOARD_X + (punto_index - 12 + 1) * self.punto_width + BOARD_WIDTH/2
        expected_y = BOARD_Y + BOARD_HEIGHT - 250
        x, y = self.tablero.get_punto_position_base(punto_index)
        self.assertEqual((x, y), (expected_x, expected_y))
        
    def test_get_punto_position_inferior_izquierda(self):
        punto_index = 18
        expected_x = BOARD_X + (punto_index - 18) * self.punto_width
        expected_y = BOARD_Y + BOARD_HEIGHT - 250
        x, y = self.tablero.get_punto_position_base(punto_index)
        self.assertEqual((x, y), (expected_x, expected_y))
        
    def test_todos_puntos_en_rango(self):
        for i in range(24):
            x, y = self.tablero.get_punto_position_base(i)
            self.assertTrue(BOARD_X <= x <= BOARD_X + BOARD_WIDTH)
            self.assertTrue(BOARD_Y <= y <= BOARD_Y + BOARD_HEIGHT)
            
    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
### Fixed
### cambios
quite el ultimo test, ya que no lo considero importante, ya que si esta generando correctamente 
la posicion de los triangulos en los otros cuadrantes, los esta generando dentro del tablero 
en el primer test agrege la variable punto_index para permitir calcular cualquier triangulo del primer cuadrante
### archivos finales
Test_ui





### modelo
### propmt 
### respuesta    
import unittest
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha

class TestTableroValidador(unittest.TestCase):
    def setUp(self):
        self.validador = Tablero_Validador()
        self.tablero = [[] for _ in range(24)]

    def test_triangulo_con_dos_fichas_rivales(self):
        """Test que verifica que detecta correctamente dos fichas rivales"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja1 = Ficha(TipoFicha.ROJA.value)
        ficha_roja2 = Ficha(TipoFicha.ROJA.value)
        
        # Colocar dos fichas rojas en el triángulo 0
        self.tablero[0] = [ficha_roja1, ficha_roja2]
        
        # Verificar con una ficha negra
        self.assertTrue(
            self.validador.triangulo_con_fichas_rivales(
                self.tablero, 
                0, 
                ficha_negra
            )
        )

    def test_triangulo_con_una_ficha_rival(self):
        """Test que verifica que una sola ficha rival no bloquea"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        
        # Colocar una ficha roja en el triángulo 0
        self.tablero[0] = [ficha_roja]
        
        # Verificar con una ficha negra
        self.assertFalse(
            self.validador.triangulo_con_fichas_rivales(
                self.tablero, 
                0, 
                ficha_negra
            )
        )

    def test_triangulo_vacio(self):
        """Test que verifica que un triángulo vacío no bloquea"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        
        self.assertFalse(
            self.validador.triangulo_con_fichas_rivales(
                self.tablero, 
                0, 
                ficha_negra
            )
        )

    def test_triangulo_con_fichas_mismo_color(self):
        """Test que verifica que las fichas del mismo color no bloquean"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_negra1 = Ficha(TipoFicha.NEGRA.value)
        ficha_negra2 = Ficha(TipoFicha.NEGRA.value)
        
        # Colocar dos fichas negras en el triángulo 0
        self.tablero[0] = [ficha_negra1, ficha_negra2]
        
        # Verificar con una ficha negra
        self.assertFalse(
            self.validador.triangulo_con_fichas_rivales(
                self.tablero, 
                0, 
                ficha_negra
            )
        )

if __name__ == '__main__':
    unittest.main()

### Fixed
### cambios
Agrege test test_triangulo_mas_dos_fichas_rivales 
No hice muchos cambios ya que los tests cubren los casos mas criticos de la clase
- devuelva true cuando se mueve una ficha a un triangulo con 2 o mas fichas rivales
- devuelva false cuando solo hay una ficha rival en el triangulo a mover
- devuelva false cuando el triangulo esta vacio o cuando el triangulo tiene fichas del mismo color
### archivos finales





### modelo
### propmt 
### respuesta    
def test_inicializar_tablero(self):
    """Test que verifica la disposición inicial correcta del tablero de backgammon"""
    game = Backgammon()
    tablero = game.inicializar_tablero()
    
    # Verificar que el tablero tiene 24 posiciones
    self.assertEqual(len(tablero), 24)
    
    # Verificar fichas negras
    self.assertEqual(len(tablero[0]), 2)
    self.assertEqual(len(tablero[11]), 5)
    self.assertEqual(len(tablero[16]), 3)
    self.assertEqual(len(tablero[18]), 5)
    
    # Verificar que son del tipo correcto
    self.assertEqual(tablero[0][0].tipo, TipoFicha.NEGRA.value)
    self.assertEqual(tablero[11][0].tipo, TipoFicha.NEGRA.value)
    self.assertEqual(tablero[16][0].tipo, TipoFicha.NEGRA.value)
    self.assertEqual(tablero[18][0].tipo, TipoFicha.NEGRA.value)
    
    # Verificar fichas rojas
    self.assertEqual(len(tablero[23]), 2)
    self.assertEqual(len(tablero[12]), 5)
    self.assertEqual(len(tablero[7]), 3)
    self.assertEqual(len(tablero[5]), 5)
    
    # Verificar que son del tipo correcto
    self.assertEqual(tablero[23][0].tipo, TipoFicha.ROJA.value)
    self.assertEqual(tablero[12][0].tipo, TipoFicha.ROJA.value)
    self.assertEqual(tablero[7][0].tipo, TipoFicha.ROJA.value)
    self.assertEqual(tablero[5][0].tipo, TipoFicha.ROJA.value)
    

### Fixed
### cambios
le agregue 2 asserts mas para validar la longitud del arreglo y los espacios vacios
### archivos finales
Test_backgammon.py







### modelo
### propmt 
### respuesta    
def test_hay_fichas_comidas_sin_fichas(self):
        """Test cuando no hay fichas comidas"""
        self.game._Backgammon__tablero__.fichas_comidas = []
        resultado = self.game.hay_fichas_comidas(TipoFicha.NEGRA)
        self.assertFalse(resultado)

    def test_hay_fichas_comidas_con_fichas(self):
        """Test cuando hay fichas comidas del tipo especificado"""
        ficha_comida = Ficha(TipoFicha.NEGRA.value)
        self.game._Backgammon__tablero__.fichas_comidas = [ficha_comida]
        resultado = self.game.hay_fichas_comidas(TipoFicha.NEGRA)
        self.assertTrue(resultado)

    def test_seleccionar_ficha_existente(self):
        """Test seleccionar una ficha que existe en el triángulo"""
        ficha = Ficha(TipoFicha.NEGRA.value)
        self.game._Backgammon__tablero__.tablero = [[ficha]]
        resultado = self.game.seleccionar_ficha(0, TipoFicha.NEGRA)
        self.assertEqual(resultado, ficha)

    def test_seleccionar_ficha_no_existente(self):
        """Test seleccionar una ficha que no existe en el triángulo"""
        self.game._Backgammon__tablero__.tablero = [[]]
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.seleccionar_ficha(0, TipoFicha.NEGRA)

    def test_seleccionar_ficha_color_incorrecto(self):
        """Test seleccionar una ficha cuando solo hay fichas de otro color"""
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.game._Backgammon__tablero__.tablero = [[ficha_roja]]
        with self.assertRaises(NoHayFichaEnTriangulo):
            self.game.seleccionar_ficha(0, TipoFicha.NEGRA)

### Fixed
### cambios TO DO CAMBIAR POR METODO INICIALIZAR_TABLERO()
### archivos finales


### modelo
### propmt 
### respuesta    
import unittest
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha

class TestFicha(unittest.TestCase):
    
    def test_repr_ficha_negra(self):
        ficha = Ficha(TipoFicha.NEGRA.value)
        self.assertEqual(repr(ficha), '\033[30m●\033[0m')


### modelo
### propmt 
### respuesta    
import unittest
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha

class TestTableroValidador(unittest.TestCase):
    def setUp(self):
        self.validador = Tablero_Validador()


### modelo
### propmt 
### respuesta    
def test_inicializar_tablero(self):
    """Test que verifica la disposición inicial correcta del tablero de backgammon"""
    game = Backgammon()
    tablero = game.inicializar_tablero()
    
    # Verificar que el tablero tiene 24 posiciones
    self.assertEqual(len(tablero), 24)


### modelo
claude
### propmt 
necesito que agreges a los tests de tablero,  los test de imprimit tablero
### respuesta    
def test_hay_fichas_comidas_sin_fichas(self):
        """Test cuando no hay fichas comidas"""
        self.game._Backgammon__tablero__.fichas_comidas = []
        resultado = self.game.hay_fichas_comidas(TipoFicha.NEGRA)
        self.assertFalse(resultado)

    def test_hay_fichas_comidas_con_fichas(self):
        """Test cuando hay fichas comidas del tipo especificado"""


### modelo
claude
### propmt 
necesito que agreges a los tests de tablero,  los test de imprimit tablero
### respuesta    
import unittest
from unittest.mock import patch
from io import StringIO
from src.core.models.tablero.Tablero import Tablero
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.CasillaOcupadaException import CasillaOcupadaException

class TestTablero(unittest.TestCase):
    # ...existing code...

    @patch('sys.stdout', new_callable=StringIO)
    def test_imprimir_tablero_vacio(self, mock_stdout):
        """Test imprimir tablero vacío"""
        self.tablero.imprimir_tablero()
        output = mock_stdout.getvalue()
        
        # Verificar que contiene elementos básicos del tablero
        self.assertIn("Puntos:", output)
        self.assertIn("Fichas:", output)
        self.assertIn("=", output)  # Líneas de separación
        
        # Verificar que contiene números de puntos
        for i in range(1, 25):
            self.assertIn(str(i), output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_imprimir_tablero_con_fichas(self, mock_stdout):
        """Test imprimir tablero con algunas fichas"""
        # Agregar fichas en posiciones específicas
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        
        self.tablero.__tablero__[0].append(ficha_negra)
        self.tablero.__tablero__[0].append(ficha_negra)
        self.tablero.__tablero__[23].append(ficha_roja)
        
        self.tablero.imprimir_tablero()
        output = mock_stdout.getvalue()
        
        # Verificar estructura básica
        self.assertIn("Puntos:", output)
        self.assertIn("Fichas:", output)
        
        # Verificar que se muestran las fichas (representadas como ●)
        self.assertIn("●", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_imprimir_tablero_con_fichas_comidas(self, mock_stdout):
        """Test imprimir tablero con fichas comidas"""
        ficha_comida = Ficha(TipoFicha.ROJA.value)
        ficha_comida.comida = True
        self.tablero.__fichas_comidas__.append(ficha_comida)
        
        self.tablero.imprimir_tablero()
        output = mock_stdout.getvalue()
        
        self.assertIn("Fichas comidas:", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_imprimir_tablero_con_fichas_ganadas(self, mock_stdout):
        """Test imprimir tablero con fichas ganadas"""
        ficha_ganada = Ficha(TipoFicha.NEGRA.value)
        self.tablero.__fichas_ganadas__.append(ficha_ganada)
        
        self.tablero.imprimir_tablero()
        output = mock_stdout.getvalue()
        
        self.assertIn("Fichas ganadas:", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_imprimir_tablero_formato_correcto(self, mock_stdout):
        """Test que el formato del tablero sea correcto"""
        self.tablero.imprimir_tablero()
        output = mock_stdout.getvalue()
        
        # Verificar separadores
        self.assertIn("=" * 100, output)
        self.assertIn("─" * 100, output)
        
        # Verificar que aparece el separador visual entre mitades
        self.assertIn("│", output)
        
        # Verificar que hay al menos 4 líneas principales (2 de puntos, 2 de fichas)
        lines = output.strip().split('\n')
        puntos_lines = [line for line in lines if 'Puntos:' in line]
        fichas_lines = [line for line in lines if 'Fichas:' in line]
        
        self.assertEqual(len(puntos_lines), 2)  # Superior e inferior
        self.assertEqual(len(fichas_lines), 2)  # Superior e inferior

    # ...existing code...

if __name__ == '__main__':
    unittest.main()
### Fixed
### cambios 
cambie para que valide si imprime los arreglos
test_imprimir_tablero_vacio
### archivos finales


### modelo
claude
### propmt 
haz los test de los 2 ultimo meotods de esta clase (clase tablero_validador)
### respuesta    
# Add these tests to your existing Test_Tablero_Validador.py file

    def test_puede_ganar_ficha_roja_triangulo_menos_uno(self): #puede_ganar()
        """Test cuando ficha roja puede ganar (triangulo_destino = -1)"""
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertTrue(self.validador.puede_ganar(ficha_roja, -1))

    def test_puede_ganar_ficha_negra_triangulo_24(self):
        """Test cuando ficha negra puede ganar (triangulo_destino = 24)"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertTrue(self.validador.puede_ganar(ficha_negra, 24))

    def test_no_puede_ganar_ficha_roja_triangulo_24(self):
        """Test cuando ficha roja NO puede ganar (triangulo_destino = 24)"""
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_roja, 24))

    def test_no_puede_ganar_ficha_negra_triangulo_menos_uno(self):
        """Test cuando ficha negra NO puede ganar (triangulo_destino = -1)"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_negra, -1))

    def test_no_puede_ganar_triangulo_intermedio(self):
        """Test cuando ninguna ficha puede ganar en triángulo intermedio"""
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertFalse(self.validador.puede_ganar(ficha_roja, 10))
        self.assertFalse(self.validador.puede_ganar(ficha_negra, 10))

    def test_esta_rango_ganar_ficha_roja_triangulo_0(self): #esta_rango_ganar()
        """Test ficha roja en rango de ganar (triangulo 0)"""
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertTrue(self.validador.esta_rango_ganar(ficha_roja, 0))

    def test_esta_rango_ganar_ficha_roja_triangulo_5(self):
        """Test ficha roja en rango de ganar (triangulo 5)"""
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertTrue(self.validador.esta_rango_ganar(ficha_roja, 5))

    def test_esta_rango_ganar_ficha_negra_triangulo_18(self):
        """Test ficha negra en rango de ganar (triangulo 18)"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertTrue(self.validador.esta_rango_ganar(ficha_negra, 18))

    def test_esta_rango_ganar_ficha_negra_triangulo_23(self):
        """Test ficha negra en rango de ganar (triangulo 23)"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertTrue(self.validador.esta_rango_ganar(ficha_negra, 23))

    def test_no_esta_rango_ganar_ficha_roja_fuera_rango(self):
        """Test ficha roja fuera del rango de ganar"""
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        self.assertFalse(self.validador.esta_rango_ganar(ficha_roja, 6))
        self.assertFalse(self.validador.esta_rango_ganar(ficha_roja, 10))
        self.assertFalse(self.validador.esta_rango_ganar(ficha_roja, 23))

    def test_no_esta_rango_ganar_ficha_negra_fuera_rango(self):
        """Test ficha negra fuera del rango de ganar"""
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        self.assertFalse(self.validador.esta_rango_ganar(ficha_negra, 0))
        self.assertFalse(self.validador.esta_rango_ganar(ficha_negra, 10))
        self.assertFalse(self.validador.esta_rango_ganar(ficha_negra, 17))
### Fixed
### cambios
Elimine los tests de puede_ganar() porque me parecieron que eran bastante complejos para lo que hacia la funcion 
### archivos finales
test_tablero_validador


### modelo
    claude
### propmt
haz un test de la funcion realizar movimiento, intenta cubrir todas las linea, excepto los prints, esos no me interesan, pon enfasis en verificar si las funciones que deberian llamarse se llaman o no
### respuesta  
#region tirar_dados
def test_tirar_dados_sin_dobles(self):
    """Test tirar dados cuando NO salen dobles"""
    with patch.object(self.cli.backgammon.dados, 'tirar_dados', return_value=[3, 5]), \
         patch.object(self.cli.backgammon.dados, 'doble', False), \
         patch('builtins.print'):
        resultado = self.cli.tirar_dados()
        self.assertEqual(resultado, [3, 5])
        self.assertEqual(self.cli.dados_disponibles, [3, 5])

def test_tirar_dados_con_dobles(self):
    """Test tirar dados cuando salen dobles"""
    with patch.object(self.cli.backgammon.dados, 'tirar_dados', return_value=[4, 4, 4, 4]), \
         patch.object(self.cli.backgammon.dados, 'doble', True), \
         patch('builtins.print'):
        resultado = self.cli.tirar_dados()
        self.assertEqual(resultado, [4, 4, 4, 4])
        self.assertEqual(self.cli.dados_disponibles, [4, 4, 4, 4])
#endregion

#region mostrar_turno_actual
def test_mostrar_turno_actual_jugador_rojo(self):
    """Test mostrar turno del jugador rojo"""
    with patch.object(self.cli.backgammon, 'turno', TipoFicha.ROJA.value), \
         patch('builtins.print') as mock_print:
        self.cli.mostrar_turno_actual()
        mock_print.assert_called_once_with('Turno del jugador rojo: Juan')

def test_mostrar_turno_actual_jugador_negro(self):
    """Test mostrar turno del jugador negro"""
    with patch.object(self.cli.backgammon, 'turno', TipoFicha.NEGRA.value), \
         patch('builtins.print') as mock_print:
        self.cli.mostrar_turno_actual()
        mock_print.assert_called_once_with('Turno del jugador negro: Maria')
#endregion

#region realizar_movimiento (TODOS LOS CASOS)
def test_realizar_movimiento_con_fichas_comidas_dado_valido(self):
    """Test realizar movimiento cuando hay fichas comidas y el dado es válido"""
    self.cli.dados_disponibles = [3, 5]
    
    with patch('builtins.input', return_value='0'), \
         patch('builtins.print'), \
         patch.object(self.cli.backgammon, 'hay_fichas_comidas', return_value=True), \
         patch.object(self.cli.backgammon, 'mover_ficha_comida') as mock_mover_comida, \
         patch.object(self.cli, 'seleccion_dado_valida', return_value=True), \
         patch('src.core.models.tablero.Tablero_Impresor.Tablero_Impresor.imprimir_tablero'):
        
        self.cli.realizar_movimiento()
        
        mock_mover_comida.assert_called_once_with(3)
        self.assertEqual(self.cli.dados_disponibles, [5])

def test_realizar_movimiento_sin_fichas_comidas_dado_y_triangulo_validos(self):
    """Test realizar movimiento cuando NO hay fichas comidas, dado y triángulo válidos"""
    self.cli.dados_disponibles = [2, 4]
    
    with patch('builtins.input', side_effect=['1', '5']), \
         patch('builtins.print'), \
         patch.object(self.cli.backgammon, 'hay_fichas_comidas', return_value=False), \
         patch.object(self.cli.backgammon, 'mover_ficha') as mock_mover_ficha, \
         patch.object(self.cli, 'seleccion_dado_valida', return_value=True), \
         patch.object(self.cli, 'seleccion_triangulo_valida', return_value=True), \
         patch('src.core.models.tablero.Tablero_Impresor.Tablero_Impresor.imprimir_tablero'):
        
        self.cli.realizar_movimiento()
        
        mock_mover_ficha.assert_called_once_with(5, 4)
        self.assertEqual(self.cli.dados_disponibles, [2])

def test_realizar_movimiento_dado_invalido(self):
    """Test realizar movimiento con selección de dado inválida"""
    self.cli.dados_disponibles = [1, 3]
    
    with patch('builtins.input', return_value='5'), \
         patch('builtins.print'), \
         patch.object(self.cli, 'seleccion_dado_valida', side_effect=SeleccionDadoInvalida("Dado inválido")):
        
        with patch.object(self.cli.backgammon, 'hay_fichas_comidas') as mock_hay_comidas, \
             patch.object(self.cli.backgammon, 'mover_ficha_comida') as mock_mover_comida, \
             patch.object(self.cli.backgammon, 'mover_ficha') as mock_mover_ficha:
            
            with self.assertRaises(SeleccionDadoInvalida):
                self.cli.realizar_movimiento()
            
            mock_hay_comidas.assert_not_called()
            mock_mover_comida.assert_not_called()
            mock_mover_ficha.assert_not_called()

def test_realizar_movimiento_sin_fichas_comidas_triangulo_invalido(self):
    """Test realizar movimiento sin fichas comidas pero triángulo inválido"""
    self.cli.dados_disponibles = [2, 6]
    
    with patch('builtins.input', side_effect=['0', '25']), \
         patch('builtins.print'), \
         patch.object(self.cli.backgammon, 'hay_fichas_comidas', return_value=False), \
         patch.object(self.cli.backgammon, 'mover_ficha') as mock_mover_ficha, \
         patch.object(self.cli, 'seleccion_dado_valida', return_value=True), \
         patch.object(self.cli, 'seleccion_triangulo_valida', side_effect=SeleccionTrianguloInvalida("Triángulo inválido")):
        
        with self.assertRaises(SeleccionTrianguloInvalida):
            self.cli.realizar_movimiento()
        
        mock_mover_ficha.assert_not_called()
        self.assertEqual(self.cli.dados_disponibles, [2, 6])

def test_realizar_movimiento_multiples_dados_seleccion_segundo(self):
    """Test realizar movimiento seleccionando el segundo dado de múltiples disponibles"""
    self.cli.dados_disponibles = [1, 3, 5, 2]
    
    with patch('builtins.input', side_effect=['2', '10']), \
         patch('builtins.print'), \
         patch.object(self.cli.backgammon, 'hay_fichas_comidas', return_value=False), \
         patch.object(self.cli.backgammon, 'mover_ficha') as mock_mover_ficha, \
         patch.object(self.cli, 'seleccion_dado_valida', return_value=True), \
         patch.object(self.cli, 'seleccion_triangulo_valida', return_value=True), \
         patch('src.core.models.tablero.Tablero_Impresor.Tablero_Impresor.imprimir_tablero'):
        
        self.cli.realizar_movimiento()
        
        mock_mover_ficha.assert_called_once_with(10, 5)
        self.assertEqual(self.cli.dados_disponibles, [1, 3, 2])
#endregion  
### Fixed
### cambios 
le quite los test de los dados porque no los voy a utizar de momento, le quite mockeos inecesarios en los validadores para que los tests sean mas "reales"
### archivos finales
test_cli.py



### modelo
    claude
### propmt
### respuesta    
### Fixed
### cambios 
### archivos finales