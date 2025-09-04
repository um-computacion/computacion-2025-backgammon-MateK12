from src.core.enums import TipoFicha
class Ficha():
    def __init__(self,tipo:TipoFicha):
        self.__tipo__:TipoFicha = tipo
        self.__comida__:bool = False

    @property
    def tipo(self):
        return self.__tipo__
    @property
    def comida(self):
        return self.__comida__
    @comida.setter
    def comida(self, valor:bool):    
        self.__comida__ = valor

    def __repr__(self):
        colores = {1: '\033[30m●\033[0m', 2: '\033[31m●\033[0m'}
        return colores.get(self.__tipo__, '●')

