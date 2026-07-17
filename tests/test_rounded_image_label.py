import os
import tempfile
import unittest

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage
from PySide6.QtWidgets import QApplication

from ui.widgets.rounded_image_label import RoundedImageLabel


app = QApplication.instance() or QApplication([])


class RoundedImageLabelTests(unittest.TestCase):
    def test_set_image_scales_and_rounds_pixmap(self):
        image = QImage(100, 100, QImage.Format.Format_ARGB32)
        image.fill(Qt.GlobalColor.red)

        with tempfile.TemporaryDirectory() as temp_dir:
            image_path = os.path.join(temp_dir, "slide.png")
            self.assertTrue(image.save(image_path))

            label = RoundedImageLabel(radius=12)
            label.set_image(image_path, 80, 50)

            pixmap = label.pixmap()

            self.assertIsNotNone(pixmap)
            self.assertLessEqual(pixmap.width(), 80)
            self.assertLessEqual(pixmap.height(), 50)
            self.assertEqual(
                pixmap.toImage().pixelColor(0, 0).alpha(),
                0
            )


if __name__ == "__main__":
    unittest.main()
