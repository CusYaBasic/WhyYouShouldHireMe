from PySide6.QtWidgets import QPushButton, QSizePolicy

class RoundedButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)

        self.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed
        )

        self.setStyleSheet("""
            QPushButton {
                background-color: #2b2b2b;
                color: white;
                border-radius: 15px;
                padding: 10px 20px;
            }

            QPushButton:hover {
                background-color: #444444;
            }

            QPushButton:pressed {
                background-color: #222222;
            }
        """)