import unittest
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha

class TestTableroValidador(unittest.TestCase):
    def setUp(self):
        self.validador = Tablero_Validador()
        self.tablero = [[] for _ in range(24)]

    def test_triangulo_con_dos_fichas_rivales(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja1 = Ficha(TipoFicha.ROJA.value)
        ficha_roja2 = Ficha(TipoFicha.ROJA.value)
        
        self.tablero[0] = [ficha_roja1, ficha_roja2] #poner 2 fichas en triangulo 
        
        self.assertTrue(self.validador.triangulo_con_fichas_rivales(self.tablero, 0, ficha_negra)) #movimiento invalido

    def test_triangulo_mas_dos_fichas_rivales(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja1 = Ficha(TipoFicha.ROJA.value)
        ficha_roja2 = Ficha(TipoFicha.ROJA.value)
        ficha_roja3 = Ficha(TipoFicha.ROJA.value)        
        self.tablero[0] = [ficha_roja1, ficha_roja2,ficha_roja3] #poner 3 fichas en triangulo 
        
        self.assertTrue(self.validador.triangulo_con_fichas_rivales(self.tablero, 0, ficha_negra)) #movimiento invalido

    def test_triangulo_con_una_ficha_rival(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_roja = Ficha(TipoFicha.ROJA.value)
        
        self.tablero[0] = [ficha_roja]
        
        self.assertFalse(self.validador.triangulo_con_fichas_rivales(self.tablero, 0, ficha_negra)) # movimiento valido come ficha

    def test_triangulo_vacio(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        
        self.assertFalse(self.validador.triangulo_con_fichas_rivales(self.tablero, 0, ficha_negra))

    def test_triangulo_con_fichas_mismo_color(self):
        ficha_negra = Ficha(TipoFicha.NEGRA.value)
        ficha_negra1 = Ficha(TipoFicha.NEGRA.value)
        ficha_negra2 = Ficha(TipoFicha.NEGRA.value)
        
        self.tablero[0] = [ficha_negra1, ficha_negra2]
        
        self.assertFalse(self.validador.triangulo_con_fichas_rivales(self.tablero, 0, ficha_negra))

if __name__ == '__main__':
    unittest.main()