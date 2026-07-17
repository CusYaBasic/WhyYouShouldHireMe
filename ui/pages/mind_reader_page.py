from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QPropertyAnimation, QPoint, Signal

from utils.path import resource_path


MENU_PURPLE = "#341539"
MENU_PURPLE_BORDER = "#7c4b87"
MENU_PURPLE_HOVER = "#4a2053"
MENU_PURPLE_PRESSED = "#241029"


class MindReaderPage(QWidget):

    back_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.setObjectName("mindReaderPage")
        self.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground,
            True
        )
        self.setStyleSheet("""
            #mindReaderPage {
                background-color: #080c12;
            }
        """)

        layout = QVBoxLayout(
            self
        )
        layout.setContentsMargins(
            48,
            30,
            48,
            30
        )
        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.content_panel = QWidget()
        self.content_panel.setObjectName("mindReaderPanel")
        self.content_panel.setMaximumWidth(
            560
        )
        self.content_panel.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Fixed
        )
        self.content_panel.setStyleSheet("""
            #mindReaderPanel {
                background-color: #111820;
                border: 1px solid #263241;
                border-radius: 18px;
            }
        """)

        content_layout = QVBoxLayout(
            self.content_panel
        )
        content_layout.setContentsMargins(
            38,
            34,
            38,
            32
        )
        content_layout.setSpacing(
            14
        )

        title = QLabel(
            "Mind Reader"
        )
        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        title.setStyleSheet("""
            color: #f5f7fb;
            font-size: 32px;
            font-weight: bold;
        """)
        self.message = QLabel(
            "Think of a number between 1 and 100..."
        )
        self.message.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.message.setStyleSheet("""
            color: #c8d0dc;
            font-size: 17px;
        """)

        self.input = QLineEdit()
        self.input.setFixedWidth(
            260
        )
        self.input.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.input.setPlaceholderText(
            "Enter your number"
        )
        self.input.setStyleSheet(f"""
            QLineEdit {{
                background-color: #0b1118;
                color: #f5f7fb;
                border: 1px solid #334255;
                border-radius: 10px;
                padding: 10px 14px;
                font-size: 16px;
            }}
            QLineEdit:focus {{
                border-color: {MENU_PURPLE_BORDER};
            }}
        """)

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
        self.result.setMinimumHeight(
            38
        )
        self.result.setWordWrap(
            True
        )
        self.result.setStyleSheet("""
            color: #f2d98f;
            font-size: 18px;
            font-weight: bold;
        """)

        primary_button_style = f"""
            QPushButton {{
                background-color: {MENU_PURPLE};
                color: #f5f7fb;
                border: 1px solid {MENU_PURPLE_BORDER};
                border-radius: 10px;
                padding: 10px 22px;
                font-size: 15px;
                font-weight: bold;
                min-width: 160px;
            }}
            QPushButton:hover {{
                background-color: {MENU_PURPLE_HOVER};
            }}
            QPushButton:pressed {{
                background-color: {MENU_PURPLE_PRESSED};
            }}
        """
        secondary_button_style = """
            QPushButton {
                background-color: #1d2733;
                color: #f5f7fb;
                border: 1px solid #334255;
                border-radius: 10px;
                padding: 10px 22px;
                font-size: 15px;
                font-weight: bold;
                min-width: 160px;
            }
            QPushButton:hover {
                background-color: #263447;
                border-color: #4a5f7a;
            }
            QPushButton:pressed {
                background-color: #141c26;
            }
        """
        self.guess_button.setStyleSheet(
            primary_button_style
        )
        self.back_button.setStyleSheet(
            secondary_button_style
        )

        content_layout.addWidget(title)
        content_layout.addWidget(self.message)
        content_layout.addWidget(
            self.input,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        content_layout.addWidget(
            self.guess_button,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        content_layout.addWidget(self.result)
        content_layout.addWidget(
            self.back_button,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        layout.addWidget(
            self.content_panel,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.reveal_image = QLabel(
            self
        )
        pixmap = QPixmap(
            resource_path("assets/images/memes/troll.png")
        )
        self.reveal_image.setPixmap(
            pixmap.scaled(
                250,
                250,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        self.reveal_image.setFixedSize(
            250,
            250
        )
        self.reveal_image.move(
            -300,
            150
        )
        self.reveal_image.hide()

        self.animation = QPropertyAnimation(
            self.reveal_image,
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
            f"Were you thinking of {number}?"
        )

        self.show_reveal_image()

    def show_reveal_image(self):

        reveal_y = self.reveal_image_y()

        self.reveal_image.show()
        self.animation.stop()
        self.animation.setStartValue(
            QPoint(
                -300,
                reveal_y
            )
        )

        self.animation.setEndValue(
            QPoint(
                500,
                reveal_y
            )
        )

        self.animation.start()

    def reveal_image_y(self):
        button_bottom = self.back_button.mapTo(
            self,
            QPoint(0, self.back_button.height())
        ).y()

        return max(
            button_bottom + 12,
            520
        )

    def reset(self):
        self.input.clear()
        self.result.clear()
        self.reveal_image.hide()
        self.reveal_image.move(
            self.width(),
            self.reveal_image_y()
        )
