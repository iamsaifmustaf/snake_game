from turtle import Turtle
import random

ALIGNTMENT = "center"
FONT = ("Courier", 18, "normal")



class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.color("white")
        self.goto((0,270))
        self.update_score_board()
        self.hideturtle()

    def update_score_board(self):
        self.write(f"Score:{self.score}", align=ALIGNTMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto((0,0))
        self.write(f"GAME OVER", align=ALIGNTMENT, font=FONT)