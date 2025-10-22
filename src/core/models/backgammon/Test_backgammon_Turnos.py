import unittest
from unittest.mock import patch
from src.core.models.dado.Dados import Dados
from src.core.models.backgammon.Backgammon_Turnos import Backgammon_Turnos
from src.core.enums.TipoFicha import TipoFicha


class Test_Backgammon_Turnos(unittest.TestCase):
    def setUp(self):
        self.dados = Dados()
        self.turnos = Backgammon_Turnos(self.dados)

    def test_tirar_dados(self):
        with patch("src.core.models.dado.Dados.Dados.tirar_dados") as mock_dados:
            mock_dados.return_value = [3, 5]
            self.turnos.quien_empieza()
            mock_dados.assert_called()

    def test_cambiar_turno(self):
        self.turnos.quien_empieza()
        turno_anterior = self.turnos.turno
        self.turnos.cambiar_turno()
        self.assertNotEqual(self.turnos.turno, turno_anterior)

    def test_quien_empieza_roja_gana(self):
        with patch.object(
            self.turnos, "_Backgammon_Turnos__tirar_dados"
        ) as mock_tirar_dados:
            mock_tirar_dados.return_value = [5, 3]
            self.turnos.quien_empieza()
            self.assertEqual(self.turnos.turno, TipoFicha.ROJA.value)

    def test_quien_empieza_negra_gana(self):
        with patch.object(
            self.turnos, "_Backgammon_Turnos__tirar_dados"
        ) as mock_tirar_dados:
            mock_tirar_dados.return_value = [2, 6]
            self.turnos.quien_empieza()
            self.assertEqual(self.turnos.turno, TipoFicha.NEGRA.value)

    def test_quien_empieza_empate_luego_negra(self):
        with patch.object(
            self.turnos, "_Backgammon_Turnos__tirar_dados"
        ) as mock_tirar_dados:
            mock_tirar_dados.side_effect = [[3, 3], [1, 5]]
            self.turnos.quien_empieza()
            self.assertEqual(self.turnos.turno, TipoFicha.NEGRA.value)
            self.assertEqual(mock_tirar_dados.call_count, 2)


if __name__ == "__main__":
    unittest.main()
