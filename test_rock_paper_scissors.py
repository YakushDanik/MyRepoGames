import unittest
from unittest.mock import MagicMock
from tkinter import Tk, Button
from rock_paper_scissors import RockPaperScissors

class TestRockPaperScissors(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Tk()
        self.root.withdraw()  # Скрыть основное окно Tkinter
        self.switch_frame_mock = MagicMock()
        self.game = RockPaperScissors(self.root, self.switch_frame_mock)

    def test_element_selection(self) -> None:
        self.assertEqual(self.game.turns, 0)
        self.game.element_selection("ROCK")
        self.assertEqual(self.game.turns, 1)
        self.assertEqual(self.game.p1_choice, "ROCK")
        self.game.element_selection("PAPER")
        self.assertEqual(self.game.p2_choice, "PAPER")

    def test_game_manage(self) -> None:
        self.game.element_selection("ROCK")
        self.game.element_selection("PAPER")
        self.game.game_manage()
        self.assertEqual(self.game.p1_score, 0)
        self.assertEqual(self.game.p2_score, 1)
        self.assertEqual(self.game.score_label["text"], "SCORE:0-1")

    def test_score_restart(self) -> None:
        self.game.element_selection("ROCK")
        self.game.element_selection("PAPER")
        self.assertEqual(self.game.p1_score, 0)
        self.assertEqual(self.game.p2_score, 1)
        self.assertEqual(self.game.score_label["text"], "SCORE:0-1")        
        self.game.score_restart()
        self.assertEqual(self.game.p1_score, 0)
        self.assertEqual(self.game.p2_score, 0)
        self.assertEqual(self.game.score_label["text"], "SCORE:0-0") 

    def test_back_to_menu(self) -> None:
        self.game.p1_score = 1
        self.game.p2_score = 2
        self.game.back_to_menu()
        self.assertEqual(self.game.p1_score, 0)
        self.assertEqual(self.game.p2_score, 0)
        self.switch_frame_mock.assert_called_with("main_menu")


if __name__ == '__main__':
    unittest.main()

