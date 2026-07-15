from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)

from PySide6.QtCore import (
    Qt,
    Signal,
    QUrl
)

from PySide6.QtMultimedia import (
    QMediaPlayer,
    QAudioOutput
)

from ui.widgets.moving_button import MovingButton
from ui.widgets.confetti_widget import ConfettiWidget



class HireLewisPage(QWidget):

    finished = Signal()


    def __init__(self):
        super().__init__()


        layout = QVBoxLayout(
            self
        )

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )


        self.title = QLabel(
            "Congratulations!"
        )

        self.title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.title.setStyleSheet("""
            color:white;
            font-size:32px;
            font-weight:bold;
        """)



        self.question = QLabel(
            "You have completed everything.\n\nWould you hire Lewis?"
        )

        self.question.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.question.setStyleSheet("""
            color:white;
            font-size:22px;
        """)



        self.yes_button = QPushButton(
            "YES"
        )

        self.no_button = MovingButton(
            "NO",
            self
        )


        self.yes_button.setFixedSize(
            120,
            50
        )

        self.no_button.setFixedSize(
            120,
            50
        )


        buttons = QHBoxLayout()

        buttons.addWidget(
            self.yes_button
        )

        buttons.addWidget(
            self.no_button
        )


        self.result = QLabel()

        self.result.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.result.setStyleSheet("""
            color:white;
            font-size:24px;
            font-weight:bold;
        """)


        layout.addWidget(
            self.title
        )

        layout.addWidget(
            self.question
        )

        layout.addLayout(
            buttons
        )

        layout.addWidget(
            self.result
        )


        # Confetti

        self.confetti = ConfettiWidget(
            self
        )



        # Sound

        self.audio_output = QAudioOutput()

        self.audio_output.setVolume(
            0.5
        )


        self.victory_sound = QMediaPlayer()

        self.victory_sound.setAudioOutput(
            self.audio_output
        )


        self.victory_sound.setSource(
            QUrl.fromLocalFile(
                "assets/sounds/victory.mp3"
            )
        )



        self.yes_button.clicked.connect(
            self.accept
        )



    def accept(self):

        self.yes_button.hide()

        self.no_button.hide()


        self.result.setText(
            "Excellent choice! 🎉\n\n"
            "I look forward to working with you."
        )


        self.victory_sound.stop()

        self.victory_sound.play()


        self.confetti.start()



    def reset(self):

        self.yes_button.show()

        self.no_button.show()


        self.result.clear()


        self.confetti.stop()