import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    car_manager.move_cars()
    car_manager.generate_car()
    time.sleep(0.1)
    screen.update()

    # Detect the collision
    for car in car_manager.cars_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect the successful crossing
    if player.is_at_finish_line():
        player.restart_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
