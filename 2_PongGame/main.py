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

# Paddle
left_paddle = Paddle(cfg.LEFT_PADDLE_START_CORD)
right_paddle = Paddle(cfg.RIGHT_PADDLE_START_CORD)

# Scoreboards
left_scoreboard = ScoreBoard(cfg.LEFT_SCOREBOARD_CORD)
right_scoreboard = ScoreBoard(cfg.RIGHT_SCOREBOARD_CORD)

# Ball
ball = Ball()

#------------------------ PREPARATION ------------------------#
# Register hotkeys
screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")


#------------------------ MAIN LOOP --------------------------#
is_game_on = True

game_speed = cfg.DEFAULT_BALL_SPEED

while is_game_on:
    time.sleep(game_speed)
    screen.update()
    
    ball.move()

    # Detect top / bottom wall collision
    if ball.ycor() > cfg.TOP_BOUNDARY - 25 or ball.ycor() < cfg.BOT_BOUNDARY + 25:
        ball.reflect_horizontal()

    # Detect left paddle collision
    # Increase the ball speed whenever touching the paddle, make the game more difficult over time.
    if ball.xcor() < cfg.LEFT_BOUNDARY + 40 and ball.distance(left_paddle) < 50:
        ball.reflect_vertical()
        game_speed *= cfg.SPEED_INCREASE_RATE

    elif ball.xcor() > cfg.RIGHT_BOUNDARY - 50 and ball.distance(right_paddle) < 50:
        ball.reflect_vertical()
        game_speed *= cfg.SPEED_INCREASE_RATE

    # Detect out of range
    # Start a new round, restart ball speed value
    if ball.xcor() < cfg.LEFT_BOUNDARY:
        right_scoreboard.increase_score()
        game_speed = cfg.DEFAULT_BALL_SPEED
        ball.reset_position()

    elif ball.xcor() > cfg.RIGHT_BOUNDARY:
        left_scoreboard.increase_score()
        game_speed = cfg.DEFAULT_BALL_SPEED
        ball.reset_position()


screen.exitonclick()