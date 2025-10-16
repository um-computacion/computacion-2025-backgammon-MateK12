from src.core.models.jugador.Jugador import Jugador
from src.core.enums.TipoFicha import TipoFicha
from src.core.models.backgammon.backgammon import Backgammon
from src.core.models.tablero.Tablero import Tablero
from src.core.exceptions.SeleccionDadoInvalida import SeleccionDadoInvalida
from src.core.exceptions.SeleccionTrianguloInvalida import SeleccionTrianguloInvalida
from src.core.exceptions.CasillaOcupadaException import CasillaOcupadaException
from src.core.exceptions.NoHayFichaEnTriangulo import NoHayFichaEnTriangulo
from src.core.exceptions.MovimientoNoJustoParaGanar import MovimientoNoJustoParaGanar
from src.core.exceptions.NingunMovimientoPosible import NingunMovimientoPosible
from src.core.models.backgammon.Backgammon_Turnos import Backgammon_Turnos
from src.core.helpers.Tablero_Impresor import Tablero_Impresor
from src.core.helpers.Tablero_Inicializador import Tablero_inicializador
from src.core.models.dado.Dados import Dados
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
from src.core.interfaces.JuegoInterfazMovimientos import IJuegoInterfazMovimientos
from src.core.interfaces.JuegoInterfazDados import IJuegoInterfazDados
from src.core.interfaces.DadosValidaciones import IDadosValidaciones
from src.core.interfaces.TrianguloValidaciones import ITrianguloValidaciones
ERROR = "\033[91m"
RESET = "\033[0m"


class CLI(IJuegoInterfazMovimientos,IJuegoInterfazDados,IDadosValidaciones,ITrianguloValidaciones):
    def __init__(self, jugador1, jugador2,backgammon:Backgammon):
        self.__jugador_rojo: Jugador = jugador1
        self.__jugador_negro: Jugador = jugador2
        self.__backgammon: Backgammon = backgammon
        self.__dados_disponibles: list[int] = []

    @property
    def jugador_rojo(self):
        """Retorna el jugador rojo"""
        return self.__jugador_rojo

    @property
    def jugador_negro(self):
        """Retorna el jugador negro"""
        return self.__jugador_negro

    @property
    def backgammon(self):
        """Retorna el objeto Backgammon (gestor del juego)"""
        return self.__backgammon

    @property
    def dados_disponibles(self):
        """Retorna los dados disponibles"""
        return self.__dados_disponibles

    @dados_disponibles.setter
    def dados_disponibles(self, dados):
        """Establece los dados disponibles"""
        self.__dados_disponibles = dados

    def tirar_dados(self):
        """
        Llama al método tirar_dados y actualiza los dados disponibles
        """
        resultado = self.__backgammon.dados.tirar_dados()
        self.__dados_disponibles = resultado
        print(f"Dados tirados: {resultado}")
        if self.backgammon.dados.doble:
            print("¡Doble!")
        return resultado

    def mover_ficha(self, triangulo_origen, movimiento):
        """Parámetros:
            triangulo_origen (int): El triángulo de origen
            movimiento (int): El movimiento a realizar
        Llama al método mover_ficha del Backgammon"""
        self.seleccion_dado_valida(movimiento)
        self.se
        self.__backgammon.mover_ficha(
            triangulo_origen, movimiento, self.__backgammon.turnero.turno
        )

    def inicializar_juego(self):
        """Inicializa el juego pidiendo los nombres y mostrando el tablero inicial"""
        print("Bienvenido al backgammon!!")
        nombre_jugador_rojo = input("Ingrese su nombre jugador rojo:")
        nombre_jugador_negro = input("Ingrese su nombre jugador negro:")
        jugador1 = Jugador(nombre_jugador_rojo)
        jugador2 = Jugador(nombre_jugador_negro)

        self.__jugador_rojo = jugador1
        self.__jugador_negro = jugador2
        self.backgammon.turnero.quien_empieza()

    def mostrar_turno_actual(self):
        """Muestra el turno del jugador actual"""
        if self.backgammon.turnero.turno == TipoFicha.ROJA.value:
            print("Turno del jugador rojo: {}".format(self.jugador_rojo))
        else:
            print("Turno del jugador negro: {}".format(self.jugador_negro))

    def realizar_movimiento(self):
        """Procesa el movimiento del jugador"""
        print("Dados disponibles: {}".format(self.dados_disponibles))
        dados_range = range(len(self.dados_disponibles))
        seleccion_index = input(f"Selecciona el dado usando {list(dados_range)}")
        if self.seleccion_dado_valida(seleccion_index):
            seleccion = self.dados_disponibles[int(seleccion_index)]
            if self.backgammon.hay_fichas_comidas():
                self.backgammon.mover_ficha_comida(seleccion)
                self.dados_disponibles.pop(int(seleccion_index))
            else:
                triangulo_origen = input("Selecciona el triángulo de origen (0-23): ")
                if self.seleccion_triangulo_valida(triangulo_origen):
                    self.backgammon.mover_ficha(int(triangulo_origen), seleccion)
                    self.dados_disponibles.pop(int(seleccion_index))
            Tablero_Impresor.imprimir_tablero(self.backgammon.tablero)

    def seleccion_dado_valida(self, seleccion: str) -> bool:
        """Valida que la selección del dado sea correcta
        Parámetros:
            seleccion (str): La selección del dado como string
        Retorna:
            bool: True si la selección es válida
        Raises:
            SeleccionDadoInvalida
        """
        if seleccion in [str(i) for i in range(len(self.dados_disponibles))]:
            return True
        raise SeleccionDadoInvalida("Selección de dado inválida")

    def puede_hacer_algun_movimiento(self):
        """Verifica si el jugador actual puede hacer algún movimiento con los dados disponibles
        Raises:
            bool: True si puede hacer algún movimiento, False en caso contrario
        """
        try:
            self.backgammon.puede_mover_ficha(self.backgammon.turnero.turno, self.dados_disponibles)
        except NingunMovimientoPosible:
            self.dados_disponibles = []
    def seleccion_triangulo_valida(self, seleccion: str) -> bool:
        """Valida que la selección del triángulo sea correcta
        Parámetros:
            seleccion (str): La selección del triángulo como string
        Retorna:
            bool: True si la selección es válida
        Raises:
            SeleccionTrianguloInvalida
        """
        if seleccion in [str(i) for i in range(24)]:
            return True
        raise SeleccionTrianguloInvalida("Selección de triángulo inválida")

    def jugar(self):
        """Método principal que controla el flujo del juego"""
        self.inicializar_juego()
        Tablero_Impresor.imprimir_tablero(self.backgammon.tablero)
        while self.backgammon.hay_ganador() is None:
            self.__dados_disponibles = []
            self.mostrar_turno_actual()
            self.tirar_dados()
            while self.dados_disponibles:
                try:
                    self.puede_hacer_algun_movimiento()
                    self.realizar_movimiento()
                except (SeleccionDadoInvalida, SeleccionTrianguloInvalida, NingunMovimientoPosible,CasillaOcupadaException,NoHayFichaEnTriangulo,MovimientoNoJustoParaGanar) as e:
                    print(f"{ERROR}{e}{RESET}")
            self.backgammon.turnero.cambiar_turno()
        self.mostrar_ganador()
    def mostrar_ganador(self):
        """Muestra el ganador del juego"""
        ganador = self.backgammon.hay_ganador()
        if ganador == TipoFicha.ROJA:
            print("¡El jugador rojo ha ganado!")
        elif ganador == TipoFicha.NEGRA:
            print("¡El jugador negro ha ganado!")

if __name__ == "__main__":
    tablero = Tablero(Tablero_inicializador.inicializar_tablero(),Tablero_Validador())
    dados = Dados()
    turnero = Backgammon_Turnos(dados)
    backgammon = Backgammon(tablero,dados,turnero)


    cli = CLI(None, None, backgammon)
    cli.jugar()
