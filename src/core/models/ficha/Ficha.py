from src.core.enums import TipoFicha


class Ficha:
    def __init__(self, tipo: TipoFicha):
        self.__tipo: TipoFicha = tipo

    @property
    def tipo(self):
        """Retorna el tipo de ficha (roja o negra)"""
        return self.__tipo

    def __repr__(self):
        """Retorna la ficha con su color correspondiente"""
        colores = {1: "\033[30m●\033[0m", 2: "\033[31m●\033[0m"}
        return colores.get(self.__tipo, "●")
