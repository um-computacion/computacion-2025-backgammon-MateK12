from src.core.interfaces.EstrategiasPuedeMover import IEstrategiaPuedeMover
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
# pylint: disable=C0303

class EstrategiaMovimientoComida(IEstrategiaPuedeMover):
    """Valida movimiento cuando hay fichas comidas"""

    def puede_mover(self, tipo: int, dados: list[int], tablero, backgammon) -> bool:
        '''Verifica si puede mover una ficha comida
        Parametros:
            tipo (int): Tipo de ficha
            dados (list[int]): Valores de los dados
            tablero: El tablero de juego
            backgammon: El juego de backgammon
        Retorna:
            bool: True si puede mover, False en caso contrario'''
        if not self._hay_fichas_comidas(tipo, tablero):
            return False
        
        for movimiento in dados:
            if self._es_movimiento_valido(tipo, movimiento, tablero):
                return True
        return False
    
    def _hay_fichas_comidas(self, tipo: int, tablero) -> bool:
        '''Verifica si hay fichas comidas del tipo dado
        Parametros:
            tipo (int): Tipo de ficha
            tablero: El tablero de juego
        Retorna:
            bool: True si hay fichas comidas, False en caso contrario'''
        return bool([f for f in tablero.fichas_comidas if f.tipo == tipo])
    
    def _es_movimiento_valido(self, tipo: int, movimiento: int, tablero) -> bool:
        '''Verifica si el movimiento desde la barra es válido
        Parametros:
            tipo (int): Tipo de ficha
            movimiento (int): Valor del dado para el movimiento
            tablero: El tablero de juego
        Retorna:
            bool: True si el movimiento es válido, False en caso contrario'''
        triangulo_origen = -1 if tipo == TipoFicha.NEGRA.value else 24
        triangulo_destino = (
            triangulo_origen + movimiento
            if tipo == TipoFicha.NEGRA.value
            else triangulo_origen - movimiento
        )
        no_hay_rivales = not tablero.validador.triangulo_con_fichas_rivales(
            tablero.tablero, triangulo_destino, Ficha(tipo)
        )
        return no_hay_rivales