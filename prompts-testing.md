### modelo
Claude
### propmt 
teniendo en cuenta el enum de tipo ficha, haz un test para verificar el metodo repr
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
