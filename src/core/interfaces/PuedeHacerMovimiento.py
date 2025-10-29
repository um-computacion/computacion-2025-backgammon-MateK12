from abc import ABC, abstractmethod

# pylint: disable=C0116
class IPuedeHacerMovimiento(ABC):

    @abstractmethod
    def puede_hacer_algun_movimiento(self):
        pass
