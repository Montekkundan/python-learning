from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def paddle_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def paddle_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
