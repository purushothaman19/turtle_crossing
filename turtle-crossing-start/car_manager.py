from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 10

    def create(self):
        num = random.randint(1, 3)
        if num == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(300, random.randint(-230, 250))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def refresh(self):
        self.car_speed += MOVE_INCREMENT
        print(self.car_speed)



