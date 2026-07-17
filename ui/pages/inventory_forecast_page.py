from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QHeaderView,
    QAbstractItemView,
    QSizePolicy
)
from PySide6.QtCore import Qt, Signal


MENU_PURPLE = "#341539"
MENU_PURPLE_BORDER = "#7c4b87"
MENU_PURPLE_HOVER = "#4a2053"
MENU_PURPLE_PRESSED = "#241029"
MENU_PURPLE_SELECTION = "#3b2144"


class InventoryForecastPage(QWidget):

    back_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.setObjectName("inventoryPage")
        self.setAttribute(
            Qt.WidgetAttribute.WA_StyledBackground,
            True
        )
        self.setStyleSheet("""
            #inventoryPage {
                background-color: #080c12;
            }
        """)

        self.inventory = [
            {
                "name": "Health Potion",
                "category": "Consumables",
                "stock": 120,
                "daily_usage": 8,
                "reorder_point": 60,
                "target_stock": 180
            },
            {
                "name": "Mana Crystal",
                "category": "Consumables",
                "stock": 60,
                "daily_usage": 5,
                "reorder_point": 30,
                "target_stock": 100
            },
            {
                "name": "Stamina Potion",
                "category": "Consumables",
                "stock": 35,
                "daily_usage": 6,
                "reorder_point": 40,
                "target_stock": 120
            },
            {
                "name": "Iron Sword",
                "category": "Weapons",
                "stock": 25,
                "daily_usage": 2,
                "reorder_point": 18,
                "target_stock": 60
            },
            {
                "name": "Arrows",
                "category": "Weapons",
                "stock": 90,
                "daily_usage": 15,
                "reorder_point": 75,
                "target_stock": 220
            },
            {
                "name": "Wood",
                "category": "Materials",
                "stock": 400,
                "daily_usage": 20,
                "reorder_point": 150,
                "target_stock": 500
            },
            {
                "name": "Leather",
                "category": "Materials",
                "stock": 70,
                "daily_usage": 7,
                "reorder_point": 45,
                "target_stock": 160
            },
            {
                "name": "Iron Ore",
                "category": "Materials",
                "stock": 140,
                "daily_usage": 12,
                "reorder_point": 80,
                "target_stock": 240
            },
            {
                "name": "Torch",
                "category": "Utility",
                "stock": 18,
                "daily_usage": 4,
                "reorder_point": 25,
                "target_stock": 80
            },
            {
                "name": "Lockpick",
                "category": "Utility",
                "stock": 12,
                "daily_usage": 3,
                "reorder_point": 20,
                "target_stock": 75
            },
            {
                "name": "Phoenix Feather",
                "category": "Rare",
                "stock": 2,
                "daily_usage": 1,
                "reorder_point": 5,
                "target_stock": 20
            }
        ]

        layout = QVBoxLayout(
            self
        )
        layout.setContentsMargins(
            48,
            30,
            48,
            30
        )
        layout.setSpacing(
            16
        )

        self.content_panel = QWidget()
        self.content_panel.setObjectName("inventoryPanel")
        self.content_panel.setMaximumWidth(
            1120
        )
        self.content_panel.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        self.content_panel.setStyleSheet("""
            #inventoryPanel {
                background-color: #111820;
                border: 1px solid #263241;
                border-radius: 18px;
            }
        """)

        content_layout = QVBoxLayout(
            self.content_panel
        )
        content_layout.setContentsMargins(
            30,
            26,
            30,
            26
        )
        content_layout.setSpacing(
            16
        )

        title = QLabel(
            "Inventory Forecast Demo"
        )
        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        title.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            color: #f5f7fb;
        """)

        subtitle = QLabel(
            "Track stock, forecast run-out risk, and restock items before they become a problem."
        )
        subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        subtitle.setStyleSheet("""
            font-size: 16px;
            color: #c8d0dc;
        """)

        content_layout.addWidget(title)
        content_layout.addWidget(subtitle)

        summary_layout = QHBoxLayout()
        summary_layout.setSpacing(
            12
        )
        self.total_items_value = self.create_summary_label("Items: 0")
        self.low_stock_value = self.create_summary_label("Low: 0")
        self.critical_stock_value = self.create_summary_label("Critical: 0")
        self.average_days_value = self.create_summary_label("Avg days: 0")

        for label in [
            self.total_items_value,
            self.low_stock_value,
            self.critical_stock_value,
            self.average_days_value
        ]:
            summary_layout.addWidget(label)

        content_layout.addLayout(summary_layout)

        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(
            12
        )

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Search item or category"
        )
        self.search_input.textChanged.connect(
            self.refresh
        )
        self.search_input.setStyleSheet(f"""
            QLineEdit {{
                background-color: #0b1118;
                color: #f5f7fb;
                border: 1px solid #334255;
                border-radius: 10px;
                padding: 10px 14px;
                font-size: 15px;
            }}
            QLineEdit:focus {{
                border-color: {MENU_PURPLE_BORDER};
            }}
        """)
        controls_layout.addWidget(self.search_input)

        self.simulate_button = QPushButton(
            "Simulate Day"
        )
        self.add_stock_button = QPushButton(
            "Add 50 All"
        )
        self.restock_selected_button = QPushButton(
            "Restock Selected"
        )
        self.back_button = QPushButton(
            "Back to Menu"
        )

        primary_style = self.button_style(
            MENU_PURPLE,
            MENU_PURPLE_BORDER,
            MENU_PURPLE_HOVER
        )
        secondary_style = self.button_style("#1d2733", "#334255", "#263447")

        self.simulate_button.setStyleSheet(primary_style)
        self.add_stock_button.setStyleSheet(secondary_style)
        self.restock_selected_button.setStyleSheet(secondary_style)
        self.back_button.setStyleSheet(secondary_style)

        for button in [
            self.simulate_button,
            self.add_stock_button,
            self.restock_selected_button,
            self.back_button
        ]:
            controls_layout.addWidget(button)

        content_layout.addLayout(controls_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(
            7
        )
        self.table.setHorizontalHeaderLabels(
            [
                "Item",
                "Category",
                "Stock",
                "Daily Usage",
                "Days Left",
                "Reorder Point",
                "Status"
            ]
        )
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: #0b1118;
                alternate-background-color: #101923;
                color: #f5f7fb;
                border: 1px solid #263241;
                border-radius: 12px;
                gridline-color: #263241;
                font-size: 14px;
                selection-background-color: {MENU_PURPLE_SELECTION};
                selection-color: #f5f7fb;
            }}
            QHeaderView::section {{
                background-color: #1d2733;
                color: #c8d0dc;
                border: 0;
                border-bottom: 1px solid #334255;
                padding: 8px;
                font-weight: bold;
            }}
        """)

        content_layout.addWidget(
            self.table
        )

        layout.addWidget(
            self.content_panel,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.back_button.clicked.connect(
            self.back_clicked.emit
        )
        self.simulate_button.clicked.connect(
            self.simulate_day
        )
        self.add_stock_button.clicked.connect(
            self.add_stock
        )
        self.restock_selected_button.clicked.connect(
            self.restock_selected
        )
        self.refresh()

    def create_summary_label(self, text):
        label = QLabel(text)
        label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        label.setStyleSheet("""
            QLabel {
                background-color: #0b1118;
                color: #f5f7fb;
                border: 1px solid #263241;
                border-radius: 10px;
                padding: 10px 14px;
                font-size: 15px;
                font-weight: bold;
            }
        """)
        return label

    def button_style(self, background, border, hover):
        return f"""
            QPushButton {{
                background-color: {background};
                color: #f5f7fb;
                border: 1px solid {border};
                border-radius: 10px;
                padding: 10px 14px;
                font-size: 14px;
                font-weight: bold;
                min-width: 104px;
            }}
            QPushButton:hover {{
                background-color: {hover};
            }}
            QPushButton:pressed {{
                background-color: {MENU_PURPLE_PRESSED};
            }}
        """

    def filtered_inventory(self):
        query = self.search_input.text().strip().lower()

        if not query:
            return list(enumerate(self.inventory))

        return [
            (index, item)
            for index, item in enumerate(self.inventory)
            if (
                query in item["name"].lower()
                or query in item["category"].lower()
            )
        ]

    def days_remaining(self, item):
        return item["stock"] // item["daily_usage"]

    def status_for_item(self, item):
        if self.days_remaining(item) <= 3:
            return "Critical"

        if item["stock"] <= item["reorder_point"]:
            return "Low"

        return "Healthy"

    def refresh(self):

        visible_items = self.filtered_inventory()
        self.table.setRowCount(
            len(visible_items)
        )

        for row, (index, item) in enumerate(visible_items):
            values = [
                item["name"],
                item["category"],
                str(item["stock"]),
                str(item["daily_usage"]),
                f"{self.days_remaining(item)} days",
                str(item["reorder_point"]),
                self.status_for_item(item)
            ]

            for column, value in enumerate(values):
                table_item = QTableWidgetItem(value)
                table_item.setTextAlignment(
                    Qt.AlignmentFlag.AlignCenter
                )
                table_item.setData(
                    Qt.ItemDataRole.UserRole,
                    index
                )
                self.table.setItem(
                    row,
                    column,
                    table_item
                )

        self.update_summary()

    def update_summary(self):
        statuses = [
            self.status_for_item(item)
            for item in self.inventory
        ]
        average_days = sum(
            self.days_remaining(item)
            for item in self.inventory
        ) // len(self.inventory)

        self.total_items_value.setText(
            f"Items: {len(self.inventory)}"
        )
        self.low_stock_value.setText(
            f"Low: {statuses.count('Low')}"
        )
        self.critical_stock_value.setText(
            f"Critical: {statuses.count('Critical')}"
        )
        self.average_days_value.setText(
            f"Avg days: {average_days}"
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

    def restock_selected(self):
        selected_row = self.table.currentRow()

        if selected_row < 0:
            return

        selected_item = self.table.item(
            selected_row,
            0
        )

        if selected_item is None:
            return

        inventory_index = selected_item.data(
            Qt.ItemDataRole.UserRole
        )
        self.inventory[inventory_index]["stock"] = self.inventory[
            inventory_index
        ]["target_stock"]
        self.refresh()
        self.table.selectRow(
            selected_row
        )

    def reset(self):
        pass
