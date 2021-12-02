import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.up, key="Up")
screen.onkey(player.down, key='Down')
car = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()
    for ca in car.all_cars:
        if ca.distance(player) < 27:
            game_is_on = False
            scoreboard.game_up()

    if player.ycor() == 280:
        player.refresh()
        car.refresh()
        scoreboard.score_up()

screen.exitonclick()
