from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.color("white")

    def increase_score(self):
        self.score += 1  
        self.draw_score() 

    def draw_score(self):
        self.clear()
        self.write((f"Score: {self.score}"), align= ALIGNMENT, font= FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= ALIGNMENT, font= FONT)
