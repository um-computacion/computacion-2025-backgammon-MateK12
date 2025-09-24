from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.CasillaOcupadaException import CasillaOcupadaException
from src.core.models.tablero.Tablero_Validador import Tablero_Validador


class Tablero:
    def __init__(self, fichas: list[list[Ficha]]) -> None:
        self.__tablero__: list[list[Ficha]] = fichas
        self.__fichas_comidas__: list[Ficha] = []
        self.__fichas_ganadas__: list[Ficha] = []
        self.__validador__: Tablero_Validador = Tablero_Validador()

    @property
    def fichas_comidas(self) -> list[Ficha]:
        """Retorna las fichas comidas"""
        return self.__fichas_comidas__

    @fichas_comidas.setter
    def fichas_comidas(self, valor: list[Ficha]) -> None:
        """Establece las fichas comidas"""
        self.__fichas_comidas__ = valor

    @property
    def fichas_ganadas(self) -> list[Ficha]:
        """Retorna las fichas ganadas"""
        return self.__fichas_ganadas__

    @property
    def tablero(self) -> list[list[Ficha]]:
        """Retorna el tablero"""
        return self.__tablero__

    def mover_ficha(
        self, ficha: Ficha, triangulo_origen: int, movimiento: int, comida: bool = False
    ) -> None:
        """Mueve una ficha de un triángulo a otro si el movimiento es válido.
        Parámetros:
            ficha (Ficha): La ficha a mover.
            triangulo_origen (int): El triángulo de origen (0-23).
            movimiento (int): El número de triángulos a mover (positivo)
        Raises:
        CasillaOcupadaException: Si el triángulo de destino tiene 2 o más fichas rivales.
        """
        triangulo_destino = triangulo_origen + movimiento
        if self.__validador__.puede_ganar(
            ficha, triangulo_destino, triangulo_origen, movimiento
        ):
            self.__tablero__[triangulo_origen].pop()
            self.__fichas_ganadas__.append(ficha)
            return
        if self.__validador__.triangulo_con_fichas_rivales(
            self.tablero, triangulo_destino, ficha
        ):  # le doy una copia para que no modifique el original
            raise CasillaOcupadaException(
                "No se puede mover a un triángulo con 2 o mas fichas rivales"
            )
        else:
            if self.__validador__.puede_comer(self.tablero, triangulo_destino, ficha):
                ficha_comida = self.__tablero__[triangulo_destino].pop()
                ficha_comida.comida = True
                self.__fichas_comidas__.append(ficha_comida)
            if comida:
                ficha.comida = False
                self.__fichas_comidas__.remove(ficha)
            else:
                self.__tablero__[triangulo_origen].pop()
            self.__tablero__[triangulo_destino].append(ficha)
