### Turtle race

import turtle as t

import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

positon_counter = -80
for turtle_index in range(0, 6):
    new_turtle = t.Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-225, y=positon_counter)
    new_turtle.color(colors[turtle_index])
    positon_counter += 25
    all_turtles.append(new_turtle)

    
if user_bet:
    is_race_on = True


tim = t.Turtle("turtle")
tim.penup()
tim.goto(210, -100)
tim.pendown()
tim.goto(210, 100)
tim.write("finish", move=True)
tim.penup()
tim.goto(225, 0)
tim.right(180)


while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 210:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You got it right!")
                print(f"The {turtle.pencolor()} turtle was the winner of the race")
                
            else:
                print("Sorry, you were wrong.")
                print(f"The {turtle.pencolor()} turtle was the winner of the race")
            is_race_on = False

screen.exitonclick()
