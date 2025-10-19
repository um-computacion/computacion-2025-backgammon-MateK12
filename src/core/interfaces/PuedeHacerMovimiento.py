from abc import ABC, abstractmethod


class IPuedeHacerMovimiento(ABC):

    @abstractmethod
    def puede_hacer_algun_movimiento(self):
        pass
