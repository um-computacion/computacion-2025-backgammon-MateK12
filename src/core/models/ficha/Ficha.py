from src.core.enums import TipoFicha
class Ficha():
    def __init__(self,tipo:TipoFicha):
        self.__tipo__:TipoFicha = tipo
        self.__comida__:bool = False
        self.__por_ganar__:bool = False
    @property
    def tipo(self):
        '''Retorna el tipo de ficha (roja o negra)'''
        return self.__tipo__
    @property
    def comida(self):
        '''Retorna si la ficha está comida o no'''
        return self.__comida__
    @comida.setter
    def comida(self, valor:bool):    
        '''Establece si la ficha está comida o no'''
        self.__comida__ = valor

    def __repr__(self):
        '''Retorna la ficha con su color correspondiente'''
        colores = {1: '\033[30m●\033[0m', 2: '\033[31m●\033[0m'}
        return colores.get(self.__tipo__, '●')

