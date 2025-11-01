from abc import ABC, abstractmethod
from src.core.models.tablero.Tablero import Tablero

class IEstrategiaPuedeMover(ABC):
    @abstractmethod
    def puede_mover(self, tipo: int, dados: list[int], tablero: Tablero, backgammon) -> bool:
        pass