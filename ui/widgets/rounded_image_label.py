from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtCore import Qt

from utils.path import resource_path


class RoundedImageLabel(QLabel):
    def __init__(self, image_path=None, radius=20):
        super().__init__()

        self.radius = radius

        if image_path:
            self.set_image(image_path)

    def set_image(self, image_path, width=None, height=None):
        self.setPixmap(
            self.create_rounded_pixmap(
                image_path,
                self.radius,
                width,
                height
            )
        )

    def create_rounded_pixmap(self, image_path, radius, width=None, height=None):
        pixmap = QPixmap(resource_path(image_path))

        if width and height:
            pixmap = pixmap.scaled(
                width,
                height,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

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
