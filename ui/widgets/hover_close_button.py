from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel
from PySide6.QtCore import Qt, QPropertyAnimation, QPoint
from PySide6.QtGui import QPixmap


class HoverCloseButton(QPushButton):
    def __init__(self, title_bar):
        super().__init__("X")
        self.title_bar = title_bar

    def enterEvent(self, event):
        self.title_bar.show_image()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.title_bar.hide_image()
        super().leaveEvent(event)