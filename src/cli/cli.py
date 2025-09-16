from src.core.models.jugador.Jugador import Jugador
from src.core.enums.TipoFicha import TipoFicha
from src.core.models.backgammon.backgammon import Backgammon
from src.core.models.tablero.Tablero import Tablero
from src.core.exceptions.SeleccionDadoInvalida import SeleccionDadoInvalida
from src.core.exceptions.SeleccionTrianguloInvalida import SeleccionTrianguloInvalida

ERROR= "\033[91m"
RESET ="\033[0m"
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

    def inicializar_juego(self):
        """Inicializa el juego pidiendo los nombres y mostrando el tablero inicial"""
        print("Bienvenido al backgammon!!")
        nombre_jugador_rojo = input("Ingrese su nombre jugador rojo:")
        nombre_jugador_negro = input("Ingrese su nombre jugador negro:")
        jugador1 = Jugador(nombre_jugador_rojo)
        jugador2 = Jugador(nombre_jugador_negro)
        
        self.__jugador_rojo = jugador1
        self.__jugador_negro = jugador2
        self.backgammon.quien_empieza()
    def mostrar_turno_actual(self):
        """Muestra el turno del jugador actual"""
        if self.backgammon.turno == TipoFicha.ROJA.value:
            print('Turno del jugador rojo: {}'.format(self.jugador_rojo))
        else:
            print('Turno del jugador negro: {}'.format(self.jugador_negro))

    def realizar_movimiento(self):
        """Procesa el movimiento del jugador"""
        print('Dados disponibles: {}'.format(self.dados_disponibles))
        dados_range = range(len(self.dados_disponibles))
        seleccion_index = input(f'Selecciona el dado usando {list(dados_range)}')
        if self.seleccion_dado_valida(seleccion_index):
            seleccion = self.dados_disponibles[int(seleccion_index)]
            if self.backgammon.hay_fichas_comidas():
                self.backgammon.mover_ficha_comida(seleccion)
                self.dados_disponibles.pop(int(seleccion_index))
            else:
                triangulo_origen = input('Selecciona el triángulo de origen (0-23): ')
                if self.seleccion_triangulo_valida(triangulo_origen):
                    self.backgammon.mover_ficha(int(triangulo_origen), seleccion)
                    self.dados_disponibles.pop(int(seleccion_index))
            self.backgammon.tablero.imprimir_tablero()
    def seleccion_dado_valida(self,seleccion:str)-> bool: 
        '''Valida que la selección del dado sea correcta
        Parámetros:
            seleccion (str): La selección del dado como string
        Retorna:
            bool: True si la selección es válida
        Raises:
            SeleccionDadoInvalida
        '''
        if seleccion in [str(i) for i in range(len(self.dados_disponibles))]:
            return True
        raise SeleccionDadoInvalida("Selección de dado inválida")
    def seleccion_triangulo_valida(self, seleccion:str) -> bool:
        '''Valida que la selección del triángulo sea correcta
        Parámetros:
            seleccion (str): La selección del triángulo como string
        Retorna:
            bool: True si la selección es válida
        Raises:
            SeleccionTrianguloInvalida
        '''
        if seleccion in [str(i) for i in range(24)]:
            return True
        raise SeleccionTrianguloInvalida("Selección de triángulo inválida")
    def jugar(self):
        """Método principal que controla el flujo del juego"""
        self.inicializar_juego()
        self.backgammon.tablero.imprimir_tablero()
        while self.backgammon.hay_ganador() is None:
            self.__dados_disponibles = []
            self.mostrar_turno_actual()
            self.tirar_dados()
            while self.dados_disponibles:
                try:
                    self.realizar_movimiento()
                except Exception as e:
                    print(f"{ERROR}{e}{RESET}")
            self.backgammon.cambiar_turno()
        print('¡El jugador {} ha ganado!'.format(self.backgammon.hay_ganador()))

if __name__ == "__main__":
    cli = CLI(None, None)
    cli.jugar()