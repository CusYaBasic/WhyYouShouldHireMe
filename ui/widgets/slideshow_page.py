from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy
)
from PySide6.QtCore import Qt, Signal

from ui.widgets.rounded_image_label import RoundedImageLabel


class SlideshowPage(QWidget):

    finished = Signal()

    def __init__(self, slides):
        super().__init__()

        self.setObjectName("slideshowPage")
        self.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground,
            True
        )
        self.setStyleSheet("""
            #slideshowPage {
                background-color: #080c12;
            }
        """)

        self.slides = slides
        self.current_index = 0

        self.content_panel = QWidget()
        self.content_panel.setObjectName("slideshowPanel")
        self.content_panel.setMaximumWidth(760)
        self.content_panel.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Fixed
        )
        self.content_panel.setStyleSheet("""
            #slideshowPanel {
                background-color: #111820;
                border: 1px solid #263241;
                border-radius: 18px;
            }
        """)

        self.image = RoundedImageLabel(radius=20)
        self.image.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.title = QLabel()
        self.title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.title.setStyleSheet("""
            font-size: 30px;
            font-weight: bold;
            color: #f5f7fb;
        """)

        self.description = QLabel()
        self.description.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.description.setWordWrap(True)
        self.description.setMaximumWidth(660)
        self.description.setStyleSheet("""
            font-size: 18px;
            line-height: 1.35;
            color: #c8d0dc;
        """)

        self.previous_button = QPushButton(
            "Previous"
        )
        self.next_button = QPushButton(
            "Next"
        )
        self.slide_counter = QLabel()
        self.slide_counter.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.slide_counter.setStyleSheet("""
            color: #91a0b5;
            font-size: 14px;
            font-weight: bold;
        """)

        button_style = """
            QPushButton {
                background-color: #1d2733;
                color: #f5f7fb;
                border: 1px solid #334255;
                border-radius: 10px;
                padding: 10px 22px;
                font-size: 15px;
                font-weight: bold;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #263447;
                border-color: #4a5f7a;
            }
            QPushButton:pressed {
                background-color: #141c26;
            }
        """
        self.previous_button.setStyleSheet(
            button_style
        )
        self.next_button.setStyleSheet(
            button_style
        )

        self.previous_button.clicked.connect(
            self.previous_slide
        )
        self.next_button.clicked.connect(
            self.next_slide
        )

        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(
            0,
            8,
            0,
            0
        )
        button_layout.setSpacing(18)
        button_layout.addWidget(
            self.previous_button
        )
        button_layout.addStretch()
        button_layout.addWidget(
            self.slide_counter
        )
        button_layout.addStretch()
        button_layout.addWidget(
            self.next_button
        )

        self.content_layout = QVBoxLayout(
            self.content_panel
        )
        self.content_layout.setSpacing(10)
        self.content_layout.setContentsMargins(
            34,
            28,
            34,
            26
        )
        self.content_layout.addWidget(
            self.image
        )
        self.content_layout.addWidget(
            self.title
        )
        self.content_layout.addWidget(
            self.description,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )
        self.content_layout.addLayout(
            button_layout
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(
            48,
            30,
            48,
            30
        )
        layout.addStretch()
        layout.addWidget(
            self.content_panel,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        layout.addStretch()

        self.update_slide()

    def update_slide(self):
        slide = self.slides[
            self.current_index
        ]

        self.image.set_image(
            slide["image"],
            560,
            300
        )

        self.title.setText(
            slide["title"]
        )
        self.description.setText(
            slide["text"]
        )
        self.slide_counter.setText(
            f"{self.current_index + 1} / {len(self.slides)}"
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
