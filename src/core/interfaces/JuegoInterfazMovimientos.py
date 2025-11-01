from abc import ABC, abstractmethod

#pylint: disable=C0116
class IJuegoInterfazMovimientos(ABC):

    @abstractmethod
    def realizar_movimiento(self):
        pass
