from turtle import Turtle
import random
import config as cfg

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.change_direction = True
        self.color(cfg.BALL_COLOR)
        self.shape("circle")
        self.speed("fastest")
        self.penup()
    
    def start_to_move(self):
        if self.change_direction == True:
            self.change_direction = False
            leftOrRight = random.randint(0,1)
            angle = random.randint(100, 260)

            if leftOrRight == 0:    # Left
                self.setheading(angle)
            else:  # Right
                self.setheading(-angle)
        
        self.forward(20)

    
        
