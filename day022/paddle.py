from turtle import Turtle

class Paddle(Turtle,):

    def __init__(self, x_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=None)
        self.color("white")
        self.goto(x_pos, 0)
        self.setheading(90)
    
    def move_up(self):
        self.forward(20)
    def move_down(self):
        self.back(20)

