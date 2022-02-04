import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.setup(width=600, height=600)
screen.title("Montek's Crossing Game")

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_up, "w")
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()
    if player.end():
        player.starting()
        car_manager.level_up()
        scoreboard.increase()
screen.exitonclick()
