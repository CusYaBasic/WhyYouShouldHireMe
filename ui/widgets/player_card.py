from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize

from utils.path import resource_path


class PlayerCard(QPushButton):

    def __init__(self, name, image):
        super().__init__()

        self.name = name
        self.setFixedSize(
            150,
            150
        )
        pixmap = QPixmap(resource_path(image))
        self.setIcon(
            QIcon(pixmap)
        )
        self.setIconSize(
            QSize(80, 80)
        )
        self.setText(
            name
        )
        self.setStyleSheet("""
            QPushButton {
                background: #202020;
                color: white;
                border-radius: 15px;
                font-size: 18px;
                border: 3px solid transparent;
            }
            QPushButton:hover {
                border: 3px solid white;
            }
            QPushButton:pressed {
                border: 3px solid #aaaaaa;
            }
        """)