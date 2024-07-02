import unittest
from unittest.mock import MagicMock
from tkinter import Tk, Button
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.root.withdraw()  # Скрыть основное окно Tkinter
        self.switch_frame_mock = MagicMock()
        self.game = TicTacToe(self.root, self.switch_frame_mock)

    def tearDown(self):
        self.root.destroy()

    def test_initial_state(self):
        self.assertEqual(self.game.turns, 1)
        self.assertEqual(self.game.rows, [0, 0, 0])
        self.assertEqual(self.game.columns, [0, 0, 0])
        self.assertEqual(self.game.diag1, 0)
        self.assertEqual(self.game.diag2, 0)
        self.assertEqual(self.game.o_score, 0)
        self.assertEqual(self.game.x_score, 0)
        self.assertEqual(self.game.score_label["text"], "SCORE:0-0")

    def test_button_on_click(self):
        self.game.button_on_click(0, 0)
        self.assertEqual(self.game.game_buttons[0, 0]["text"], "X")
        self.assertEqual(self.game.turns, 2)
        self.game.button_on_click(0, 1)
        self.assertEqual(self.game.game_buttons[0, 1]["text"], "O")

    def test_win(self) -> None:
        self.game.button_on_click(0, 0)
        self.game.button_on_click(1, 0)
        self.game.button_on_click(0, 1)
        self.game.button_on_click(1, 1)
        self.game.button_on_click(0, 2)
        self.game.game_manage(0, 2)
        self.assertEqual(self.game.score_label["text"], "SCORE:1-0")
        self.assertEqual(self.game.x_score, 1)

    def test_draw(self) -> None:
        for i in range(0, 2):
            for j in range(0, 2):
                self.game.button_on_click(i , j)
        self.game.game_manage(2, 2)
        self.assertEqual(self.game.score_label["text"], "SCORE:0-0")
        self.assertEqual(self.game.x_score, 0)
        self.assertEqual(self.game.o_score, 0)

    def test_score_restart(self) -> None:
        self.game.button_on_click(0, 0)
        self.game.button_on_click(1, 0)
        self.game.button_on_click(0, 1)
        self.game.button_on_click(1, 1)
        self.game.button_on_click(0, 2)
        self.game.game_manage(0, 2)
        self.assertEqual(self.game.x_score, 1)
        self.game.score_restart()
        self.assertEqual(self.game.x_score, 0)

    def test_back_to_menu(self) -> None:
        self.game.button_on_click(0, 0)
        self.game.button_on_click(1, 0)
        self.game.button_on_click(0, 1)
        self.game.button_on_click(1, 1)
        self.game.button_on_click(0, 2)
        self.game.game_manage(0, 2)
        self.assertEqual(self.game.game_buttons[0, 0]["text"], "X")
        self.game.back_to_menu()
        self.switch_frame_mock.assert_called_with("main_menu")
        self.assertEqual(self.game.game_buttons[0, 0]["text"], "")
        self.assertEqual(self.game.turns, 1)
        self.assertEqual(self.game.x_score, 0)
        self.assertEqual(self.game.o_score, 0)
        self.assertEqual(self.game.score_label["text"], "SCORE:0-0")
        


if __name__ == '__main__':
    unittest.main()