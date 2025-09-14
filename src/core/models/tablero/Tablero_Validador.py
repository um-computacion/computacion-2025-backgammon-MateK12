from core.models import ficha
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