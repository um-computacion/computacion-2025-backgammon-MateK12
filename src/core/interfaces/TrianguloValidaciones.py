from abc import ABC, abstractmethod

# pylint: disable=C0116
class ITrianguloValidaciones(ABC):

    @abstractmethod
    def seleccion_triangulo_valida(triangulo) -> bool:
        pass
