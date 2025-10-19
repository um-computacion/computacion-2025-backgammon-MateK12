from abc import ABC, abstractmethod


class IJuegoInterfazMovimientos(ABC):

    @abstractmethod
    def realizar_movimiento(self):
        pass
