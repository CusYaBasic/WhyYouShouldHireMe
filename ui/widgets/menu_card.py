from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl

from utils.path import resource_path


class MenuCard(QWidget):

    clicked = Signal()

    def __init__(self, title, description, image):
        super().__init__()

        self.setFixedSize(250, 250)
        self.image = QLabel()
        pixmap = QPixmap(resource_path(image))
        self.image.setPixmap(
            pixmap.scaled(
                100,
                100
            )
        )
        self.image.setFixedHeight(110)
        self.title = QLabel(title)
        self.description = QLabel(description)
        self.title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            color: white;
        """)
        self.description.setStyleSheet("""
            color: #bbbbbb;
        """)
        layout = QVBoxLayout(self)

        layout.addWidget(self.image)
        layout.addWidget(self.title)
        layout.addWidget(self.description)

        # Click sound
        self.audio_output = QAudioOutput()
        self.click_sound = QMediaPlayer()
        self.click_sound.setAudioOutput(
            self.audio_output
        )
        self.click_sound.setSource(
            QUrl.fromLocalFile(
                "assets/sounds/button_click.mp3"
            )
        )
        print(self.click_sound.source())
        self.audio_output.setVolume(0.5)

        self.setStyleSheet("""
            QWidget {
                background: #202020;
                border-radius: 15px;
            }
            QWidget:hover {
                background: #303030;
            }
        """)

    def mousePressEvent(self, event):
        self.click_sound.stop()
        self.click_sound.play()
        self.clicked.emit()

        super().mousePressEvent(event)