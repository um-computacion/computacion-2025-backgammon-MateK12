from src.core.enums.TipoFicha import TipoFicha
from src.core.models.ficha.Ficha import Ficha
from src.core.exceptions.MovimientoNoJustoParaGanar import MovimientoNoJustoParaGanar


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

    def tiene_fichas_comidas(self, tablero, ficha: Ficha) -> bool:
        """Verifica si el jugador tiene fichas comidas
        Parametros:
            tablero (list[list[Ficha]]): El tablero de juego
            ficha (Ficha): La ficha del jugador a verificar
        Retorna:
            bool: True si tiene fichas comidas, False en caso contrario
        """
        tipo = ficha.tipo
        for triangulo in tablero:
            for f in triangulo:
                if f.tipo == tipo:
                    return False
        return True

    def puede_ganar(
        self, ficha: Ficha, triangulo_destino, triangulo_origen: int, movimiento: int
    ) -> bool:
        """Verifica si el jugador puede ganar esa ficha
        Parametros:
            tablero (list[list[Ficha]]): El tablero de juego
            ficha (Ficha): La ficha del jugador a verificar
            triangulo_destino (int): El triángulo al que se quiere mover la ficha
        Retorna:
            bool: True si puede ganar, False en caso contrario
        Raises:
            MovimientoNoJustoParaGanar si el movimiento lleva a un numero fuera del tablero, >-1 para las fichas rojas y >24 para las negras
        """
        tipo = ficha.tipo
        if tipo == TipoFicha.ROJA.value:
            if triangulo_destino == -1 and triangulo_origen < 6:
                return True
            if (
                triangulo_origen < 5 and triangulo_origen + movimiento < -1
            ):  # lo dejo sumando porque el movimiento rojo es negativo
                raise MovimientoNoJustoParaGanar(
                    "Movimiento no válido para ganar la ficha, se pasa"
                )
        elif tipo == TipoFicha.NEGRA.value and triangulo_destino > 24:
            raise MovimientoNoJustoParaGanar(
                "Movimiento no válido para ganar la ficha, se pasa"
            )
        elif tipo == TipoFicha.NEGRA.value and triangulo_destino == 24:
            return True
        return False
