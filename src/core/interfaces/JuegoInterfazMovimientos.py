from abc import ABC, abstractmethod

class IJuegoInterfazMovimientos(ABC):

    @abstractmethod
    def realizar_movimiento(self):
        pass

    @abstractmethod
    def puede_hacer_algun_movimiento(self):
        pass

