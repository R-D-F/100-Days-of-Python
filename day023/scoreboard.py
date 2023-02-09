from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup
        self.ht()
        self.goto(-250, 250)

    def write_score(self, score):
        self.clear()
        self.write(arg=score, font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game Over", font= FONT, align="center")
    
