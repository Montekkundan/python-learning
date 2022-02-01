import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("classic")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed(0)


def draw(gap_size):
    for a in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw(5)
screen = Screen()
screen.exitonclick()
