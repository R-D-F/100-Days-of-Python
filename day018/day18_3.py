import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)

num_range = 200

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(num_range):
    tim.color(random_color())
    tim.right(360/num_range)
    tim.circle(100)




screen = t.Screen()
screen.exitonclick()