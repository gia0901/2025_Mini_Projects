from turtle import Turtle

import config as cfg

class ScoreBoard(Turtle):
    def __init__(self, cord):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(cord[0], cord[1])
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"SCORE: {self.score}", align=cfg.SCOREBOARD_ALIGNMENT, font=cfg.SCOREBOARD_FONT)

    def increase_score(self):
        self.score += 1
        self.refresh()