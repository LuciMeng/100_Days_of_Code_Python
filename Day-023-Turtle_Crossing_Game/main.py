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

screen.title("The Turtle Crossing Game")
screen.onkey(player.move, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    #Create cars and move them.
    car_manager.create_car()
    car_manager.move_cars()

    # Detect when the player collide with a car.
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    #Speed up cars after the finish line.
    if player.is_at_finish_line():
        car_manager.speed_up()
        scoreboard.increase_score()


    screen.update() #refresh after the cars move.
screen.exitonclick()
