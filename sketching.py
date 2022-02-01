from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()


def move_forward():
    arrow.forward(10)


def move_right():
    arrow.right(10)


def move_left():
    arrow.left(10)


def move_backward():
    arrow.backward(10)


def clear():
    arrow.clear()
    arrow.penup()
    arrow.home()
    arrow.pendown()


def undo_it():
    arrow.undo()


screen.listen()
screen.onkeypress(move_forward, key="w")
screen.onkey(move_right, key="d")
screen.onkey(move_left, key="a")
screen.onkeypress(move_backward, key="s")
screen.onkeypress(move_forward, key="Up")
screen.onkey(move_right, key="Right")
screen.onkey(move_left, key="Left")
screen.onkeypress(move_backward, key="Down")
screen.onkey(clear, key="c")
screen.onkey(undo_it, "z")
screen.exitonclick()
