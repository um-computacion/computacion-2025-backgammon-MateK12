from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
class Tablero_inicializador():
    @staticmethod
    def inicializar_tablero() -> list[list[Ficha | None]]:
        """Inicializa el tablero con la configuración inicial del backgammon
        Retorna:
            list[list[Ficha | None]]: Tablero inicial con fichas en sus posiciones correspondientes (como indican las reglas del backgammon)
        """
        tablero_inicial: list[list[Ficha]] = [[] for _ in range(24)]
        tablero_inicial[0] = [Ficha(TipoFicha.NEGRA.value) for _ in range(2)]
        tablero_inicial[11] = [Ficha(TipoFicha.NEGRA.value) for _ in range(5)]
        tablero_inicial[16] = [Ficha(TipoFicha.NEGRA.value) for _ in range(3)]
        tablero_inicial[18] = [Ficha(TipoFicha.NEGRA.value) for _ in range(5)]
        tablero_inicial[23] = [Ficha(TipoFicha.ROJA.value) for _ in range(2)]
        tablero_inicial[12] = [Ficha(TipoFicha.ROJA.value) for _ in range(5)]
        tablero_inicial[7] = [Ficha(TipoFicha.ROJA.value) for _ in range(3)]
        tablero_inicial[5] = [Ficha(TipoFicha.ROJA.value) for _ in range(5)]
        return tablero_inicial
