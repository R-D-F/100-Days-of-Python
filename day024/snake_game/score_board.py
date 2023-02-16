from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        with open("high_score.txt", mode="r") as file:
            self.high_score = file.read()
        self.high_score = int(self.high_score)
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.color("white")

    def increase_score(self):
        self.score += 1  
        self.draw_score() 

    def draw_score(self):
        self.clear()
        self.write((f"Score: {self.score} High Score: {self.high_score}"), align= ALIGNMENT, font= FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = str(self.score)
            with open("high_score.txt", mode="w") as file:
                file.write(self.score)
        self.score = 0 
        self.draw_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align= ALIGNMENT, font= FONT)
