from src.core.models.dado.Dados import Dados
from src.core.models.tablero.Tablero import Tablero
from src.core.enums.TipoFicha import TipoFicha
from src.core.exceptions.NoHayFichaEnTriangulo import NoHayFichaEnTriangulo
from src.core.models.ficha.Ficha import Ficha
from src.core.models.backgammon.Backgammon_Turnos import Backgammon_Turnos
from src.core.interfaces.DadosValidaciones import IDadosValidaciones
from src.core.exceptions.SeleccionDadoInvalida import SeleccionDadoInvalida
from src.core.exceptions.SeleccionTrianguloInvalida import SeleccionTrianguloInvalida
from src.core.interfaces.TrianguloValidaciones import ITrianguloValidaciones
from src.core.exceptions.NingunMovimientoPosible import NingunMovimientoPosible


class Backgammon(IDadosValidaciones, ITrianguloValidaciones):
    def __init__(
        self, tablero: Tablero, dados: Dados, BackgammonTurno: Backgammon_Turnos
    ):
        self.__dados__: Dados = dados
        self.__tablero__: Tablero = tablero
        self.__backgammon_turno = BackgammonTurno
        self.__dados_disponibles: list[int] = []
    @property
    def tablero(self):
        """Retorna el tablero"""
        return self.__tablero__

    @property
    def dados(self):
        """Retorna los dados"""
        return self.__dados__

    @property
    def turnero(self):
        """Retorna el tunero de backgammon"""
        return self.__backgammon_turno
    
    @property
    def dados_disponibles(self):
        """Retorna los dados disponibles"""
        return self.__dados_disponibles

    @dados_disponibles.setter
    def dados_disponibles(self, dados):
        """Setea los dados disponibles"""
        for dado in dados:
            self.seleccion_dado_valida(dado)
        self.__dados_disponibles = dados
    
    def seleccion_triangulo_valida(self, triangulo: int):
        """Verifica si la seleccion de triangulo es valida
        Parametros:
            triangulo (int): Numero del triangulo seleccionado
        Retorna:
            bool: True si la seleccion es valida
        Raises:
            SeleccionTrianguloInvalida: Si la seleccion no es valida
        """
        if triangulo is None:
            raise SeleccionTrianguloInvalida("El triangulo no puede ser indefinido")
        if type(triangulo) is not int:
            raise SeleccionTrianguloInvalida("El triangulo debe ser un numero entero")
        if not (0 <= triangulo <= 23):
            raise SeleccionTrianguloInvalida(f"El triangulo {triangulo} no es valido")
        return True

    def seleccion_dado_valida(self, dado: int):
        """Verifica si la seleccion del dado es valida
        Parametros:
            dados int: el dado seleccionado
        Retorna:
            bool: True si la seleccion es valida
        Raises:
            SeleccionDadoInvalida: Si la seleccion no es valida
        """
        if not dado:
            raise SeleccionDadoInvalida("El dado no puede ser indefinido")
        if type(dado) is not int:
            raise SeleccionDadoInvalida("El dado debe ser un numero entero")
        if not (dado <= 6 and dado >= 1):
            raise SeleccionDadoInvalida(f"El dado {dado} no es valido")
        return True

    def hay_fichas_comidas(self) -> bool:
        """Verifica si hay fichas comidas del tipo de ficha correspondiente
        Paramentros:
            tipo (TipoFicha): Tipo de ficha a verificar
        Retorna:
            bool: True si hay fichas comidas del tipo, False en caso contrario
        """
        tipo = self.__backgammon_turno.turno
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
            raise SeleccionTrianguloInvalida("El triangulo seleccionado no es valido")
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
        self.seleccion_triangulo_valida(triangulo_origen)
        self.seleccion_dado_valida(movimiento)
        ficha: Ficha = self.seleccionar_ficha(
            triangulo_origen, self.__backgammon_turno.turno
        )
        movimiento = (
            movimiento
            if self.__backgammon_turno.turno == TipoFicha.NEGRA.value
            else -movimiento
        )
        self.__tablero__.mover_ficha(ficha, triangulo_origen, movimiento)
        self.__dados_disponibles.remove(abs(movimiento))

    def mover_ficha_comida(self, movimiento: int):
        """Mueve una ficha comida al tablero
        Parametros:
            movimiento (int): Numero de posiciones a mover (positivo)
        Retorna: void"""
        self.seleccion_dado_valida(movimiento)
        ficha: Ficha = [
            ficha
            for ficha in self.__tablero__.fichas_comidas
            if ficha.tipo == self.__backgammon_turno.turno
        ][0]
        movimiento = (
            movimiento - 1
            if self.__backgammon_turno.turno == TipoFicha.NEGRA.value
            else -movimiento
        )
        triangulo_origen = (
            24 if self.__backgammon_turno.turno == TipoFicha.ROJA.value else 0
        )
        self.__tablero__.mover_ficha(ficha, triangulo_origen, movimiento, True)
        dado_valido = movimiento + 1 if self.__backgammon_turno.turno == TipoFicha.NEGRA.value else abs(movimiento)
        self.__dados_disponibles.remove(abs(dado_valido))

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

    def puede_mover_ficha(self, tipo: int, dados: list[int]) -> bool:
        """Verifica si el jugador puede mover alguna ficha de su tipo en base a un movimiento
        Parametros:
            tipo (TipoFicha): Tipo de ficha a verificar
            dados (list[int]): Lista de dados disponibles
        Retorna:
            bool: True si puede mover alguna ficha, False en caso contrario
        """
        movimientos_totales = []

        for movimiento in dados:
            if self.hay_fichas_comidas():
                triangulo_origen = (
                    -1 if TipoFicha.NEGRA.value == self.__backgammon_turno.turno else 24
                )
                triangulo_destino = (
                    triangulo_origen + movimiento
                    if tipo == TipoFicha.NEGRA.value
                    else triangulo_origen - movimiento
                )
                if self.__tablero__.validador.triangulo_con_fichas_rivales(
                    self.__tablero__.tablero, triangulo_destino, Ficha(tipo)
                ):
                    continue
                movimientos_totales.append(movimiento)
            else:
                for i in range(24):
                    triangulo_destino = (
                        i + movimiento
                        if tipo == TipoFicha.NEGRA.value
                        else i - movimiento
                    )
                    tiene_fichas = [
                        ficha for ficha in self.tablero.tablero[i] if ficha.tipo == tipo
                    ]
                    movimiento_justo_para_ganar = self.tablero.validador.puede_ganar(
                        Ficha(tipo), triangulo_destino, i
                    ) and not self.tablero.validador.se_pasa_del_tablero(
                        Ficha(tipo), triangulo_destino, i, self.tablero.tablero
                    )
                    puede_liberar = self.tablero.validador.puede_liberar(
                        self.tablero.tablero, Ficha(tipo), self.tablero.fichas_ganadas
                    )
                    se_pasa = self.tablero.validador.se_pasa_del_tablero(
                        Ficha(tipo), triangulo_destino, i, self.tablero.tablero
                    )

                    if not tiene_fichas:
                        movimientos_totales.append(0)
                        continue
                    if se_pasa:
                        movimientos_totales.append(0)
                        continue
                    if movimiento_justo_para_ganar and puede_liberar:
                        movimientos_totales.append(movimiento)
                        continue
                    if movimiento_justo_para_ganar and not puede_liberar:
                        movimientos_totales.append(0)
                        continue
                    no_hay_fichas_rivales = (
                        not self.tablero.validador.triangulo_con_fichas_rivales(
                            self.tablero.tablero, triangulo_destino, Ficha(tipo)
                        )
                    )
                    if no_hay_fichas_rivales:
                        movimientos_totales.append(movimiento)
                        continue
                    movimientos_totales.append(0)

        movimientos_validos = [f for f in movimientos_totales if f > 0]
        if len(movimientos_validos)==2 and len(dados)==2 and abs(movimientos_totales.index(dados[0])-movimientos_totales.index(movimientos_validos[1]))==24:
            triangulo_origen = movimientos_totales.index(dados[0])
            no_es_unica_ficha =len([f for f in self.tablero.tablero[triangulo_origen] if f.tipo == tipo]) != 1
            if dados[0] == dados[1] or no_es_unica_ficha:
                return True
            if not self._puede_mover_suma_ambos(tipo,dados,movimientos_totales):
                dado = max(dados)
                triangulo_origen = movimientos_totales.index(dados[0])
                self.mover_ficha(triangulo_origen, dado)

        if movimientos_validos:
            return True

        turno_string = "Rojo" if tipo == TipoFicha.ROJA.value else "Negro"
        self.dados_disponibles = []
        raise NingunMovimientoPosible(
                "No hay movimientos posibles con los dados: {} y turno: {}".format(
                    dados, turno_string
                )
            )

    def _puede_mover_suma_ambos(self,tipo: int, dados: list[int],movimientos_totales: list[int]):
        """Verifica si el jugador puede una ficha en especifico de su tipo en base a la suma de ambos dados
        Parametros:
            tipo (TipoFicha): Tipo de ficha a verificar
            dados (list[int]): Lista de dados disponibles
        Retorna:
            bool: True si puede mover alguna ficha, False en caso contrario
        """
        suma_dados = sum(dados)
        triangulo_origen = movimientos_totales.index(dados[0])
        triangulo_destino = (
            triangulo_origen + suma_dados
            if tipo == TipoFicha.NEGRA.value
            else triangulo_origen - suma_dados
        )
        movimiento_justo_para_ganar = self.tablero.validador.puede_ganar(
            Ficha(tipo), triangulo_destino, triangulo_origen
        ) and not self.tablero.validador.se_pasa_del_tablero(
            Ficha(tipo), triangulo_destino, triangulo_origen, self.tablero.tablero
        )
        puede_liberar = self.tablero.validador.puede_liberar(
            self.tablero.tablero, Ficha(tipo), self.tablero.fichas_ganadas
        )
        se_pasa = self.tablero.validador.se_pasa_del_tablero(
            Ficha(tipo), triangulo_destino, triangulo_origen, self.tablero.tablero
        )
        if se_pasa:
            return False
        if movimiento_justo_para_ganar and puede_liberar:
            return True
        if movimiento_justo_para_ganar and not puede_liberar:
            return False
        no_hay_fichas_rivales = (
            not self.tablero.validador.triangulo_con_fichas_rivales(
                self.tablero.tablero, triangulo_destino, Ficha(tipo)
            )
        )
        if no_hay_fichas_rivales:
            return True