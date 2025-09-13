import unittest
from src.core.models.tablero.Tablero import Tablero
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.CasillaOcupadaException import CasillaOcupadaException
from io import StringIO
from unittest.mock import patch

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero_vacio = [[] for _ in range(24)]
        self.tablero = Tablero(self.tablero_vacio)

    def test_mover_ficha_a_espacio_vacio(self): #mover_ficha()
        ficha = Ficha(TipoFicha.NEGRA.value)
        self.tablero.__tablero__[0].append(ficha)
        
        self.tablero.mover_ficha(ficha, 0, 1)
        
        self.assertEqual(len(self.tablero.__tablero__[0]), 0)
        self.assertEqual(len(self.tablero.__tablero__[1]), 1)
        self.assertEqual(self.tablero.__tablero__[1][0], ficha)

    def test_mover_ficha_a_espacio_con_ficha_mismo_color(self):
        ficha1 = Ficha(TipoFicha.NEGRA.value)
        ficha2 = Ficha(TipoFicha.NEGRA.value)
        self.tablero.__tablero__[0].append(ficha1)
        self.tablero.__tablero__[1].append(ficha2)
        
        self.tablero.mover_ficha(ficha1, 0, 1)
        
        self.assertEqual(len(self.tablero.__tablero__[0]), 0)
        self.assertEqual(len(self.tablero.__tablero__[1]), 2)

    def test_mover_ficha_a_espacio_con_fichas_rivales(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja1 = Ficha(TipoFicha.ROJA.value)
        ficha_roja2 = Ficha(TipoFicha.ROJA.value)
        
        self.tablero.__tablero__[0].append(ficha_negra)
        self.tablero.__tablero__[1].append(ficha_roja1)
        self.tablero.__tablero__[1].append(ficha_roja2)
        
        with self.assertRaises(CasillaOcupadaException):
            self.tablero.mover_ficha(ficha_negra, 0, 1)
    def test_mover_ficha_a_espacio_con_una_ficha_rival(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        
        self.tablero.__tablero__[0].append(ficha_negra)
        self.tablero.__tablero__[1].append(ficha_roja)
        
        self.tablero.mover_ficha(ficha_negra, 0, 1)
        
        self.assertEqual(len(self.tablero.__tablero__[0]), 0)
        self.assertEqual(len(self.tablero.__tablero__[1]), 1)
        self.assertEqual(self.tablero.__tablero__[1][0], ficha_negra)
        self.assertEqual(len(self.tablero.fichas_comidas), 1) #ficha roja
        self.assertEqual(self.tablero.fichas_comidas[0], ficha_roja)
        self.assertTrue(self.tablero.fichas_comidas[0].comida)

    def test_get_tablero(self):
        self.assertEqual(self.tablero.tablero,self.tablero.__tablero__)



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
        self.assertIn("●", output)

        # Verificar estructura básica
        self.assertIn("10", output)
        self.assertIn("[ ]", output)
        # self.assertIn("Fichas:", output)
        
        # Verificar que se muestran las fichas (representadas como ●)

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

    # @patch('sys.stdout', new_callable=StringIO)
    # def test_imprimir_tablero_formato_correcto(self, mock_stdout):
    #     """Test que el formato del tablero sea correcto"""
    #     self.tablero.imprimir_tablero()
    #     output = mock_stdout.getvalue()
        
    #     # Verificar separadores
    #     self.assertIn("=" * 10, output)
    #     self.assertIn("-" * 10, output)
        
    #     # Verificar que aparece el separador visual entre mitades
    #     self.assertIn("│", output)
        
    #     # Verificar que hay al menos 4 líneas principales (2 de puntos, 2 de fichas)
    #     lines = output.strip().split('\n')
    #     puntos_lines = [line for line in lines if 'Puntos:' in line]
    #     fichas_lines = [line for line in lines if 'Fichas:' in line]
        
    #     self.assertEqual(len(puntos_lines), 2)  # Superior e inferior
    #     self.assertEqual(len(fichas_lines), 2)  # Superior e inferior

if __name__ == '__main__':
    unittest.main()