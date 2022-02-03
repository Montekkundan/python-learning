from turtle import Turtle, Screen
import random


class Food(Turtle):
    screen = Screen()
    screen.register_shape("apple.gif")

    def __init__(self):
        super().__init__()
        self.shape("apple.gif")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
