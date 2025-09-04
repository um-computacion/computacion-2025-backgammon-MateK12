from src.core.models.dado.Dados import Dados 
from src.core.models.tablero.Tablero import Tablero
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.NoHayFichaEnTriangulo import NoHayFichaEnTriangulo
from src.core.models.ficha.Ficha import Ficha
class Backgammon():
    def __init__(self):
        self.__dados__:Dados = Dados()
        self.__tablero__:Tablero = Tablero(self.inicializar_tablero())
        self.__turno:TipoFicha = TipoFicha.ROJA
    def tirar_dados(self):
        dados = self.__dados__.tirar_dados()
        return {'dado1': dados['dado1'], 'dado2': dados['dado2'],'doble': self.__dados__.doble}
    @property
    def tablero(self):
        return self.__tablero__
    @property
    def dados(self):
        return self.__dados__

    def hay_fichas_comidas(self,tipo:TipoFicha)->bool:
        if [ficha.tipo == tipo for ficha in self.__tablero__.fichas_comidas]:
            return True
        else:
            return False

    def seleccionar_ficha(self,triangulo:int,tipo:TipoFicha)->Ficha | None:
        fichas = self.__tablero__.tablero[triangulo]
        tipos_fichas = [ficha for ficha in fichas if ficha.tipo == tipo]
        if not tipos_fichas:
            raise NoHayFichaEnTriangulo("No tiene una ficha de su color en el triangulo seleccionado")
        else:
            return tipos_fichas[0]
        
    def cambiar_turno(self):
        self.__turno = TipoFicha.NEGRA if self.__turno == TipoFicha.ROJA else TipoFicha.ROJA

    def hay_ganador(self) -> int | None:
        fichas_rojas:list[Ficha] = [ficha for ficha in self.__tablero__.fichas_ganadas if ficha.tipo == TipoFicha.ROJA.value]
        fichas_negras:list[Ficha] = [ficha for ficha in self.__tablero__.fichas_ganadas if ficha.tipo == TipoFicha.NEGRA.value]
        if len(fichas_rojas) == 24:
            return TipoFicha.ROJA.value
        if len(fichas_negras) == 24:
            return TipoFicha.NEGRA.value
        return None

    def inicializar_tablero(self) -> list[list[Ficha | None]]:
        
        tablero_inicial: list[list[Ficha]] = [[] for _ in range(24)]
        tablero_inicial[0] = [Ficha(TipoFicha.NEGRA.value) for _ in range(2)]  
        tablero_inicial[11] = [Ficha(TipoFicha.NEGRA.value) for _ in range(5)] 
        tablero_inicial[16] = [Ficha(TipoFicha.NEGRA.value) for _ in range(3)] 
        tablero_inicial[18] = [Ficha(TipoFicha.NEGRA.value) for _ in range(5)] 

        tablero_inicial[23] = [Ficha(TipoFicha.ROJA.value) for _ in range(2)]  
        tablero_inicial[12] = [Ficha(TipoFicha.ROJA.value) for _ in range(5)]  
        tablero_inicial[7] = [Ficha(TipoFicha.ROJA.value) for _ in range(3)]   
        tablero_inicial[5] = [Ficha(TipoFicha.ROJA.value) for _ in range(5)]   

        return tablero_inicial
