from src.core.enums.TipoFicha import TipoFicha
from src.core.models.ficha.Ficha import Ficha


class Tablero_Validador:
    def triangulo_con_fichas_rivales(
        self, tablero, triangulo: int, ficha: Ficha
    ) -> bool:
        """
        Verifica si en el triángulo dado hay al menos dos fichas del tipo rival
        Parametros:
            tablero (list[list[Ficha]]): El tablero de juego
            triangulo (int): El triángulo a verificar
            ficha (Ficha): La ficha que se está moviendo
        Retorna:
            bool: True si hay al menos dos fichas rivales, False en caso contrario
        """
        tipo_rival = (
            TipoFicha.ROJA.value
            if ficha.tipo == TipoFicha.NEGRA.value
            else TipoFicha.NEGRA.value
        )
        tipos_en_triangulo = [f.tipo for f in tablero[triangulo]]
        if tipos_en_triangulo.count(tipo_rival) >= 2:
            return True
        return False

    def puede_comer(self, tablero, triangulo: int, ficha: Ficha) -> bool:
        """
        Verifica si en el triángulo dado hay solo una ficha del tipo rival
        Parametros:
            tablero (list[list[Ficha]]): El tablero de juego
            triangulo (int): El triángulo a verificar
            ficha (Ficha): La ficha que se está moviendo
        Retorna:
            bool: True si puede comer, False en caso contrario
        """
        tipo_rival = (
            TipoFicha.ROJA.value
            if ficha.tipo == TipoFicha.NEGRA.value
            else TipoFicha.NEGRA.value
        )
        tipos_en_triangulo = [f.tipo for f in tablero[triangulo]]
        if tipos_en_triangulo.count(tipo_rival) == 1:
            return True
        return False

    def puede_ganar(
        self, ficha: Ficha, triangulo_destino: int, triangulo_origen: int
    ) -> bool:
        """Verifica si el jugador puede ganar esa ficha (llega exactamente al final)
        Parametros:
            ficha (Ficha): La ficha del jugador a verificar
            triangulo_destino (int): El triángulo al que se quiere mover la ficha
            triangulo_origen (int): El triángulo desde donde se mueve la ficha
        Retorna:
            bool: True si puede ganar (llega exactamente al final), False en caso contrario
        """
        tipo = ficha.tipo

        if tipo == TipoFicha.ROJA.value:
            return triangulo_destino == -1 and triangulo_origen < 6
        elif tipo == TipoFicha.NEGRA.value:
            return triangulo_destino == 24 and triangulo_origen > 17

        return False

    def se_pasa_del_tablero(
        self, ficha: Ficha, triangulo_destino: int, triangulo_origen: int
    ) -> bool:
        """Verifica si el movimiento se pasa del tablero (va más allá del final)
        Parametros:
            ficha (Ficha): La ficha del jugador a verificar
            triangulo_destino (int): El triángulo al que se quiere mover la ficha
            triangulo_origen (int): El triángulo desde donde se mueve la ficha
            movimiento (int): El valor del dado/movimiento
        Retorna:
            bool: True si se pasa del tablero, False en caso contrario
        """
        tipo = ficha.tipo

        if tipo == TipoFicha.ROJA.value:
            if triangulo_origen < 6 and triangulo_destino < -1:
                return True
        elif tipo == TipoFicha.NEGRA.value:
            if triangulo_origen > 17 and triangulo_destino > 24:
                return True

        return False
    def puede_liberar(
        self, tablero, ficha: Ficha,fichas_ganadas:list[Ficha]
    ) -> bool:
        """
        Verifica si el jugador puede liberar una ficha desde la barra, osea si hay bear off o no
        Parametros:
            tablero (list[list[Ficha]]): El tablero de juego
            ficha (Ficha): La ficha que se está moviendo
        """
        fichas_ganadas = [f for f in fichas_ganadas if f.tipo == ficha.tipo]
        fichas_restantes = 15 - len(fichas_ganadas)
        agg_len=0
        if ficha.tipo == TipoFicha.ROJA.value:
            for triangulo in range(0, 6):
                fichas_rojas_en_triangulo = [f for f in tablero[triangulo] if f.tipo == TipoFicha.ROJA.value]
                agg_len += len(fichas_rojas_en_triangulo)
            return fichas_restantes == agg_len
        elif ficha.tipo == TipoFicha.NEGRA.value:
            agg_len=0
            for triangulo in range(18, 24):
                fichas_negras_en_triangulo = [f for f in tablero[triangulo] if f.tipo == TipoFicha.NEGRA.value]
                agg_len += len(fichas_negras_en_triangulo)
            return agg_len == fichas_restantes
