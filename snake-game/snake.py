from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body_parts = []
        self.create_snake()

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_body(positions)

    def add_body(self, positions):
        new_body = Turtle("square")
        new_body.color("blue")
        new_body.penup()
        new_body.goto(positions)
        self.body_parts.append(new_body)

    def reset(self):
        for body in self.body_parts:
            body.goto(1000, 1000)
        self.body_parts.clear()
        self.create_snake()

    def move(self):
        for body in range(len(self.body_parts) - 1, 0, -1):
            x_cor = self.body_parts[body - 1].xcor()
            y_cor = self.body_parts[body - 1].ycor()
            self.body_parts[body].goto(x_cor, y_cor)
        self.body_parts[0].forward(DISTANCE)

    def extend(self):
        self.add_body(self.body_parts[-1].position())

    def up(self):
        if self.body_parts[0].heading() != DOWN:
            self.body_parts[0].setheading(UP)

    def down(self):
        if self.body_parts[0].heading() != UP:
            self.body_parts[0].setheading(DOWN)

    def left(self):
        if self.body_parts[0].heading() != RIGHT:
            self.body_parts[0].setheading(LEFT)

    def right(self):
        if self.body_parts[0].heading() != LEFT:
            self.body_parts[0].setheading(RIGHT)
