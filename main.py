import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.go_up, key="Up")

game_is_on = True
while game_is_on:
   
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_car()
    
    # detect collision with car
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            
    # detect when player has reached the other side
    if player.ycor() == 300:
        player.goto(0, -280)
    # update score
        scoreboard.score += 1
        scoreboard.update_score()
        carmanager.level_up()
        
      

            

screen.exitonclick()



