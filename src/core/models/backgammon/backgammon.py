from src.core.models.dado.Dados import Dados 
from src.core.models.tablero.Tablero import Tablero
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.NoHayFichaEnTriangulo import NoHayFichaEnTriangulo
class Backgammon():
    def __init__(self):
        self.__dados__:Dados = Dados()
        self.__tablero__:Tablero = Tablero()
    
    def tirar_dados(self):
        return self.__dados__.tirar_dados()
    
    def mover_ficha(self):
        self.__tablero__.mover_ficha()
    def seleccionar_ficha(self,triangulo:int,tipo:TipoFicha):
        ficha = self.__tablero__.tab
