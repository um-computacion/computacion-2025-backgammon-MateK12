from abc import ABC, abstractmethod

# pylint: disable=C0116
class ICartelUI(ABC):

    @abstractmethod
    def mostrar_cartel(self, mensaje: str, duracion: float, titulo: str ,color_fondo:tuple,color_texto:tuple):
        pass

    @abstractmethod
    def actualizar_y_dibujar(self, screen):
        pass