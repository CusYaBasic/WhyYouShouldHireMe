import unittest

from PySide6.QtWidgets import QApplication

from ui.pages.mini_game_page import GameWidget


app = QApplication.instance() or QApplication([])


class FakeGameParent:
    def __init__(self):
        self.score = 0

    def game_over(self):
        pass


class MiniGamePageTests(unittest.TestCase):
    def test_game_widget_shows_muted_controls_label_below_score(self):
        game = GameWidget(FakeGameParent())
        self.addCleanup(game.timer.stop)
        self.addCleanup(game.deleteLater)

        self.assertEqual(
            game.controls_label.text(),
            "Controls: A / D or Left / Right to move"
        )
        self.assertGreater(
            game.controls_label.y(),
            game.score_label.y()
        )
        self.assertIn(
            "color: #555555",
            game.controls_label.styleSheet()
        )


if __name__ == "__main__":
    unittest.main()
