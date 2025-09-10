
from src.core.models.jugador.Jugador import Jugador
from src.core.enums.TipoFicha import TipoFicha
from src.core.models.backgammon.backgammon import Backgammon
from src.core.models.tablero.Tablero import Tablero
class CLI():
    def __init__(self,jugador1,jugador2):
        self.__jugador_rojo:Jugador = jugador1
        self.__jugador_negro:Jugador = jugador2
        self.__backgammon:Backgammon = Backgammon()
        self.__dados_disponibles:list[int] = []
    @property
    def jugador_rojo(self):
        return self.__jugador_rojo
    @property
    def jugador_negro(self):
        return self.__jugador_negro
    @property
    def backgammon(self):
        return self.__backgammon
    @property
    def dados_disponibles(self):
        return self.__dados_disponibles
    @dados_disponibles.setter
    def dados_disponibles(self, dados):
        self.__dados_disponibles = dados
    def tirar_dados(self):
        resultado = self.__backgammon.dados.tirar_dados()
        self.__dados_disponibles = resultado
        print(f'Dados tirados: {resultado}')
        if self.backgammon.dados.doble:
            print('¡Doble!')
        return resultado
    def mover_ficha(self,triangulo_origen,movimiento):
        triangulo_origen = movimiento['origen']

        self.__backgammon.mover_ficha(triangulo_origen, movimiento, self.__backgammon.turno)
    
if __name__ == "__main__":
    # try:
        print("Bienvenido al backgammon!!")
        nombre_jugador_rojo:str = input("Ingrese su nombre jugador rojo:")
        nombre_jugador_negro:str = input("Ingrese su nombre jugador negro:")
        jugador1:Jugador = Jugador(nombre_jugador_rojo)
        jugador2:Jugador = Jugador(nombre_jugador_negro)
        cli:CLI = CLI(jugador1, jugador2)
        tablero:Tablero = cli.backgammon.tablero
        tablero.imprimir_tablero()
        print('Empieza el jugador rojo: {}'.format(cli.jugador_rojo))
        while cli.backgammon.hay_ganador() is None:
            cli.__dados_disponibles = []
            tablero.imprimir_tablero()
            if cli.backgammon.turno == TipoFicha.ROJA:
                print('Turno del jugador rojo: {}'.format(cli.jugador_rojo))
            else:
                print('Turno del jugador negro: {}'.format(cli.jugador_negro))
            cli.tirar_dados()
            print('Selecciona movimiento')#TO DO validar que elija un movimiento correcto
            print(cli.dados_disponibles)
            print('0  1  2  3')
            seleccion_index = input('Selecciona el dado usando (0-3): ')
            seleccion = cli.dados_disponibles.pop(int(seleccion_index))
            if 0 <= int(seleccion_index):
                dado_seleccionado = cli.dados_disponibles[int(seleccion_index)]
                triangulo_origen = int(input('Selecciona el triángulo de origen (1-24): '))# to do validar que elija el numero correcto
                cli.backgammon.mover_ficha(triangulo_origen,seleccion)
            else:
                print('Selección inválida. Intente de nuevo.')

        print('¡El jugador {} ha ganado!'.format(cli.backgammon.hay_ganador()))
    # except Exception as e:
    #     print(e)