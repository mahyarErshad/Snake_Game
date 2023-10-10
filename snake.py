from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        x_cord = 0
        for _ in range(4):
            snake_body = Turtle("square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(x=x_cord, y=0)
            x_cord -= 20
            self.snake.append(snake_body)

    def move(self):
        for snake_part in range(len(self.snake) - 1, 0, -1):
            new_x_position = self.snake[snake_part - 1].xcor()
            new_y_position = self.snake[snake_part - 1].ycor()
            self.snake[snake_part].goto((new_x_position, new_y_position))
        self.snake[0].forward(20)