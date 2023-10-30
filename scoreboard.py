from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highScore.txt") as data:
            self.high_score = int(data.read())
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
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highScore.txt", mode="w") as data:
                data.write(f"{self.high_score}")

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("courier", 24, "normal"))