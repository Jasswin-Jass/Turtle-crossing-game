import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
score = Scoreboard()

game_is_on = True

screen.onkey(player.go_up, "Up")

while game_is_on:
    time.sleep(0.1)
    car.make_car()
    car.make_car()
    car.car_move()
    screen.update()
    if player.ycor() > 260:
        score.update_level()
        player.player_reset()
        car.increase_speed()
        time.sleep(0.5)
    for vehicle in car.cars:
        if vehicle.distance(player) < 25:
            score.game_over()
            game_is_on = False

screen.exitonclick()
