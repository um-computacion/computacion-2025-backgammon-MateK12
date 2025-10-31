from src.core.interfaces.EstrategiasPuedeMover import IEstrategiaPuedeMover
from src.core.interfaces.EstrategiaMovible import IEstrategiaMovible
from src.core.models.ficha.Ficha import Ficha
from src.core.enums.TipoFicha import TipoFicha
# pylint: disable=C0303

class EstrategiaUnicaFicha(IEstrategiaMovible, IEstrategiaPuedeMover):
    """Regla: si solo UNA ficha puede moverse con UN dado (no ambos), usa el dado MAYOR"""
    
    def puede_mover(self, tipo: int, dados: list[int], tablero, backgammon) -> bool:
        '''Verifica si solo una ficha puede moverse con un dado (no ambos)
        y si es asi, retorna True para que se use la estrategia y mueva con el dado mayor.
        Parametros:
            tipo (int): Tipo de ficha del jugador que quiere mover
            dados (list[int]): Lista con los valores de los dados
            tablero: El tablero de juego
            backgammon: La instancia del juego de backgammon para realizar movimientos
            Retorna: True si se puede mover con la estrategia, False en caso contrario'''
        
        if backgammon.hay_fichas_comidas():
            return False

        if len(dados) != 2:
            return False
        
        dado1, dado2 = dados[0], dados[1]
        suma_dados = dado1 + dado2
        
        if dado1 == dado2:
            return False
        if self._puede_mover_con_suma(tipo, suma_dados, tablero):
            return False
        resultado = self._chequear_regla(tipo, dados, tablero,backgammon)
        return resultado
    
    def ejecutar(self,dados,triangulo_origen, backgammon) -> None:
        """Ejecuta el movimiento con el dado mayor
        Parametros:
            dados (list[int]): Lista con los valores de los dados
            triangulo_origen (int): Triángulo desde donde se moverá la ficha
            backgammon: La instancia del juego de backgammon para realizar movimientos
        """
        dado_mayor = max(dados)
        backgammon.mover_ficha(triangulo_origen, dado_mayor)
    
    def _chequear_regla(self, tipo: int, dados: list[int], tablero, backgammon) -> bool:
        """Verifica si cumple la regla de única ficha movible
        Parametros:
            tipo (int): Tipo de ficha del jugador que quiere mover
            dados (list[int]): Lista con los valores de los dados
            tablero: El tablero de juego
            backgammon: La instancia del juego de backgammon para realizar movimientos
            Retorna: True si se cumple la regla, False en caso contrario"""
        dado1, dado2 = dados[0], dados[1]

        triangulos_dado1 = self._obtener_triangulos_validos(tipo, dado1, tablero)
        triangulos_dado2 = self._obtener_triangulos_validos(tipo, dado2, tablero)

        if len(triangulos_dado1) == 1 and len(triangulos_dado2) == 1 and triangulos_dado1[0] == triangulos_dado2[0]:
            triangulo_origen = triangulos_dado1[0]
            unico_triangulo = len(tablero.tablero[triangulo_origen])==1
            if not unico_triangulo:
                return False
            self.ejecutar(dados, triangulo_origen, backgammon)
            return True

        return False
    def _puede_mover_con_suma(self, tipo: int, suma_dados: int, tablero) -> bool:
        """Verifica si alguna ficha puede moverse con la suma de los dados
        Parametros:
            tipo (int): Tipo de ficha
            suma_dados (int): Suma de los valores de los dados
            tablero: El tablero de juego
        Retorna:
            bool: True si alguna ficha puede moverse con la suma de los dados, False en"""
        for triangulo in range(24):
            tiene_fichas = [f for f in tablero.tablero[triangulo] if f.tipo == tipo]
            if not tiene_fichas:
                continue
            triangulo_destino = (
                triangulo + suma_dados
                if tipo == TipoFicha.NEGRA.value
                else triangulo - suma_dados
            )
            puede_liberar = tablero.validador.puede_liberar(
                tablero.tablero, Ficha(tipo), tablero.fichas_ganadas
            )
            if self._es_movimiento_ganar(tipo, triangulo_destino, triangulo, tablero):
                if puede_liberar:
                    return True
                else: continue
            
            se_pasa = tablero.validador.se_pasa_del_tablero(
                Ficha(tipo), triangulo_destino, triangulo, tablero.tablero
            )
            if se_pasa:
                continue
            no_hay_rivales = not tablero.validador.triangulo_con_fichas_rivales(
                tablero.tablero, triangulo_destino, Ficha(tipo)
            )
            if no_hay_rivales:
                return True

        return False
    
    def _se_pasa_tablero(self, tipo: int, triangulo_destino: int, triangulo_origen: int, tablero) -> bool:
        '''Verifica si el movimiento se pasa del tablero
            Parametros:
            tipo (int): Tipo de ficha
            triangulo_destino (int): Triángulo destino del movimiento
            triangulo_origen (int): Triángulo origen del movimiento
            tablero: El tablero de juego'''
        return tablero.validador.se_pasa_del_tablero(
            Ficha(tipo), triangulo_destino, triangulo_origen, tablero.tablero
        )
    
    def _es_movimiento_ganar(self, tipo: int, triangulo_destino: int, triangulo_origen: int, tablero) -> bool:
        '''Verifica si el movimiento es para ganar
        Parametros:
            tipo (int): Tipo de ficha
            triangulo_destino (int): Triángulo destino del movimiento
            triangulo_origen (int): Triángulo origen del movimiento
            tablero: El tablero de juego
        '''
        puede_ganar = tablero.validador.puede_ganar(
            Ficha(tipo), triangulo_destino, triangulo_origen
        )
        no_se_pasa = not self._se_pasa_tablero(tipo, triangulo_destino, triangulo_origen, tablero)
        return puede_ganar and no_se_pasa
    

    def _obtener_triangulos_validos(self, tipo: int, movimiento: int, tablero) -> list[int]:
        """Retorna lista de triángulos desde donde se puede mover con el movimiento dado
        Parametros:
            tipo (int): Tipo de ficha
            movimiento (int): Valor del dado
            tablero: El tablero de juego
        Retorna:
            list[int]: Lista de triángulos válidos (puede estar vacía)
        """
        triangulos_validos = []

        for triangulo in range(24):
            # Verificar si hay fichas del tipo en este triángulo
            tiene_fichas = [f for f in tablero.tablero[triangulo] if f.tipo == tipo]
            if not tiene_fichas:
                continue
            
            triangulo_destino = (
                triangulo + movimiento
                if tipo == TipoFicha.NEGRA.value
                else triangulo - movimiento
            )

            # Verificar si se pasa del tablero
            if self._se_pasa_tablero(tipo, triangulo_destino, triangulo, tablero):
                continue
            
            # Verificar si es movimiento para ganar
            if self._es_movimiento_ganar(tipo, triangulo_destino, triangulo, tablero):
                puede_liberar = tablero.validador.puede_liberar(
                    tablero.tablero, Ficha(tipo), tablero.fichas_ganadas
                )
                if puede_liberar:
                    triangulos_validos.append(triangulo)
                continue
            
            # Verificar si hay rivales
            no_hay_rivales = not tablero.validador.triangulo_con_fichas_rivales(
                tablero.tablero, triangulo_destino, Ficha(tipo)
            )
            if no_hay_rivales:
                triangulos_validos.append(triangulo)

        return triangulos_validos