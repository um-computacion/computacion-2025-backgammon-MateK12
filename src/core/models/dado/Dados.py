import random
class Dados:

    def __init__(self):
        self.__doble__:bool = False
    '''
    Tira dos dados y devuelve un diccionario con los resultados de ambos dados
    Si los dados son iguales, cambia el atributo doble a True, de lo contrario a False.
    '''
    def tirar_dados(self)->dict['dado1':int, 'dado2':int]:
        dice_1:int= random.randint(1, 6)
        dice_2:int= random.randint(1, 6)
        if dice_1 == dice_2:
            self.__doble__ = True
        else:
            self.__doble__ = False
        return {'dado1': dice_1, 'dado2': dice_2}

    @property
    def doble(self):
        return self.__doble__