import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.update()

snake = Snake()

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()











screen.exitonclick()