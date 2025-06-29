from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!\nYour max score: {self.score}", align=ALIGNMENT, font=FONT)