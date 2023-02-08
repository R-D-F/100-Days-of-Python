import turtle as t

tim = t.Turtle()


screen = t.Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_right():
    tim.right(10)
def turn_left():
    tim.left(10)
def clear_page():
    tim.setpos(0,0)
    tim.clear()
    


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_page)

screen.exitonclick()
