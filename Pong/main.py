from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()
screen.setup(height=600, width=800)
screen.bgpic("background.gif")
screen.title("Montek's Pong Game")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")

game_on = True
while game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    # Detect Ball collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ycor()

    # Detect Ball collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.speed *= 0.9
        ball.bounce_xcor()

    # Detect if paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball.speed = 0.1
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball.speed = 0.1
screen.exitonclick()
