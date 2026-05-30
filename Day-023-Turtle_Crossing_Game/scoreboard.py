FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.level = 1
        self.display_level()

    def display_level(self):
        self.write(f"Level {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.display_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
