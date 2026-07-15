# this class was created by AI as I couldn't find a good way of doing this

import random

from PySide6.QtWidgets import QWidget, QFrame
from PySide6.QtCore import QTimer, Qt


class ConfettiWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )

        self.particles = []

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_particles
        )


    def start(self):

        self.setGeometry(
            self.parent().rect()
        )

        self.show()

        self.create_particles()

        self.timer.start(
            16
        )


    def create_particles(self):

        # remove old particles
        for particle in self.particles:
            particle.deleteLater()

        self.particles.clear()


        for _ in range(100):

            particle = QFrame(
                self
            )

            size = random.randint(
                5,
                12
            )

            particle.setFixedSize(
                size,
                size
            )


            particle.setStyleSheet(
                f"""
                background: rgb(
                    {random.randint(50,255)},
                    {random.randint(50,255)},
                    {random.randint(50,255)}
                );

                border-radius:
                    {size // 2}px;
                """
            )


            particle.move(
                random.randint(
                    0,
                    self.width()
                ),

                random.randint(
                    -self.height(),
                    0
                )
            )


            particle.show()

            self.particles.append(
                particle
            )


    def update_particles(self):

        for particle in self.particles:

            x = particle.x()

            y = particle.y()


            y += random.randint(
                3,
                8
            )

            x += random.randint(
                -3,
                3
            )


            if y > self.height():

                y = random.randint(
                    -100,
                    0
                )

                x = random.randint(
                    0,
                    self.width()
                )


            particle.move(
                x,
                y
            )


    def stop(self):

        self.timer.stop()

        self.hide()