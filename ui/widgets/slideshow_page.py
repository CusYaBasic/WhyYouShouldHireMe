from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal

class SlideshowPage(QWidget):

    finished = Signal()

    def __init__(self, slides):
        super().__init__()

        self.slides = slides
        self.current_index = 0

        self.image = QLabel()
        self.image.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.title = QLabel()
        self.title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: white;
        """)

        self.description = QLabel()
        self.description.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.description.setWordWrap(True)
        self.description.setStyleSheet("""
            font-size: 18px;
            color: white;
        """)

        self.previous_button = QPushButton(
            "◀ Previous"
        )
        self.next_button = QPushButton(
            "Next ▶"
        )

        self.previous_button.clicked.connect(
            self.previous_slide
        )
        self.next_button.clicked.connect(
            self.next_slide
        )

        button_layout = QHBoxLayout()
        button_layout.addWidget(
            self.previous_button
        )
        button_layout.addWidget(
            self.next_button
        )

        layout = QVBoxLayout(self)
        layout.setSpacing(5)
        layout.setContentsMargins(
            20,
            20,
            20,
            20
        )
        layout.addWidget(
            self.image
        )
        layout.addWidget(
            self.title
        )
        layout.addWidget(
            self.description
        )
        layout.addLayout(
            button_layout
        )

        self.update_slide()

    def update_slide(self):
        slide = self.slides[
            self.current_index
        ]

        pixmap = QPixmap(
            slide["image"]
        )
        self.image.setPixmap(
            pixmap.scaled(
                400,
                250,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        self.title.setText(
            slide["title"]
        )
        self.description.setText(
            slide["text"]
        )

    def next_slide(self):
        self.current_index += 1

        if self.current_index >= len(self.slides):
            self.finished.emit()
            self.current_index = 0
            return

        self.update_slide()

    def previous_slide(self):
        self.current_index -= 1

        if self.current_index < 0:
            self.current_index = len(self.slides) - 1

        self.update_slide()

    def reset(self):
        self.current_index = 0
        self.update_slide()