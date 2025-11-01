from abc import ABC, abstractmethod
from src.core.models.tablero.Tablero import Tablero

class IEstrategiaMovible(ABC):
    @abstractmethod
    def ejecutar(self, tipo: int, dados: list[int], tablero: Tablero, backgammon) -> None:
        """Ejecuta el movimiento si aplica la estrategia"""
        pass