from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.models.dado.Dados import Dados
class Backgammon_Turnos:
    def __init__(self,dados:Dados):
        self.__turno: int
        self.__dados= dados

    @property
    def turno(self) -> int:
        """Retorna el turno actual"""
        return self.__turno
    @turno.setter
    def turno(self, value: int) -> None:
        self.__turno = value

    def cambiar_turno(self):
        """Cambia el turno dependiendo del turno actual"""
        self.__turno = (
            TipoFicha.NEGRA.value
            if self.__turno == TipoFicha.ROJA.value
            else TipoFicha.ROJA.value
        )

    def quien_empieza(self):
        """Determina quien empieza el juego tirando los dados
        Retorna:
            int: TipoFicha del jugador que empieza"""
        hay_Ganador = False
        while not hay_Ganador:
            dados = self.__tirar_dados()
            if dados[0] > dados[1]:
                self.__turno = TipoFicha.ROJA.value
                hay_Ganador = True
            elif dados[0] < dados[1]:
                self.__turno = TipoFicha.NEGRA.value
                hay_Ganador = True

    def __tirar_dados(self):
        """Tira los dados y retorna el resultado
        Retorna:
            list[int]: Resultado de los dados"""
        dados = self.__dados.tirar_dados()
        return dados
