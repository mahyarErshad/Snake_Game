import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = []
def create_snake():
    x_cord = 0
    for _ in range(4):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(x=x_cord, y=0)
        x_cord -= 20
        snake.append(snake_body)

create_snake()

screen.update()

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    for snake_part in range(len(snake) - 1, 0, -1):
        new_x_position = snake[snake_part - 1].xcor()
        new_y_position = snake[snake_part - 1].ycor()
        snake[snake_part].goto((new_x_position, new_y_position))
    snake[0].forward(20)










screen.exitonclick()