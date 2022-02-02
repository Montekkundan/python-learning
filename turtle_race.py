from turtle import Turtle, Screen
import random

spell_check = True
game_on = False
screen = Screen()
screen.setup(width=600, height=400)
while spell_check:
    user_choice = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ").lower()
    if user_choice == "red" or user_choice == "orange" or user_choice == "yellow" or user_choice == "green" or user_choice == "blue" or user_choice == "purple":
        spell_check = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-70, -40, -10, 20, 50, 80]
list_of_turtles = []
for turtles in range(0, 6):
    turtle_new = Turtle(shape="turtle")
    turtle_new.color(colors[turtles])
    turtle_new.penup()
    turtle_new.goto(x=-280, y=positions[turtles])
    list_of_turtles.append(turtle_new)

if user_choice:
    game_on = True
while game_on:
    for turtles in list_of_turtles:
        if turtles.xcor() > 280:
            game_on = False
            wining_color = turtles.pencolor()
            if wining_color == user_choice:
                print(f"You've won! The {wining_color} turtle is the winner!")
            else:
                print(f"You've lost! The {wining_color} turtle is the winner!")
        distance = random.randint(0, 10)
        turtles.forward(distance)
screen.exitonclick()
