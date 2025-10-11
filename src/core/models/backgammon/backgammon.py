from src.core.models.dado.Dados import Dados
from src.core.models.tablero.Tablero import Tablero
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.NoHayFichaEnTriangulo import NoHayFichaEnTriangulo
from src.core.models.ficha.Ficha import Ficha


class Backgammon:
    def __init__(self,tablero:Tablero,dados:Dados):
        self.__dados__: Dados = dados
        self.__tablero__: Tablero = tablero
        self.__turno: int

    def tirar_dados(self):
        """Tira los dados y retorna el resultado
        Retorna:
            list[int]: Resultado de los dados"""
        dados = self.__dados__.tirar_dados()
        return dados

    @property
    def tablero(self):
        """Retorna el tablero"""
        return self.__tablero__

    @property
    def dados(self):
        """Retorna los dados"""
        return self.__dados__

    @property
    def turno(self):
        """Retorna el turno actual"""
        return self.__turno

    def hay_fichas_comidas(self) -> bool:
        """Verifica si hay fichas comidas del tipo de ficha correspondiente
        Paramentros:
            tipo (TipoFicha): Tipo de ficha a verificar
        Retorna:
            bool: True si hay fichas comidas del tipo, False en caso contrario
        """
        tipo = self.__turno
        if [ficha for ficha in self.__tablero__.fichas_comidas if ficha.tipo == tipo]:
            return True
        else:
            return False

    def seleccionar_ficha(self, triangulo: int, tipo: int) -> Ficha | None:
        """Selecciona una ficha del triangulo dado y del tipo dado
        Parametros:
            triangulo (int): Numero del triangulo (0-23)
            tipo (TipoFicha): Tipo de ficha a seleccionar
        Retorna:
            Ficha | None: La ficha seleccionada o None si no hay ficha del tipo en el triangulo
        Raises:
            NoHayFichaEnTriangulo: Si el triangulo no es valido o no hay ficha del tipo en el triangulo
        """
        if triangulo < 0 or triangulo > 23:
            raise NoHayFichaEnTriangulo("El triangulo seleccionado no es valido")
        fichas = self.__tablero__.tablero[triangulo]
        tipos_fichas = [ficha for ficha in fichas if ficha.tipo == tipo]
        if not tipos_fichas:
            raise NoHayFichaEnTriangulo(
                "No tiene una ficha de su color en el triangulo seleccionado"
            )
        else:
            return tipos_fichas[0]

    def mover_ficha(self, triangulo_origen: int, movimiento: int):
        """Mueve una ficha en el tablero
        Parametros:
            triangulo_origen (int): Numero del triangulo de origen (0-23)
            movimiento (int): Numero de posiciones a mover (positivo)
        Retorna: void"""
        ficha: Ficha = self.seleccionar_ficha(triangulo_origen, self.__turno)
        movimiento = (
            movimiento if self.__turno == TipoFicha.NEGRA.value else -movimiento
        )
        self.__tablero__.mover_ficha(ficha, triangulo_origen, movimiento)

    def mover_ficha_comida(self, movimiento: int):
        """Mueve una ficha comida al tablero
        Parametros:
            movimiento (int): Numero de posiciones a mover (positivo)
        Retorna: void"""
        ficha: Ficha = [
            ficha
            for ficha in self.__tablero__.fichas_comidas
            if ficha.tipo == self.__turno
        ][0]
        ficha.comida = False
        movimiento = (
            movimiento - 1 if self.__turno == TipoFicha.NEGRA.value else -movimiento
        )
        triangulo_origen = 24 if self.__turno == TipoFicha.ROJA.value else 0
        self.__tablero__.mover_ficha(ficha, triangulo_origen, movimiento, True)

    def cambiar_turno(self):
        """Cambia el turno dependiendo del turno actual"""
        self.__turno = (
            TipoFicha.NEGRA.value
            if self.__turno == TipoFicha.ROJA.value
            else TipoFicha.ROJA.value
        )

    def hay_ganador(self) -> int | None:
        """'Verifica si hay un ganador
        Retorna:
            int | None: TipoFicha del ganador o None si no hay ganador
        """
        fichas_rojas: list[Ficha] = [
            ficha
            for ficha in self.__tablero__.fichas_ganadas
            if ficha.tipo == TipoFicha.ROJA.value
        ]
        fichas_negras: list[Ficha] = [
            ficha
            for ficha in self.__tablero__.fichas_ganadas
            if ficha.tipo == TipoFicha.NEGRA.value
        ]
        if len(fichas_rojas) == 15:
            return TipoFicha.ROJA.value
        if len(fichas_negras) == 15:
            return TipoFicha.NEGRA.value
        return None


    def quien_empieza(self):
        """Determina quien empieza el juego tirando los dados
        Retorna:
            int: TipoFicha del jugador que empieza"""
        hay_Ganador = False
        while not hay_Ganador:
            dados = self.tirar_dados()
            if dados[0] > dados[1]:
                self.__turno = TipoFicha.ROJA.value
                hay_Ganador = True
            elif dados[0] < dados[1]:
                self.__turno = TipoFicha.NEGRA.value
                hay_Ganador = True

    def puede_mover_ficha(self, tipo: int, movimiento: int) -> bool:
        """Verifica si el jugador puede mover alguna ficha de su tipo en base a un movimiento
        Parametros:
            tipo (TipoFicha): Tipo de ficha a verificar
            movimiento (int): Numero de posiciones a mover (positivo)
        Retorna:
            bool: True si puede mover alguna ficha, False en caso contrario
        """
        if self.hay_fichas_comidas():
            triangulo_origen = -1 if TipoFicha.NEGRA.value == self.__turno else 24
            triangulo_destino = (
                triangulo_origen + movimiento
                if tipo == TipoFicha.NEGRA.value
                else triangulo_origen - movimiento
            )
            return not self.tablero.validador.triangulo_con_fichas_rivales(
                self.tablero.tablero, triangulo_destino, Ficha(self.__turno)
            )
        else:
            for i in range(24):
                triangulo_destino = (
                    i + movimiento if tipo == TipoFicha.NEGRA.value else i - movimiento
                )
                tiene_fichas = [
                    ficha for ficha in self.tablero.tablero[i] if ficha.tipo == tipo
                ]
                puede_ganar = self.tablero.validador.puede_ganar(
                    Ficha(tipo), triangulo_destino, i
                ) and not self.tablero.validador.se_pasa_del_tablero(
                    Ficha(tipo), triangulo_destino, i
                )
                se_pasa = self.tablero.validador.se_pasa_del_tablero(
                    Ficha(tipo), triangulo_destino, i
                )
                if not tiene_fichas:
                    continue
                if se_pasa:
                    continue
                if puede_ganar:
                    return True
                no_hay_fichas_rivales = (
                    not self.tablero.validador.triangulo_con_fichas_rivales(
                        self.tablero.tablero, triangulo_destino, Ficha(tipo)
                    )
                )
                if no_hay_fichas_rivales:
                    return True
            return False
