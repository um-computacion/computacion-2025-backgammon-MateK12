from src.core.models.tablero.Tablero import Tablero
class Tablero_Impresor():
    @staticmethod
    def imprimir_tablero(tablero:Tablero)->None:
        """
        Imprime una representación del tablero en la consola con fichas apiladas verticalmente.
        Muestra los puntos 12-7 en la línea superior izquierda
        los puntos 6-1 en la línea superior derecha
        los puntos 13-18 en la línea inferior izquierda
        los puntos 19-24 en la línea inferior derecha
        """
        print("\n" + "=" * 80)

        # Encontrar la altura máxima de las columnas
        max_height = max(len(columna) for columna in tablero.tablero)

        # Imprimir números de los puntos superiores
        print("Puntos 12-7:", end=" ")
        for i in range(11, 5, -1):
            print(f"{i:2}", end="     ")
        print(" | ", end=" ")
        for i in range(5, -1, -1):
            print(f"{i:2}", end="     ")
        print()

        # Imprimir fichas superiores verticalmente
        for altura in range(max_height-1, -1, -1):
            print(" " * 11, end="")  # Alineación
            # Puntos 12-7
            for i in range(11, 5, -1):
                if altura < len(tablero.tablero[i]):
                    print(f"  [{tablero.tablero[i][altura]}]", end=" ")
                else:
                    print("   [ ]", end=" ")
            print(" | ", end=" ")
            # Puntos 6-1
            for i in range(5, -1, -1):
                if altura < len(tablero.tablero[i]):
                    print(f"  [{tablero.tablero[i][altura]}]", end=" ")
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
                if altura < len(tablero.tablero[i]):
                    print(f"  [{tablero.tablero[i][altura]}]", end=" ")
                else:
                    print("   [ ]", end=" ")
            print(" | ", end=" ")
            # Puntos 19-24
            for i in range(18, 24):
                if altura < len(tablero.tablero[i]):
                    print(f"  [{tablero.tablero[i][altura]}]", end=" ")
                else:
                    print("   [ ]", end=" ")
            print()

        # Imprimir números de los puntos inferiores
        print("Puntos 13-18:", end=" ")
        for i in range(12, 18):
            print(f"{i:2}", end="     ")
        print(" | ", end=" ")
        for i in range(18, 24):
            print(f"{i:2}", end="     ")
        print()

        print("=" * 80)

        # Mostrar fichas comidas y ganadas si hay
        if tablero.fichas_comidas:
            print("Fichas comidas:", "".join([str(ficha) for ficha in tablero.fichas_comidas]))
        if tablero.fichas_ganadas:
            print("Fichas ganadas:", "".join([str(ficha) for ficha in tablero.fichas_ganadas]))
