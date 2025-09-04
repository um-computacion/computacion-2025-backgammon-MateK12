
from src.core.models.jugador import Jugador
from src.core.enums.TipoFicha import TipoFicha
from src.core.models.backgammon.backgammon import Backgammon
from src.core.models.tablero.Tablero import Tablero
class CLI():
    def __init__(self,jugador1,jugador2):
        self.__jugador_rojo:Jugador = jugador1
        self.__jugador_negro:Jugador = jugador2
        self.__backgammon:Backgammon = Backgammon()
    @property
    def jugador_rojo(self):
        return self.__jugador_rojo
    @property
    def jugador_negro(self):
        return self.__jugador_negro
    @property
    def backgammon(self):
        return self.__backgammon
    def tirar_dados(self):
        resultado = self.__backgammon.dados.tirar_dados()
        print(f'Dados tirados: {resultado['dado1']} y {resultado['dado2']}')
        if self.backgammon.dados.doble:
            print('¡Doble! Tira de nuevo.')
        return resultado

if __name__ == "__main__":
    print("Bienvenido al backgammon!!")
    nombre_jugador_rojo:str = input("Ingrese su nombre jugador rojo:")
    nombre_jugador_negro:str = input("Ingrese su nombre jugador negro:")
    jugador1:Jugador = Jugador(nombre_jugador_rojo, TipoFicha.ROJA.value)
    jugador2:Jugador = Jugador(nombre_jugador_negro, TipoFicha.NEGRA.value)
    cli:CLI = CLI(jugador1, jugador2)
    tablero:Tablero = CLI.backgammon.tablero
    tablero.mostrar_tablero()
    print('Empieza el jugador rojo: {}'.format(cli.jugador_rojo))
    while cli.backgammon.hay_ganador() is False:
        if cli.backgammon.turno == TipoFicha.ROJA:
            print('Turno del jugador rojo: {}'.format(cli.jugador_rojo))
            cli.tirar_dados()
    print('¡El jugador {} ha ganado!'.format(cli.backgammon.hay_ganador()))