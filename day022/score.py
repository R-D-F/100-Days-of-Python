from turtle import Turtle

class Score(Turtle):

    def __init__(self,):
        super().__init__()
        self.penup()
        self.ht()
        self.color("white")
    def right(self, score_right):
        self.goto(30, 270)
        self.write(score_right)
    def left(self, score_left):
        self.goto(-30, 270)
        self.write(score_left)

        
