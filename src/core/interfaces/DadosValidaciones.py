from abc import ABC, abstractmethod


class IDadosValidaciones(ABC):

    @abstractmethod
    def seleccion_dado_valida(self):
        pass
