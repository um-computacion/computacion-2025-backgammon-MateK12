from src.core.enums.TipoFicha import TipoFicha
from src.core.models.ficha.Ficha import Ficha

class Tablero_Validador:
    def triangulo_con_fichas_rivales(self,tablero, triangulo:int,ficha:Ficha)->bool:
        '''
        Verifica si en el triángulo dado hay al menos dos fichas del tipo rival
        '''
        tipo_rival = TipoFicha.ROJA.value if ficha.tipo == TipoFicha.NEGRA.value else TipoFicha.NEGRA.value
        tipos_en_triangulo = [f.tipo for f in tablero[triangulo]]
        if tipos_en_triangulo.count(tipo_rival) >= 2:
            return True
        return False
    def puede_comer(self,tablero, triangulo:int,ficha:Ficha)->bool:
        '''
        Verifica si en el triángulo dado hay solo una ficha del tipo rival
        Parametros:
            tablero (list[list[Ficha]]): El tablero de juego
            triangulo (int): El triángulo a verificar
            ficha (Ficha): La ficha que se está moviendo
        Retorna:
            bool: True si puede comer, False en caso contrario
        '''
        tipo_rival = TipoFicha.ROJA.value if ficha.tipo == TipoFicha.NEGRA.value else TipoFicha.NEGRA.value
        tipos_en_triangulo = [f.tipo for f in tablero[triangulo]]
        if tipos_en_triangulo.count(tipo_rival) == 1:
            return True
        return False
    def tiene_fichas_comidas(self,tablero,ficha:Ficha)->bool:
        '''Verifica si el jugador tiene fichas comidas 
        Parametros:
            tablero (list[list[Ficha]]): El tablero de juego
            ficha (Ficha): La ficha del jugador a verificar
        Retorna:
            bool: True si tiene fichas comidas, False en caso contrario
        '''
        tipo = ficha.tipo
        for triangulo in tablero:
            for f in triangulo:
                if f.tipo == tipo:
                    return False
        return True
    def puede_ganar(self,ficha:Ficha,triangulo_destino)->bool:
        '''Verifica si el jugador puede ganar esa ficha
        Parametros:
            tablero (list[list[Ficha]]): El tablero de juego
            ficha (Ficha): La ficha del jugador a verificar
            triangulo_destino (int): El triángulo al que se quiere mover la ficha
        Retorna:
            bool: True si puede ganar, False en caso contrario
        '''
        tipo = ficha.tipo
        if tipo == TipoFicha.ROJA.value and triangulo_destino ==-1:
            return True
        elif tipo == TipoFicha.NEGRA.value and triangulo_destino ==24:
            return True
        return False
    def esta_rango_ganar(self,ficha:Ficha,triangulo_origen:int)->bool:
        '''Verifica si la ficha está en rango de ganar
        Parametros:
            ficha (Ficha): La ficha del jugador a verificar
            triangulo_origen (int): El triángulo donde está la ficha
        Retorna:
            bool: True si la ficha esta en rango de ganar (un movimiento de 0 a 6), False en caso contrario
        '''
        if ficha.tipo == TipoFicha.ROJA.value and triangulo_origen in range(0,6):
            return True
        elif ficha.tipo == TipoFicha.NEGRA.value and triangulo_origen in range(18,24):
            return True
        return False