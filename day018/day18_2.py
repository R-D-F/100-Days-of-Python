import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


angles = [0, 90, 180, 270]
tim.color(random_color())
tim.shape("turtle")
tim.pensize(10)
tim.speed(0)
for _ in range (5):
    

    heading = random.choice(angles)

    tim.setheading(heading)
    tim.forward(25)
    tim.color(random_color())























screen = t.Screen()
screen.exitonclick()