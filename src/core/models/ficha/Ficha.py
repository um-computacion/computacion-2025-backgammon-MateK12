from src.core.enums import TipoFicha
class Ficha():
    def __init__(self,tipo:TipoFicha):
        self.__tipo__:TipoFicha = tipo

    @property
    def tipo(self):
        return self.__tipo__

    def __repr__(self):
        colores = {1: '\033[30m●\033[0m', 2: '\033[31m●\033[0m'}
        return colores.get(self.__tipo__, '●')

