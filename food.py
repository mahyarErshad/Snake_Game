from turtle import  Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("circle")
        super().penup()
        super().shapesize(stretch_wid=0.5, stretch_len=0.5)
        super().color("blue")
        super().speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 255)
        super().goto(random_x, random_y)