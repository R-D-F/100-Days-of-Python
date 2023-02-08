from turtle import Screen, Turtle
import random

tim = Turtle()
tim.shape("turtle")

tim.color((random.random(), random.random(), random.random()))
tim.penup()
tim.setpos(0, 400)
tim.pendown()

shape_sides = 3
shape_sides_counter = 0
while shape_sides < 99:
    if shape_sides == shape_sides_counter:
        color1 = random.random()
        color2 = random.random()
        color3 = random.random()
        shape_sides += 1
        shape_sides_counter = 0
        tim.color(color1, color2, color3)
    tim.forward(20)
    tim.right(360/shape_sides)
    shape_sides_counter += 1
    print(tim.pos())
    print(shape_sides)











screen = Screen()
screen.exitonclick()