from abc import ABC, abstractmethod


class ICartelUI(ABC):

    @abstractmethod
    def mostrar_cartel(self, mensaje: str, duracion: float = 3.0, titulo: str = "Error"):
        pass

    @abstractmethod
    def actualizar_y_dibujar(self, screen):
        pass