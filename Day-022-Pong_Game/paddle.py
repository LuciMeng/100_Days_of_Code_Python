from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position): # pass a tuple for position
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)  # 20pixel x5 = 100 pixels
        self.goto(position) #tuple
        self.speed(0)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y <= 250:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y >= -250:
            self.goto(self.xcor(), new_y)

