class Jugador:
    def __init__(self, nombre: str):
        self.__nombre__: str = nombre

    def __repr__(self):
        """
        Retorna el nombre del jugador cuando se llame a la función print() sobre el objeto Jugador
        w"""
        return self.__nombre__
