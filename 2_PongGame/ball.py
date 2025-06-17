from turtle import Turtle
import random
import time
import config as cfg

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_step = 10
        self.y_step = 10    # 90 degree of bouncing (fixed), not too real, need a way to enhance it
        self.color(cfg.BALL_COLOR)
        self.shape("circle")
        self.speed("fastest")
        self.penup()
    
    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0,0)
        # Change to opposite side
        self.x_step *= -1
        self.y_step *= -1 
        time.sleep(0.5)
    
    def reflect_horizontal(self):
        self.y_step *= -1
    
    def reflect_vertical(self):
        self.x_step *= -1


    

    
        
