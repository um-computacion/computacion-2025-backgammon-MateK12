from abc import ABC, abstractmethod

class IJuegoInterfazDados(ABC):


    @abstractmethod
    def seleccion_dado_valida(self) -> bool:
        pass
