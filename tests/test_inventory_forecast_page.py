import unittest

from PySide6.QtWidgets import QApplication

from ui.pages.inventory_forecast_page import InventoryForecastPage


app = QApplication.instance() or QApplication([])


class InventoryForecastPageTests(unittest.TestCase):
    def test_inventory_demo_has_richer_item_data_and_tooling(self):
        page = InventoryForecastPage()

        self.assertGreaterEqual(
            len(page.inventory),
            8
        )
        self.assertEqual(
            [
                page.table.horizontalHeaderItem(column).text()
                for column in range(page.table.columnCount())
            ],
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
        self.assertEqual(
            page.search_input.placeholderText(),
            "Search item or category"
        )
        self.assertEqual(
            page.restock_selected_button.text(),
            "Restock Selected"
        )

    def test_inventory_demo_uses_main_menu_purple_accent(self):
        page = InventoryForecastPage()

        self.assertIn(
            "background-color: #341539",
            page.simulate_button.styleSheet()
        )
        self.assertIn(
            "#7c4b87",
            page.simulate_button.styleSheet()
        )
        self.assertIn(
            "#7c4b87",
            page.search_input.styleSheet()
        )

    def test_simulate_day_button_reduces_stock(self):
        page = InventoryForecastPage()
        starting_stock = page.inventory[0]["stock"]

        page.simulate_button.click()

        self.assertEqual(
            page.inventory[0]["stock"],
            starting_stock - page.inventory[0]["daily_usage"]
        )

    def test_add_stock_button_increases_stock(self):
        page = InventoryForecastPage()
        starting_stock = page.inventory[0]["stock"]

        page.add_stock_button.click()

        self.assertEqual(
            page.inventory[0]["stock"],
            starting_stock + 50
        )

    def test_search_filters_inventory_by_item_or_category(self):
        page = InventoryForecastPage()

        page.search_input.setText("Potion")
        app.processEvents()

        visible_names = [
            page.table.item(row, 0).text()
            for row in range(page.table.rowCount())
        ]

        self.assertLess(
            len(visible_names),
            len(page.inventory)
        )
        self.assertTrue(
            all("Potion" in name for name in visible_names)
        )

    def test_restock_selected_item_sets_stock_to_target(self):
        page = InventoryForecastPage()
        page.search_input.clear()
        page.refresh()
        sword_index = next(
            index
            for index, item in enumerate(page.inventory)
            if item["name"] == "Iron Sword"
        )
        page.inventory[sword_index]["stock"] = 5
        page.refresh()
        page.table.selectRow(sword_index)

        page.restock_selected_button.click()

        self.assertEqual(
            page.inventory[sword_index]["stock"],
            page.inventory[sword_index]["target_stock"]
        )

    def test_summary_labels_count_low_and_critical_items(self):
        page = InventoryForecastPage()

        self.assertIn(
            "Items:",
            page.total_items_value.text()
        )
        self.assertIn(
            "Low:",
            page.low_stock_value.text()
        )
        self.assertIn(
            "Critical:",
            page.critical_stock_value.text()
        )


if __name__ == "__main__":
    unittest.main()
