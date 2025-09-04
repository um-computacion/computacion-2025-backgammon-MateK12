class Jugador:
    def __init__(self, nombre:str):
        self.__nombre__:str = nombre

    '''
    Retorna el nombre del jugador cuando se llame a la función print() sobre el objeto Jugador
    '''
    def __repr__(self):
        return self.__nombre__