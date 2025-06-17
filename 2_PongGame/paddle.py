from turtle import Turtle

import config as cfg

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("orange")
        self.speed("fastest")
        self.penup()
        self.setheading(cfg.HEAD_NORTH)
        self.shapesize(stretch_wid=1.0, stretch_len=5.0)
    
    def move_up(self):
        # Detect top boundary:
        if self.ycor() < cfg.TOP_BOUNDARY - 70:
            self.setheading(cfg.HEAD_NORTH)
            self.forward(cfg.PADDLE_STEP)

    
    def move_down(self):
        # Detect bottom boundary:
        if self.ycor() > cfg.BOT_BOUNDARY + 70:
            self.setheading(cfg.HEAD_SOUTH)
            self.forward(cfg.PADDLE_STEP)