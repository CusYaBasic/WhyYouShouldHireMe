import unittest

from PySide6.QtCore import QPoint, Qt
from PySide6.QtWidgets import QApplication

from ui.pages.mind_reader_page import MindReaderPage


app = QApplication.instance() or QApplication([])


class MindReaderPageTests(unittest.TestCase):
    def test_guess_uses_question_copy(self):
        page = MindReaderPage()
        page.input.setText("42")

        page.guess()

        self.assertEqual(
            page.result.text(),
            "Were you thinking of 42?"
        )

    def test_page_uses_dark_card_layout(self):
        page = MindReaderPage()

        self.assertEqual(
            page.content_panel.objectName(),
            "mindReaderPanel"
        )
        self.assertTrue(
            page.testAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        )
        self.assertIn(
            "background-color: #111820",
            page.content_panel.styleSheet()
        )

    def test_page_uses_main_menu_purple_accent(self):
        page = MindReaderPage()

        self.assertIn(
            "background-color: #341539",
            page.guess_button.styleSheet()
        )
        self.assertIn(
            "#7c4b87",
            page.guess_button.styleSheet()
        )
        self.assertIn(
            "#7c4b87",
            page.input.styleSheet()
        )

    def test_reveal_image_animates_below_back_button(self):
        page = MindReaderPage()
        page.resize(1280, 720)
        page.show()
        app.processEvents()

        page.input.setText("42")
        page.guess()
        app.processEvents()

        button_bottom = page.back_button.mapTo(
            page,
            QPoint(0, page.back_button.height())
        ).y()

        self.assertGreaterEqual(
            page.animation.endValue().y(),
            button_bottom + 12
        )
        page.close()


if __name__ == "__main__":
    unittest.main()
