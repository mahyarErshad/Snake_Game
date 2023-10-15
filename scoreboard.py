from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0 , 260)
        self.print_score()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"Game Over!", align="center", font=("courier", 24, "normal"))

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("courier", 24, "normal"))