from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel
from PySide6.QtCore import Qt, QPropertyAnimation, QPoint, QUrl
from ui.widgets.hover_close_button import HoverCloseButton
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
import random
from PySide6.QtCore import QEasingCurve


class TitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent

        self.setFixedHeight(40)

        self.title = QLabel("Why You Should Hire Me")

        # Image belongs to the main window, not the title bar
        self.jesus_image = QLabel(self.parent)

        pixmap = QPixmap("assets/images/memes/jesus.png")

        if pixmap.isNull():
            print("Failed to load Jesus image")

        self.jesus_image.setPixmap(
            pixmap.scaled(
                207,
                301,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        self.jesus_image.setFixedSize(207, 301)

        # Jesus sound
        self.audio_output = QAudioOutput()

        self.jesus_sound = QMediaPlayer()
        self.jesus_sound.setAudioOutput(
            self.audio_output
        )

        self.jesus_sound.setSource(
            QUrl.fromLocalFile(
                "assets/sounds/moving-stone.mp3"
            )
        )

        self.audio_output.setVolume(0.5)

        self.jesus_message = QLabel(self.parent)

        self.phrases = [
            "Please no...",
            "Jesus doesn't approve",
            "Jesus is watching",
            "Think about what you're doing",
            "Do you really want this?",
            "The button of sin has been hovered",
            "Jesus saw that..."
        ]

        self.jesus_message.setStyleSheet("""
            QLabel {
                color: white;
                background: #202020;
                border-radius: 10px;
                padding: 8px;
                font-size: 16px;
            }
        """)

        self.jesus_message.hide()

        # Start off screen
        self.jesus_image.move(
            -self.jesus_image.width(),
            200
        )

        #self.jesus_image.hide()

        self.jesus_animation = QPropertyAnimation(
            self.jesus_image,
            b"pos"
        )

        self.message_animation = QPropertyAnimation(
            self.jesus_message,
            b"pos"
        )

        self.message_animation.setDuration(1200)

        self.jesus_animation.setDuration(1200)

        self.close_button = HoverCloseButton(self)
        self.close_button.setFixedSize(40, 30)

        self.close_button.clicked.connect(self.close_window)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 10, 0)

        layout.addWidget(self.title)
        layout.addStretch()
        layout.addWidget(self.close_button)

        self.setStyleSheet("""
            QWidget {
                background: #202020;
            }

            QLabel {
                color: white;
            }

            QPushButton {
                color: white;
                background: transparent;
                border: none;
                font-size: 16px;
            }

            QPushButton:hover {
                background: #e81123;
                border-radius: 5px;
            }

            QPushButton:pressed {
                background: #a00000;
            }
        """)


    def close_window(self):
        self.parent.close()

    def show_image(self):
        self.jesus_animation.stop()
        self.message_animation.stop()

        phrase = random.choice(self.phrases)
        self.jesus_message.setText(phrase)
        self.jesus_message.adjustSize()

        self.jesus_image.show()
        self.jesus_message.show()

        self.jesus_sound.stop()
        self.jesus_sound.play()

        self.jesus_animation.stop()
        self.message_animation.stop()

        self.jesus_image.raise_()
        self.jesus_message.raise_()

        # Jesus
        self.jesus_animation.setStartValue(
            QPoint(-self.jesus_image.width(), 200)
        )

        self.jesus_animation.setEndValue(
            QPoint(0, 200)
        )

        # Text bubble
        self.message_animation.setStartValue(
            QPoint(-300, 250)
        )

        self.message_animation.setEndValue(
            QPoint(75, 280)
        )

        self.jesus_animation.start()
        self.message_animation.start()

    def hide_image(self):
        self.jesus_animation.stop()
        self.message_animation.stop()

        self.jesus_sound.stop()

        self.jesus_animation.stop()
        self.message_animation.stop()

        self.jesus_animation.setStartValue(
            self.jesus_image.pos()
        )

        self.jesus_animation.setEndValue(
            QPoint(-self.jesus_image.width(), 200)
        )

        self.message_animation.setStartValue(
            self.jesus_message.pos()
        )

        self.message_animation.setEndValue(
            QPoint(-300, 250)
        )

        self.jesus_animation.start()
        self.message_animation.start()