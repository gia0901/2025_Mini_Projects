from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()  # This prevent it appears at the default position (0,0)
    
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))