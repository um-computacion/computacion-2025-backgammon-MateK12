from src.core.interfaces.EstrategiasPuedeMover import IEstrategiaPuedeMover
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha

# pylint: disable=C0303

class EstrategiaMovimientoNormal(IEstrategiaPuedeMover):
    """Valida movimiento normal de fichas en el tablero"""
    
    def puede_mover(self, tipo: int, dados: list[int], tablero, backgammon) -> bool:
        '''Verifica si puede mover una ficha normalmente
        Parametros:
            tipo (int): Tipo de ficha
            dados (list[int]): Valores de los dados
            tablero: El tablero de juego
            backgammon: El juego de backgammon
            Retorna:
            bool: True si puede mover, False en caso contrario'''
        if backgammon.hay_fichas_comidas():
            return False
        for movimiento in dados:
            if self._existe_movimiento_valido(tipo, movimiento, tablero):
                return True
        return False
    
    
    def _existe_movimiento_valido(self, tipo: int, movimiento: int, tablero) -> bool:
        '''Verifica si existe un movimiento válido desde algún triángulo
        Parametros:
            tipo (int): Tipo de ficha
            movimiento (int): Valor del dado para el movimiento
            tablero: El tablero de juego
            Retorna:
            bool: True si existe un movimiento válido, False en caso contrario'''
        for triangulo in range(24):
            if self._puede_mover_desde_triangulo(tipo, triangulo, movimiento, tablero):
                return True
        return False
    
    def _puede_mover_desde_triangulo(self, tipo: int, triangulo: int, movimiento: int, tablero) -> bool:
        '''Verifica si se puede mover desde un triángulo específico
        Parametros:
            tipo (int): Tipo de ficha
            triangulo (int): Triángulo desde donde se quiere mover
            movimiento (int): Valor del dado para el movimiento
            tablero: El tablero de juego
        Retorna:
            bool: True si se puede mover, False en caso contrario'''
        tiene_fichas = [f for f in tablero.tablero[triangulo] if f.tipo == tipo]
        if not tiene_fichas:
            return False
        
        triangulo_destino = (
            triangulo + movimiento
            if tipo == TipoFicha.NEGRA.value
            else triangulo - movimiento
        )
        
        if self._se_pasa_tablero(tipo, triangulo_destino, triangulo, tablero):
            return False
        
        if self._es_movimiento_ganar(tipo, triangulo_destino, triangulo, tablero):
            puede_liberar = tablero.validador.puede_liberar(
                tablero.tablero, Ficha(tipo), tablero.fichas_ganadas
            )
            return puede_liberar
        
        no_hay_rivales = not tablero.validador.triangulo_con_fichas_rivales(
            tablero.tablero, triangulo_destino, Ficha(tipo)
        )
        return no_hay_rivales
    
    def _se_pasa_tablero(self, tipo: int, triangulo_destino: int, triangulo_origen: int, tablero) -> bool:
        '''Verifica si el movimiento se pasa del tablero
            Parametros:
            tipo (int): Tipo de ficha
            triangulo_destino (int): Triángulo destino del movimiento
            triangulo_origen (int): Triángulo origen del movimiento
            tablero: El tablero de juego'''
        return tablero.validador.se_pasa_del_tablero(
            Ficha(tipo), triangulo_destino, triangulo_origen, tablero.tablero
        )
    
    def _es_movimiento_ganar(self, tipo: int, triangulo_destino: int, triangulo_origen: int, tablero) -> bool:
        '''Verifica si el movimiento es para ganar
        Parametros:
            tipo (int): Tipo de ficha
            triangulo_destino (int): Triángulo destino del movimiento
            triangulo_origen (int): Triángulo origen del movimiento
            tablero: El tablero de juego
        Retorna:
            bool: True si el movimiento es para ganar, False en caso contrario'''
        puede_ganar = tablero.validador.puede_ganar(
            Ficha(tipo), triangulo_destino, triangulo_origen
        )
        no_se_pasa = not self._se_pasa_tablero(tipo, triangulo_destino, triangulo_origen, tablero)
        return puede_ganar and no_se_pasa