from abc import ABC, abstractmethod

class IJuegoInterfazDados(ABC):


    @abstractmethod
    def tirar_dados(self):
        pass
    @abstractmethod
    def seleccion_dado_valida(self) -> bool:
        pass
