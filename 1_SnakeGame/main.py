from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import random
import time

# TODO:
# 1. Create snake segments
# 2. Moving the snake
# 3. Extend snake length
# 4. Create random food
# 5. Score board
# 6. Food collision & wall collision

# BUG:
# 1. If pressing key too fast, somehow the snake eats itself -> Game Over

############# Create main objects #############
screen = Screen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

############# Initialize screen settings #############
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("Snake Game - built with Turtle Graphics")
screen.tracer(0)    # Turn off animation

screen.listen()     # Listen for Hotkeys
screen.onkey(snake.turn_north, "Up")
screen.onkey(snake.turn_south, "Down")
screen.onkey(snake.turn_west, "Left")
screen.onkey(snake.turn_east, "Right")

is_game_continue = True
snake_speed = 0.1

while is_game_continue:
    # Update the animation in each loop, instead of default frequency (better animation for this game)
    screen.update()
    time.sleep(snake_speed)
    snake.move()

    if snake.detect_food(food):
        food.refresh()  # Food re-generate at another position
        scoreboard.increase_score()
        snake.extend()
    
    if snake.detect_wall() or snake.detect_tail():
        is_game_continue = False


# Game over
scoreboard.game_over()

screen.exitonclick()