from abc import ABC, abstractmethod

# pylint: disable=C0116
class IDadosValidaciones(ABC):

    @abstractmethod
    def seleccion_dado_valida(self):
        pass
