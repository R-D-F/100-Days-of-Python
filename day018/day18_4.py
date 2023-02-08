import turtle as t
import random
import colorgram
import math

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
colors = colorgram.extract('damien-hirst-bromobenzotrifluoride.jpg', 15)
list_color = list(colors)
list_len = len(list_color) - 1
result_list = []
for item in range(list_len):
    rgb = list_color[item].rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    if (r + g + b) < 700:
        result_list.append(list_color[item])
        print("did it")


tim.penup()
tim.goto(-400, -400)
tim.hideturtle()

dots = 40
number_of_dots = dots * dots
dot_size = 30
space = 20
counter_x = 0
counter_y = 1
def draw_dot():
    tim_color = random.choice(result_list)
    tim_color_rgb = tim_color.rgb
    tim.color(tim_color_rgb)
    tim.dot(dot_size ,tim_color_rgb)

for _ in range(number_of_dots):
    counter_x += 1
    draw_dot()

    if math.sqrt(number_of_dots) == counter_x and counter_y % 2 != 0:
        tim.left(90)
        tim.forward(space)
        tim.left(90)
        counter_x = 0
        counter_y += 1
    elif math.sqrt(number_of_dots) == counter_x and counter_y % 2 == 0:
        tim.right(90)
        tim.forward(space)
        tim.right(90)
        counter_x = 0
        counter_y += 1
    else:
        tim.forward(space)
    










screen = t.Screen()
screen.exitonclick()