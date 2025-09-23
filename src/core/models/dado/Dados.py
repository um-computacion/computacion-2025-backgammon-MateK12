import random


class Dados:

    def __init__(self):
        self.__doble__: bool = False

    def tirar_dados(self) -> list[int]:
        """
        Tira dos dados y devuelve un diccionario con los resultados de ambos dados
        Si los dados son iguales, cambia el atributo doble a True, de lo contrario a False.
        """
        self.__doble__ = False
        dice_1: int = random.randint(1, 6)
        dice_2: int = random.randint(1, 6)
        if dice_1 == dice_2:
            self.__doble__ = True
            return [dice_1, dice_2, dice_1, dice_2]
        else:
            self.__doble__ = False
        return [dice_1, dice_2]

    @property
    def doble(self):
        """
        Retorna doble
        """
        return self.__doble__
