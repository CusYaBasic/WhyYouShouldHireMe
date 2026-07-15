from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem
)

from PySide6.QtCore import Qt, Signal


class InventoryForecastPage(QWidget):

    back_clicked = Signal()

    def __init__(self):
        super().__init__()


        self.inventory = [
            {
                "name": "Health Potion",
                "stock": 120,
                "daily_usage": 8
            },

            {
                "name": "Iron Sword",
                "stock": 25,
                "daily_usage": 2
            },

            {
                "name": "Wood",
                "stock": 400,
                "daily_usage": 20
            },

            {
                "name": "Mana Crystal",
                "stock": 60,
                "daily_usage": 5
            }
        ]


        layout = QVBoxLayout(
            self
        )


        title = QLabel(
            "Inventory Forecast Demo"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )


        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: white;
        """)


        layout.addWidget(
            title
        )


        self.table = QTableWidget()

        self.table.setColumnCount(
            4
        )


        self.table.setHorizontalHeaderLabels(
            [
                "Item",
                "Stock",
                "Daily Usage",
                "Days Remaining"
            ]
        )


        layout.addWidget(
            self.table
        )

        buttons = QHBoxLayout()

        self.back_button = QPushButton(
            "Back to Menu"
        )

        self.simulate_button = QPushButton(
            "Simulate Day"
        )

        self.add_stock_button = QPushButton(
            "Add Stock"
        )

        buttons.addWidget(
            self.back_button
        )

        buttons.addWidget(
            self.simulate_button
        )

        buttons.addWidget(
            self.add_stock_button
        )

        layout.addLayout(
            buttons
        )

        self.back_button.clicked.connect(
            self.back_clicked.emit
        )


        self.refresh()



    def refresh(self):

        self.table.setRowCount(
            len(self.inventory)
        )


        for row,item in enumerate(self.inventory):

            days = (
                item["stock"] //
                item["daily_usage"]
            )


            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    item["name"]
                )
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(item["stock"])
                )
            )

            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    str(item["daily_usage"])
                )
            )


            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    f"{days} days"
                )
            )



    def simulate_day(self):

        for item in self.inventory:

            item["stock"] -= item["daily_usage"]

            if item["stock"] < 0:
                item["stock"] = 0


        self.refresh()



    def add_stock(self):

        for item in self.inventory:

            item["stock"] += 50


        self.refresh()



    def reset(self):

        pass