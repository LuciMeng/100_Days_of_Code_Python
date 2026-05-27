from turtle import Turtle
X_COR = 0
Y_COR = 0
MOVE_DISTANCE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=X_COR, y=Y_COR)
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
       self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9 #Every time hit by paddle speeds up.

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1


