from PySide6.QtCore import Qt, Signal

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

from ui.widgets.rounded_image_label import RoundedImageLabel
from ui.widgets.rounded_button import RoundedButton


class HomePage(QWidget):

    hire_clicked = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        tcg_icon = RoundedImageLabel(
            "assets/images/logos/tcgroup.jpg",
            30
        )

        tcg_icon.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title = QLabel("Why You Should Hire Me")
        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        subtitle = QLabel(
            "A completely unnecessary Python application."
        )

        subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.hire_button = RoundedButton(
            "Why Hire Me?"
        )

        self.hire_button.clicked.connect(
            self.on_hire_clicked
        )

        layout.addStretch()

        layout.setSpacing(20)

        layout.addWidget(tcg_icon)
        layout.addWidget(title)
        layout.addWidget(subtitle)

        layout.addWidget(
            self.hire_button,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )

        layout.addStretch()


    def on_hire_clicked(self):
        self.hire_clicked.emit()