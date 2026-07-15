from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QPushButton
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QPropertyAnimation, QPoint, Signal

from utils.path import resource_path


class MindReaderPage(QWidget):

    back_clicked = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(
            self
        )
        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        title = QLabel(
            "Mind Reader"
        )
        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        title.setStyleSheet("""
            color:white;
            font-size:30px;
            font-weight:bold;
        """)
        self.message = QLabel(
            "Think of a number between 1 and 100..."
        )
        self.message.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.input = QLineEdit()
        self.input.setFixedWidth(
            200
        )
        self.input.setPlaceholderText(
            "Enter your number"
        )
        self.guess_button = QPushButton(
            "Guess"
        )
        self.guess_button.clicked.connect(
            self.guess
        )
        self.back_button = QPushButton(
            "Back to Menu"
        )
        self.back_button.clicked.connect(
            self.back_clicked.emit
        )

        self.result = QLabel()
        self.result.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(title)
        layout.addWidget(self.message)
        layout.addWidget(self.input)
        layout.addWidget(self.guess_button)
        layout.addWidget(self.result)
        layout.addWidget(self.back_button)

        # Troll image
        self.troll = QLabel(
            self
        )

        pixmap = QPixmap(resource_path("assets/images/memes/troll.png"
        ))


        self.troll.setPixmap(
            pixmap.scaled(
                250,
                250,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        self.troll.setFixedSize(
            250,
            250
        )

        # Start off screen
        self.troll.move(
            -300,
            150
        )

        self.troll.hide()

        self.animation = QPropertyAnimation(
            self.troll,
            b"pos"
        )

        self.animation.setDuration(
            500
        )

    def guess(self):

        number = self.input.text()

        if not number.isdigit():
            self.result.setText(
                "Nice try... enter an actual number"
            )
            return

        self.result.setText(
            f"I knew you were thinking of {number} 😈"
        )

        self.show_troll()

    def show_troll(self):

        self.troll.show()
        self.animation.stop()
        self.animation.setStartValue(
            QPoint(
                -300,
                450
            )
        )

        self.animation.setEndValue(
            QPoint(
                500,
                450
            )
        )

        self.animation.start()

    def reset(self):
        self.input.clear()
        self.result.clear()
        self.troll.hide()
        self.troll.move(
            self.width(),
            250
        )