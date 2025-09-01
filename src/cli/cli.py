
from src.core.models.jugador import Jugador
from src.core.enums.TipoFicha import TipoFicha
class CLI():
    def __init__(self,jugador1,jugador2):
        self.__jugador_rojo:Jugador = jugador1
        self.__jugador_negro:Jugador = jugador2
    @property
    def jugador_rojo(self):
        return self.__jugador_rojo
    @property
    def jugador_negro(self):
        return self.__jugador_negro

if __name__ == "__main__":
    print("Bienvenido al backgammon!!")
    nombre_jugador_rojo = input("Ingrese su nombre jugador rojo:")
    nombre_jugador_negro = input("Ingrese su nombre jugador negro:")
    jugador1 = CLI.cargar_jugador(nombre_jugador_rojo, TipoFicha.ROJA.value)
    jugador2 = CLI.cargar_jugador(nombre_jugador_negro, TipoFicha.NEGRA.value)
    cli = CLI(jugador1, jugador2)
    cli.run()