import pygame
import time

class Cartel_ErrorUI:
    def __init__(self,posicion:tuple,):
        self.__error_activo = False
        self.__tiempo_error_inicio = 0
        self.__mensaje_error = ""
        self.__duracion_error = 3.0

        self.__font_titulo = pygame.font.Font(None, 36)
        self.__font_mensaje = pygame.font.Font(None, 24)
        self.__color_fondo = (255, 0, 0)
        self.__color_texto = (255, 255, 255)
        self.__posicion = posicion
        self.__ancho = 400
        self.__alto = 150

    @property
    def error_activo(self) -> bool:
        """Indica si hay un error activo que mostrar"""
        return self.__error_activo
    def mostrar_error(self, mensaje: str, duracion: float = 3.0):
        """
        Configura un error para mostrar durante el tiempo especificado
        
        Args:
            mensaje (str): Mensaje de error a mostrar
            duracion (float): Duración en segundos (por defecto 3.0)
        """
        self.__error_activo = True
        self.__tiempo_error_inicio = time.time()
        self.__mensaje_error = str(mensaje)
        self.__duracion_error = duracion

    def actualizar_y_dibujar(self,screen: pygame.Surface):
        """
        Actualiza el estado del error y lo dibuja si está activo
        Debe llamarse en cada frame del loop principal
        """
        if not self.__error_activo:
            return
            
        tiempo_actual = time.time()
        if tiempo_actual - self.__tiempo_error_inicio >= self.__duracion_error:
            self.__error_activo = False
            return
        
        self.__dibujar_error(screen)

    def __dibujar_error(self, screen: pygame.Surface):
        """Dibuja el cartel de error en pantalla"""
        offset_x = self.__ancho // 2
        offset_y = self.__alto // 2
        pygame.draw.rect(screen, self.__color_fondo, 
                        (self.__posicion[0]-offset_x, self.__posicion[1]-offset_y, self.__ancho, self.__alto))

        titulo = self.__font_titulo.render("ERROR", True, self.__color_texto)
        titulo_rect = titulo.get_rect()
        titulo_x = self.__posicion[0] - (offset_x - 10)
        screen.blit(titulo, (titulo_x, self.__posicion[1]-offset_y + 10))

        y_mensaje = self.__posicion[1]+5
        lineas_mensaje = self.__dividir_mensaje(self.__mensaje_error)

        for linea in lineas_mensaje:
            mensaje_surface = self.__font_mensaje.render(linea, True, self.__color_texto)
            screen.blit(mensaje_surface, (self.__posicion[0]-offset_x, y_mensaje))
            y_mensaje += 20

    def __dividir_mensaje(self, mensaje: str, max_caracteres: int = 45) -> list[str]:
        """Divide el mensaje en líneas para que quepa en el cartel"""
        if len(mensaje) <= max_caracteres:
            return [mensaje]
        
        palabras = mensaje.split(' ')
        lineas = []
        linea_actual = ""
        
        for palabra in palabras:
            if len(linea_actual + palabra + " ") <= max_caracteres:
                linea_actual += palabra + " "
            else:
                if linea_actual:
                    lineas.append(linea_actual.strip())
                linea_actual = palabra + " "
        
        if linea_actual:
            lineas.append(linea_actual.strip())
        
        return lineas[:3]  # Máximo 3 líneas

