import random
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel
)
from PySide6.QtCore import (
    Qt,
    QTimer,
    QPoint,
    Signal
)
from PySide6.QtGui import QPainter, QColor
from ui.widgets.player_card import PlayerCard
from PySide6.QtWidgets import QMessageBox

class MiniGamePage(QWidget):

    finished = Signal()

    def __init__(self):
        super().__init__()

        self.players = [
            "Stuart",
            "David",
            "Yas",
            "Robyn"
        ]

        self.high_scores = {
            "Stuart": 0,
            "David": 0,
            "Yas": 0,
            "Robyn": 0
        }

        self.selected_player = None


        self.layout = QVBoxLayout(self)

        self.layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )


        self.create_player_select()



    def create_player_select(self):

        self.player_select = QWidget()
        player_layout = QVBoxLayout(
            self.player_select
        )
        title = QLabel(
            "Choose Player"
        )
        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        player_layout.addWidget(
            title
        )
        players = QHBoxLayout()

        for player in self.players:

            card = PlayerCard(
                player,
                f"assets/images/players/{player.lower()}.png"
            )
            card.clicked.connect(
                lambda checked=False,
                p=player:
                self.start_game(p)
            )
            players.addWidget(
                card
            )

        player_layout.addLayout(
            players
        )
        self.layout.addWidget(
            self.player_select
        )



    def start_game(self, player):

        self.selected_player = player
        self.score = 0
        # Hide player selection
        self.player_select.hide()

        if hasattr(self, "game") and self.game is not None:
            self.game.deleteLater()

        self.game = GameWidget(
            self
        )
        self.layout.addWidget(
            self.game,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.game.setFocus()

    def game_over(self):

        if self.score > self.high_scores[self.selected_player]:
            self.high_scores[self.selected_player] = self.score
        result = QMessageBox(self)
        result.setWindowTitle(
            "Game Over"
        )
        result.setText(
            f"Game Over!\n\n"
            f"Player: {self.selected_player}\n"
            f"Score: {self.score}\n"
            f"High Score: {self.high_scores[self.selected_player]}"
        )
        restart_button = result.addButton(
            "Restart",
            QMessageBox.ButtonRole.AcceptRole
        )
        home_button = result.addButton(
            "Back to Menu",
            QMessageBox.ButtonRole.RejectRole
        )

        result.exec()

        if result.clickedButton() == restart_button:
            self.restart_game()
        elif result.clickedButton() == home_button:
            self.finished.emit()

    def restart_game(self):

        self.game.deleteLater()
        self.score = 0
        self.game = GameWidget(
            self
        )
        self.layout.addWidget(
            self.game,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.game.setFocus()

    def reset(self):

        # Remove old game safely
        if hasattr(self, "game") and self.game is not None:
            self.game.timer.stop()
            self.game.deleteLater()
            self.game = None

        self.score = 0
        self.selected_player = None
        # Show player selection again
        self.player_select.show()

class GameWidget(QWidget):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.setFixedSize(
            800,
            500
        )
        # Player
        self.player_x = 350
        self.player_speed = 8
        self.keys = set()
        # Ball
        self.ball = QPoint(
            random.randint(0, 750),
            0
        )
        self.ball_speed = 5
        # Score/lives
        self.score = 0
        self.lives = 3
        self.score_label = QLabel(
            "Score: 0   Lives: 3",
            self
        )
        self.score_label.setFixedWidth(
            250
        )
        self.score_label.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-weight: bold;
        """)
        self.score_label.move(
            20,
            20
        )
        self.timer = QTimer()
        self.timer.timeout.connect(
            self.update_game
        )
        self.timer.start(
            16
        )
        self.setFocusPolicy(
            Qt.FocusPolicy.StrongFocus
        )

    def spawn_ball(self):

        self.ball = QPoint(
            random.randint(0, 750),
            0
        )


    def update_game(self):

        # Smooth movement
        if (
            Qt.Key.Key_A in self.keys
            or Qt.Key.Key_Left in self.keys
        ):
            self.player_x -= self.player_speed
        if (
            Qt.Key.Key_D in self.keys
            or Qt.Key.Key_Right in self.keys
        ):
            self.player_x += self.player_speed


        # Keep basket on screen
        self.player_x = max(
            0,
            min(
                700,
                self.player_x
            )
        )
        # Move ball
        self.ball.setY(
            self.ball.y() + self.ball_speed
        )
        # Missed
        if self.ball.y() > 500:

            self.lives -= 1
            self.update_ui()
            self.spawn_ball()

            if self.lives <= 0:
                self.game_over()


        # Catch
        if (
            420 < self.ball.y() < 460
            and
            self.player_x < self.ball.x()
            <
            self.player_x + 100
        ):

            self.score += 1
            # Increase difficulty
            self.ball_speed += 0.2
            self.update_ui()
            self.spawn_ball()

        self.update()

    def update_ui(self):

        self.score_label.setText(
            f"Score: {self.score}   Lives: {self.lives}"
        )

    def keyPressEvent(self, event):

        self.keys.add(
            event.key()
        )

    def keyReleaseEvent(self, event):

        self.keys.discard(
            event.key()
        )

    def game_over(self):

        self.timer.stop()
        self.parent.score = self.score
        self.parent.game_over()

    def paintEvent(self,event):

        painter = QPainter(self)
        # Ball
        painter.setBrush(
            QColor("white")
        )
        painter.drawEllipse(
            self.ball,
            15,
            15
        )
        # Basket
        painter.drawRect(
            self.player_x,
            430,
            100,
            30
        )