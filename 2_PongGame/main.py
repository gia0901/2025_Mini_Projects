from turtle import Turtle, Screen
from paddle import Paddle
from ball   import Ball
from scoreboard import ScoreBoard

import config as cfg
import time

#------------------------ OBJECT CREATIONS ------------------------#
# Screen
screen = Screen()
screen.setup(width = cfg.SCREEN_WIDTH, height = cfg.SCREEN_HEIGHT)
screen.bgcolor(cfg.BACKGROUND_COLOR)
screen.title("Pong Game")
screen.tracer(0)

# Middle-line drawing
middle_line = Turtle()
middle_line.color(cfg.MIDDLE_LINE_COLOR)
middle_line.pensize(cfg.MIDDLE_LINE_SIZE)
middle_line.hideturtle()


# Paddle
left_paddle = Paddle()
right_paddle = Paddle()

# Scoreboards
left_scoreboard = ScoreBoard()
right_scoreboard = ScoreBoard()

# Ball
ball = Ball()

#------------------------ PREPARATION ------------------------#
# Register hotkeys
screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

# Draw middle-line (temporary)
middle_line.goto(0, cfg.TOP_BOUNDARY)
middle_line.setheading(cfg.HEAD_SOUTH)
middle_line.forward(600)

# Move Paddles
left_paddle.goto(cfg.LEFT_PADDLE_XCOR, 0)
right_paddle.goto(cfg.RIGHT_PADDLE_XCOR, 0)

# Move Scoreboards
left_scoreboard.goto(cfg.LEFT_SCOREBOARD_XCOR, cfg.LEFT_SCOREBOARD_YCOR)
left_scoreboard.refresh()
right_scoreboard.goto(cfg.RIGHT_SCOREBOARD_XCOR, cfg.RIGHT_SCOREBOARD_YCOR)
right_scoreboard.refresh()

# Move the ball

is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(0.1)
    ball.start_to_move()


screen.exitonclick()