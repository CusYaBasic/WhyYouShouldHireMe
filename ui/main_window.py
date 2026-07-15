from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QStackedWidget
)

from PySide6.QtCore import Qt

from ui.pages.home_page import HomePage
from ui.pages.sections_page import SectionsPage
from ui.pages.why_hire_page import WhyHirePage
from ui.pages.strengths_page import StrengthsPage
from ui.pages.weaknesses_page import WeaknessesPage
from ui.pages.mini_game_page import MiniGamePage
from ui.pages.previous_work_page import PreviousWorkPage
from ui.pages.programming_principles_page import ProgrammingPrinciplesPage
from ui.pages.inventory_forecast_page import InventoryForecastPage
from ui.pages.mind_reader_page import MindReaderPage

from ui.widgets.title_bar import TitleBar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.unlocked_sections = {
            "Why Hire Me": True,
            "Strengths": False,
            "Weaknesses": False,
            "Previous Work": False,
            "Programming\nPrinciples": False,
            "Inventory Demo": False,
            "Mind Reader": False,
            "Mini Game": False
        }

        self.setWindowTitle(
            "Why You Should Hire Me"
        )

        self.resize(
            1280,
            720
        )

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
        )


        central = QWidget()
        self.setCentralWidget(
            central
        )


        layout = QVBoxLayout()

        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout.setSpacing(
            0
        )

        central.setLayout(
            layout
        )


        # Custom title bar
        self.title_bar = TitleBar(
            self
        )

        layout.addWidget(
            self.title_bar
        )


        # Page container
        self.pages = QStackedWidget()


        # Create pages
        self.home_page = HomePage()
        self.sections_page = SectionsPage()
        self.why_hire_page = WhyHirePage()
        self.strengths_page = StrengthsPage()
        self.weaknesses_page = WeaknessesPage()
        self.mini_game_page = MiniGamePage()
        self.previous_work_page = PreviousWorkPage()
        self.programming_principles_page = ProgrammingPrinciplesPage()
        self.inventory_page = InventoryForecastPage()
        self.mind_reader_page = MindReaderPage()


        self.why_hire_page.finished.connect(
            self.open_sections
        )
        self.sections_page.update_unlocks(
            self.unlocked_sections
        )
        # Add pages
        self.pages.addWidget(
            self.home_page
        )

        self.pages.addWidget(
            self.sections_page
        )

        self.pages.addWidget(
            self.why_hire_page
        )

        self.pages.addWidget(
            self.strengths_page
        )

        self.pages.addWidget(
            self.weaknesses_page
        )

        self.pages.addWidget(
            self.mini_game_page
        )

        self.pages.addWidget(
            self.previous_work_page
        )

        self.pages.addWidget(
            self.programming_principles_page
        )

        self.pages.addWidget(
            self.inventory_page
        )

        self.pages.addWidget(
            self.mind_reader_page
        )

        layout.addWidget(
            self.pages
        )


        # Navigation signals

        self.home_page.hire_clicked.connect(
            self.open_sections
        )
        self.why_hire_page.finished.connect(
            lambda:
            self.unlock_section("Strengths")
        )
        self.strengths_page.finished.connect(
            self.open_sections
        )
        self.strengths_page.finished.connect(
            lambda:
            self.unlock_section("Weaknesses")
        )
        self.sections_page.home_clicked.connect(
            self.open_home
        )
        self.weaknesses_page.finished.connect(
            self.open_sections
        )
        self.weaknesses_page.finished.connect(
            lambda:
            self.unlock_section("Mini Game")
        )
        self.sections_page.open_page.connect(
            self.open_page
        )
        self.mini_game_page.finished.connect(
            self.open_sections
        )
        self.mini_game_page.finished.connect(
            lambda:
            self.unlock_section("Previous Work")
        )
        self.previous_work_page.finished.connect(
            self.open_sections
        )
        self.previous_work_page.finished.connect(
            lambda:
            self.unlock_section("Programming\nPrinciples")
        )
        self.programming_principles_page.finished.connect(
            self.open_sections
        )
        self.programming_principles_page.finished.connect(
            lambda:
            self.unlock_section("Inventory Demo")
        )
        self.inventory_page.back_clicked.connect(
            self.open_sections
        )
        self.inventory_page.back_clicked.connect(
            lambda:
            self.unlock_section("Mind Reader")
        )
        self.mind_reader_page.back_clicked.connect(
            self.open_sections
        )
        self.mind_reader_page.back_clicked.connect(
            lambda:
            self.unlock_section("Mini Game")
        )

    def unlock_section(self, section):

        if section in self.unlocked_sections:
            self.unlocked_sections[section] = True

        self.sections_page.update_unlocks(
            self.unlocked_sections
        )

    def open_sections(self):

        current_page = self.pages.currentWidget()

        if hasattr(current_page, "reset"):
            current_page.reset()

        self.pages.setCurrentWidget(
            self.sections_page
        )


    def open_home(self):

        self.pages.setCurrentWidget(
            self.home_page
        )


    def open_page(self, page_name):

        pages = {
            "why_hire_page":
                self.why_hire_page,
            "strengths_page":
                self.strengths_page,
            "weaknesses_page":
                self.weaknesses_page,
            "mini_game_page":
                self.mini_game_page,
            "previous_work_page":
                self.previous_work_page,
            "programming_principles_page":
                self.programming_principles_page,
            "inventory_page":
                self.inventory_page,
            "mind_reader_page":
                self.mind_reader_page,


        }

        if page_name in pages:

            page = pages[page_name]

            if hasattr(page, "reset"):
                page.reset()

            self.pages.setCurrentWidget(page)