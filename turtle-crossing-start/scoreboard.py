from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.scores = 0
        self.score = Turtle()
        self.score.ht()
        self.screen = Screen()

    def game_up(self):
        self.score.home()
        self.score.write("Game Over.", align="center", font=FONT)

    def score_up(self):
        self.scores += 1
        self.score.penup()
        self.score.goto(-250, 250)
        self.score_card()

    def score_card(self):
        self.score.clear()
        self.score.write(f"Score: {self.scores}", align="center", font=("Courier", 10, "normal"))
