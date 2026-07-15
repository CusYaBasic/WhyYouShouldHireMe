from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtCore import Signal

from ui.widgets.image_button import ImageButton


class SectionsPage(QWidget):

    home_clicked = Signal()
    open_page = Signal(str)

    def __init__(self):
        super().__init__()

        layout = QGridLayout(self)

        sections = [
            ("Home", "assets/images/sections/home.png"),
            ("Why Hire Me", "assets/images/sections/hire.png"),
            ("Strengths", "assets/images/sections/strengths.png"),
            ("Weaknesses", "assets/images/sections/weaknesses.png"),
            ("Mini Game", "assets/images/sections/game.png"),
            ("Previous Work", "assets/images/sections/work.png"),
            ("Programming\nPrinciples", "assets/images/sections/code.png"),
            ("Inventory Demo", "assets/images/sections/inventory.png"),
            ("Mind Reader", "assets/images/sections/mind.png"),
        ]

        row = 0
        col = 0

        for title, image in sections:
            button = ImageButton(
                title,
                image
            )

            # Only change the Home button behaviour
            if title == "Home":
                button.clicked.connect(
                    self.home_clicked.emit
                )
            elif title == "Why Hire Me":
                button.clicked.connect(
                    lambda checked=False:
                    self.open_page.emit("why_hire_page")
                )
            elif title == "Strengths":
                button.clicked.connect(
                    lambda checked=False:
                    self.open_page.emit("strengths_page")
                )
            elif title == "Weaknesses":
                button.clicked.connect(
                    lambda checked=False:
                    self.open_page.emit("weaknesses_page")
                )
            elif title == "Mini Game":
                button.clicked.connect(
                    lambda checked=False:
                    self.open_page.emit("mini_game_page")
                )
            elif title == "Previous Work":
                button.clicked.connect(
                    lambda checked=False:
                    self.open_page.emit("previous_work_page")
                )
            elif title == "Programming\nPrinciples":
                button.clicked.connect(
                    lambda checked=False:
                    self.open_page.emit("programming_principles_page")
                )
            elif title == "Inventory Demo":
                button.clicked.connect(
                    lambda checked=False:
                    self.open_page.emit("inventory_page")
                )
            elif title == "Mind Reader":
                button.clicked.connect(
                    lambda checked=False:
                    self.open_page.emit("mind_reader_page")
                )

            layout.addWidget(
                button,
                row,
                col
            )

            col += 1

            if col == 3:
                col = 0
                row += 1