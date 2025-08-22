### modelo
Claude
### propmt 
queiro representar una ficha de backgammon en el cli, hay alguna manera de ponerle color negro o rojo? ten en cuenta que tiene que ser un circulo

### respuesta    

class Ficha:
    # Códigos de color ANSI
    COLORES = {
        'negro': '\033[30m',
        'rojo': '\033[31m',
        'reset': '\033[0m'
    }
    
    def __init__(self, color):
        """
        Inicializa una ficha con un color específico.
        
        Args:
            color (str): 'negro' o 'rojo'
        """
        if color not in ['negro', 'rojo']:
            raise ValueError("El color debe ser 'negro' o 'rojo'")
        self.color = color
    
    def __repr__(self):
        """
        Representa la ficha como un círculo coloreado en la terminal.
        """
        color_code = self.COLORES[self.color]
        reset = self.COLORES['reset']
        return f"{color_code}●{reset}"
    
    def __str__(self):
        """
        Representación string más descriptiva.
        """
        return f"Ficha({self.color})"
    
    def __eq__(self, other):
        """
        Compara dos fichas por su color.
        """
        if not isinstance(other, Ficha):
            return False
        return self.color == other.color

ef __repr__(self):
   colores = {'negro': '\033[30m●\033[0m', 'rojo': '\033[31m●\033[0m'}
   return colores.get(self.color, '●')
### cambios
use la ultima funcion como guia, porque lo otro no me parecio necesario 
### archivos finales
Test_ficha

### modelo
Claude
### propmt 
### respuesta    


### Fixed
### cambios
### archivos finales
