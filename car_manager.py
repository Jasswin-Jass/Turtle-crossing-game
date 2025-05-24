from turtle import Turtle
import random

COLORS = ["red", "orange", "dark red", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.cars = []

    def make_car(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-230, 230))
            new_car.setheading(180)
            self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
