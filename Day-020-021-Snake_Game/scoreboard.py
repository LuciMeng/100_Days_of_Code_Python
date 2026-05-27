from turtle import Turtle
ALIGHTMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,280)
        self.write(arg=f'Score: {self.score}', move=False, align=ALIGHTMENT, font=FONT)

    def score_update(self):
        self.clear()
        self.score += 1
        self.write(arg=f'Score: {self.score}', move=False, align=ALIGHTMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f'GAVE OVER :(', move=False, align=ALIGHTMENT, font=FONT)
