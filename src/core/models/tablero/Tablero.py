from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.CasillaOcupadaException import CasillaOcupadaException 
from src.core.models.tablero.Tablero_Validador import Tablero_Validador
class Tablero():
    def __init__(self,fichas:list[list[Ficha]])->None:
        self.__tablero__:list[list[Ficha]] =fichas
        self.__fichas_comidas__:list[Ficha] = []
        self.__fichas_ganadas__:list[Ficha] = []
        self.__validador__:Tablero_Validador = Tablero_Validador()

    @property 
    def fichas_comidas(self)->list[Ficha]:
        return self.__fichas_comidas__
    @fichas_comidas.setter
    def fichas_comidas(self, valor:list[Ficha])->None:
        self.__fichas_comidas__ = valor

    @property
    def fichas_ganadas(self)->list[Ficha]:
        return self.__fichas_ganadas__
    @property
    def tablero(self)->list[list[Ficha]]:
        return self.__tablero__

    def mover_ficha(self, ficha:Ficha, triangulo_origen:int, moviemiento:int):
        '''Mueve una ficha de un triángulo a otro si el movimiento es válido.
        Parámetros:
            ficha (Ficha): La ficha a mover.
            triangulo_origen (int): El triángulo de origen (0-23).
            moviemiento (int): El número de triángulos a mover (positivo)
        Raises:            
        CasillaOcupadaException: Si el triángulo de destino tiene 2 o más fichas rivales.
            '''
        if self.__validador__.triangulo_con_fichas_rivales(self.__tablero__.copy(),triangulo_origen + moviemiento, ficha): #le doy una copia para que no modifique el original
            raise CasillaOcupadaException("No se puede mover a un triángulo con 2 o mas fichas rivales")
        else:
            if self.__validador__.puede_comer(self.__tablero__.copy(),triangulo_origen + moviemiento, ficha):
                ficha_comida = self.__tablero__[triangulo_origen + moviemiento].pop()
                ficha_comida.comida = True
                self.__fichas_comidas__.append(ficha_comida) 
            self.__tablero__[triangulo_origen].remove(ficha)
            self.__tablero__[triangulo_origen+ moviemiento].append(ficha)

    # def mover_ficha_comida(self, ficha:Ficha, moviemiento:int)->None:
    #     if self.__validador__.triangulo_con_fichas_rivales(self.__tablero__.copy(),moviemiento, ficha): 
    #         raise CasillaOcupadaException("No se puede mover a un triángulo con 2 o mas fichas rivales")
    #     else:
    #         pass

    def imprimir_tablero(self) -> None:
        """
        Imprime una representación del tablero en la consola con fichas apiladas verticalmente.
        Muestra los puntos 12-7 en la línea superior izquierda
        los puntos 6-1 en la línea superior derecha
        los puntos 13-18 en la línea inferior izquierda
        los puntos 19-24 en la línea inferior derecha
        """
        print("\n" + "=" * 80)

        # Encontrar la altura máxima de las columnas
        max_height = max(len(columna) for columna in self.__tablero__)

        # Imprimir números de los puntos superiores
        print("Puntos 12-7:", end=" ")
        for i in range(11, 5, -1):
            print(f"{i+1:2}", end="     ")
        print(" | ", end=" ")
        print("Puntos 6-1:", end=" ")
        for i in range(5, -1, -1):
            print(f"{i+1:2}", end="     ")
        print()

        # Imprimir fichas superiores verticalmente
        for altura in range(max_height-1, -1, -1):
            print(" " * 11, end="")  # Alineación
            # Puntos 12-7
            for i in range(11, 5, -1):
                if altura < len(self.__tablero__[i]):
                    print(f"  [{self.__tablero__[i][altura]}]", end=" ")
                else:
                    print("   [ ]", end=" ")
            print(" | ", end=" ")
            # Puntos 6-1
            for i in range(5, -1, -1):
                if altura < len(self.__tablero__[i]):
                    print(f"  [{self.__tablero__[i][altura]}]", end=" ")
                else:
                    print("   [ ]", end=" ")
            print()

        # Imprimir línea central
        print("-" * 80)

        # Imprimir fichas inferiores verticalmente
        for altura in range(max_height):
            print(" " * 11, end="")  # Alineación
            # Puntos 13-18
            for i in range(12, 18):
                if altura < len(self.__tablero__[i]):
                    print(f"  [{self.__tablero__[i][altura]}]", end=" ")
                else:
                    print("   [ ]", end=" ")
            print(" | ", end=" ")
            # Puntos 19-24
            for i in range(18, 24):
                if altura < len(self.__tablero__[i]):
                    print(f"  [{self.__tablero__[i][altura]}]", end=" ")
                else:
                    print("   [ ]", end=" ")
            print()

        # Imprimir números de los puntos inferiores
        print("Puntos 13-18:", end=" ")
        for i in range(12, 18):
            print(f"{i+1:2}", end="     ")
        print(" | ", end=" ")
        print("Puntos 19-24:", end=" ")
        for i in range(18, 24):
            print(f"{i+1:2}", end="     ")
        print()

        print("=" * 80)

        # Mostrar fichas comidas y ganadas si hay
        if self.__fichas_comidas__:
            print("Fichas comidas:", "".join([str(ficha) for ficha in self.__fichas_comidas__]))
        if self.__fichas_ganadas__:
            print("Fichas ganadas:", "".join([str(ficha) for ficha in self.__fichas_ganadas__]))
    