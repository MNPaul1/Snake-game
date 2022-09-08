from ast import Global
from turtle import Turtle


from turtle import Turtle
ALIGN =  "center"
FONT = ("courier",15,"bold")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("day_20\data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align =ALIGN,font = FONT)
    
    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            with open("day_20\data.txt", "w") as file:
                file.write(str(self.score))
            self.high_score  = self.score
        self.score = 0
        self.update()

