from PySide6.QtWidgets import  QPushButton

class HoverCloseButton(QPushButton):
    def __init__(self, title_bar):
        super().__init__("X")
        self.title_bar = title_bar

    def enterEvent(self, event):
        self.title_bar.show_image()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.title_bar.hide_image()
        super().leaveEvent(event)