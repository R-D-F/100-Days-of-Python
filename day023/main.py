import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
car_list = []
player = Player()
for num in range(25):
    new_car = CarManager()
    new_car.set_random_positon_start()
    car_list.append(new_car)
player.go_to_start()
current_score = 0 
game_is_on = True
sleep_time = .1
scoreboard.write_score(current_score)
while game_is_on:

    for car in car_list:
        car.move()
        if car.xcor() < -300: 
            car.set_random_position()
        if (player.xcor() - car.xcor()) < 25 and (player.xcor() - car.xcor()) > -25 and (player.ycor() - car.ycor()) < 20 and (player.ycor() - car.ycor()) > -20:    
            game_is_on = False
    if player.ycor() > 280:
        player.go_to_start()
        current_score += 1
        scoreboard.write_score(current_score)
        sleep_time = sleep_time / current_score 
    


    

    time.sleep(sleep_time)
    screen.update()
    screen.listen()
    screen.onkeypress(player.move_up, 'w')
    screen.update()

scoreboard.game_over()

screen.exitonclick()
