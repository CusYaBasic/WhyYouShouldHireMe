import os
import tempfile
import unittest

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QApplication

from ui.widgets.slideshow_page import SlideshowPage


app = QApplication.instance() or QApplication([])


class SlideshowPageTests(unittest.TestCase):
    def test_slideshow_uses_compact_dark_presentation_panel(self):
        image = QImage(640, 360, QImage.Format.Format_ARGB32)
        image.fill(Qt.GlobalColor.blue)

        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = os.path.join(temp_dir, "slide.png")
            self.assertTrue(image.save(image_path))

            page = SlideshowPage([
                {
                    "image": image_path,
                    "title": "Professional Slide",
                    "text": "A compact description that should sit close to the title."
                }
            ])
            page.resize(1280, 672)
            page.show()
            app.processEvents()

            self.assertEqual(
                page.content_panel.objectName(),
                "slideshowPanel"
            )
            self.assertLessEqual(
                page.content_layout.spacing(),
                14
            )
            self.assertLessEqual(
                page.description.geometry().top() - page.title.geometry().bottom(),
                20
            )
            self.assertEqual(
                page.slide_counter.text(),
                "1 / 1"
            )
            self.assertIn(
                "background-color: #111820",
                page.content_panel.styleSheet()
            )

    def test_slideshow_paints_dark_page_background(self):
        image = QImage(640, 360, QImage.Format.Format_ARGB32)
        image.fill(Qt.GlobalColor.blue)

        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = os.path.join(temp_dir, "slide.png")
            self.assertTrue(image.save(image_path))

            page = SlideshowPage([
                {
                    "image": image_path,
                    "title": "Professional Slide",
                    "text": "The background outside the panel should be dark."
                }
            ])

            self.assertTrue(
                page.testAttribute(Qt.WidgetAttribute.WA_StyledBackground)
            )


if __name__ == "__main__":
    unittest.main()
