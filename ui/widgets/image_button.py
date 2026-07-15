from PySide6.QtWidgets import QPushButton, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from pathlib import Path

class ImageButton(QPushButton):

    def __init__(self, title, image):
        super().__init__()

        self.setFixedSize(250, 180)
        # Click sound
        self.audio_output = QAudioOutput()
        self.click_sound = QMediaPlayer()
        self.click_sound.setAudioOutput(
            self.audio_output
        )
        sound_path = Path(
            "assets/sounds/button_click.mp3"
        ).resolve()
        self.click_sound.setSource(
            QUrl.fromLocalFile(
                str(sound_path)
            )
        )
        self.audio_output.setVolume(0.5)

        # Background image
        self.image = QLabel(self)
        pixmap = QPixmap(image)
        self.image.setPixmap(
            pixmap.scaled(
                51,
                51,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        self.image.setFixedSize(51, 51)
        self.image.move(
            (self.width() - 51) // 2,
            25
        )
        self.image.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )

        # Black text outline
        self.text_outline = QLabel(title, self)
        self.text_outline.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.text_outline.setGeometry(
            0,
            90,
            self.width(),
            40
        )
        self.text_outline.move(2, 92)
        self.text_outline.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 22px;
                font-weight: bold;
            }
        """)

        # Main text
        self.text = QLabel(title, self)
        self.text.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.text.setGeometry(
            10,
            85,
            self.width() - 20,
            60
        )
        self.text.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 22px;
                font-weight: bold;
            }
        """)
        self.text.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )
        self.setStyleSheet("""
            QPushButton {
                border-radius: 15px;
                border: 3px solid transparent;
                background: #341539;
            }
            QPushButton:hover {
                border: 3px solid white;
            }
            QPushButton:pressed {
                border: 3px solid #aaaaaa;
            }
            QPushButton:disabled {
                background: #151515;
                border: 3px solid #222222;
            }
        """)


    def mousePressEvent(self, event):
        self.click_sound.stop()
        self.click_sound.play()

        super().mousePressEvent(event)