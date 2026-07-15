from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt

from utils.path import resource_path


class RoundedImageLabel(QLabel):
    def __init__(self, image_path, radius=20):
        super().__init__()

        self.setPixmap(
            self.create_rounded_pixmap(image_path, radius)
        )

    def create_rounded_pixmap(self, image_path, radius):
        pixmap = QPixmap(resource_path(image_path))
        rounded = QPixmap(pixmap.size())
        rounded.fill(Qt.GlobalColor.transparent)
        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        clip = QPainterPath()
        clip.addRoundedRect(
            0,
            0,
            pixmap.width(),
            pixmap.height(),
            radius,
            radius
        )

        painter.setClipPath(clip)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        return rounded