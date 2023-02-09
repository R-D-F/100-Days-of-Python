from turtle import Turtle
from random import randint
from time import sleep

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("gray")

    def set_heading(self): 
        heading = randint(135, 225)
        self.setheading(heading)
        
    def move(self):
        self.forward(4)
        sleep(.0001)

    def detect_wall_colision(self):
        if self.ycor() > 290 and self.heading() > 90:
            last_heading = self.heading()
            new_heading =  (180 - last_heading) + 180
            self.setheading(new_heading)
            self.forward(16)
        elif self.ycor() > 290 and self.heading() < 90:
            last_heading = self.heading()
            new_heading =  360 - last_heading
            self.setheading(new_heading)
            self.forward(16)
        elif self.ycor() < -280 and self.heading() > 270:
            last_heading = self.heading()
            new_heading = 360 - last_heading
            self.setheading(new_heading)
            self.forward(16)
        elif self.ycor() < -280 and self.heading() < 270:
            last_heading = self.heading()
            new_heading = 180 -(last_heading - 180)
            self.setheading(new_heading)
            self.forward(16)

    def detect_colision_with_paddle(self, right_paddle, left_paddle):
        ball_xpos = self.xcor()
        ball_ypos = self.ycor()
        right_paddle_xpos = right_paddle.xcor()
        right_paddle_ypos = right_paddle.ycor()
        left_paddle_xpos = left_paddle.xcor()
        left_paddle_ypos = left_paddle.ycor()
        if ball_xpos > (right_paddle_xpos - 10) and ((ball_ypos < right_paddle_ypos + 50) and (ball_ypos > right_paddle_ypos - 50)):
            if self.heading() > 270:
                last_heading = self.heading()
                new_heading = 270 -(last_heading - 270)
                self.setheading(new_heading)
                self.forward(16)
            elif self.heading() < 90:
                last_heading = self.heading()
                new_heading = 90 + (90 - last_heading)
                self.setheading(new_heading)
                self.forward(16)
        elif ball_xpos < (left_paddle_xpos + 10) and ((ball_ypos < left_paddle_ypos + 50) and (ball_ypos > left_paddle_ypos - 50)):
            if self.heading() > 180:
                last_heading = self.heading()
                new_heading = 270 +(270 - last_heading)
                self.setheading(new_heading)
                self.forward(16)
            elif self.heading() < 180:
                last_heading = self.heading()
                new_heading = 90 -(last_heading - 90)
                self.setheading(new_heading)
                self.forward(16)
    def reset(self):
        self.home()