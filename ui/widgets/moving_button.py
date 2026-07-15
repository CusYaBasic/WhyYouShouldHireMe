import random
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve

class MovingButton(QPushButton):

    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        self.animation = QPropertyAnimation(
            self,
            b"pos"
        )
        self.animation.setDuration(
            250
        )
        self.animation.setEasingCurve(
            QEasingCurve.Type.OutBack
        )

    def enterEvent(self, event):
        parent = self.parentWidget()

        if parent:
            max_x = parent.width() - self.width()
            max_y = parent.height() - self.height()

            new_x = random.randint(
                0,
                max_x
            )
            new_y = random.randint(
                0,
                max_y
            )

            self.animation.stop()
            self.animation.setStartValue(
                self.pos()
            )
            self.animation.setEndValue(
                QPoint(
                    new_x,
                    new_y
                )
            )
            self.animation.start()

        super().enterEvent(event)