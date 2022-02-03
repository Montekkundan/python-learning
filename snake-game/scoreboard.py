from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        if self.score == 69:
            self.write(f"Score: {self.score} NICE!", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()
