from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.setup(height=600, width=600)
screen.bgpic("bg.gif")
screen.title("Montek's Snake Game")
screen.tracer(0)

screen.listen()
screen.onkeypress(snake.up, key="w")
screen.onkey(snake.right, key="d")
screen.onkey(snake.left, key="a")
screen.onkeypress(snake.down, key="s")
screen.onkeypress(snake.up, key="Up")
screen.onkey(snake.right, key="Right")
screen.onkey(snake.left, key="Left")
screen.onkeypress(snake.down, key="Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Collision with Food
    if snake.body_parts[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
    # Collision with Wall
    if snake.body_parts[0].xcor() > 290 or snake.body_parts[0].xcor() < -299 or snake.body_parts[0].ycor() > 290 or snake.body_parts[0].ycor() < -290:
        scoreboard.reset_score()
        snake.reset()
    # Collision with Tail
    for body in snake.body_parts[1:]:
        if snake.body_parts[0].distance(body) < 10:
            scoreboard.reset_score()
            snake.reset()

screen.exitonclick()
