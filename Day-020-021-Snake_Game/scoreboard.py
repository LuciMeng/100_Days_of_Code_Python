from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")
with open("data.txt") as data_file:
    data = data_file.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(data)
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,280)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(arg=f'Score: {self.score}  High Score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data_file:
                data_file.write(str(self.high_score))
        self.score = 0
        self.score_update()

    def increase_score(self):
        self.score += 1
        self.score_update()
