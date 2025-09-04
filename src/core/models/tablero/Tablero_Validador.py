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
        Verifica si en el triángulo dado hay SOLO una ficha del tipo rival
        '''
        tipo_rival = TipoFicha.ROJA.value if ficha.tipo == TipoFicha.NEGRA.value else TipoFicha.NEGRA.value
        tipos_en_triangulo = [f.tipo for f in tablero[triangulo]]
        if tipos_en_triangulo.count(tipo_rival) == 1:
            return True
        return False
    def tiene_fichas_comidas(self,tablero,ficha:Ficha)->bool:
        tipo = ficha.tipo
        for triangulo in tablero:
            for f in triangulo:
                if f.tipo == tipo:
                    return False
        return True