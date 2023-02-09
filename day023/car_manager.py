from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
program_on = True

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len= 2)
        
        self.st()

    def set_random_positon_start(self):
        self.goto(random.randint(-280, 900), random.randint(-250, 280))

    def set_random_position(self):
        self.goto(random.randint(300, 1200), random.randint(-250, 280))

    def move(self): 
        self.setx(self.xcor()-MOVE_INCREMENT)
        

    
        
    
