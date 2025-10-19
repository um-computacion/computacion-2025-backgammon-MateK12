from abc import ABC, abstractmethod


class ITrianguloValidaciones(ABC):

    @abstractmethod
    def seleccion_triangulo_valida(triangulo) -> bool:
        pass
