from turtle import Screen
from paddle import Paddle 
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0) # turns off the animation

screen.listen()
r_paddle = Paddle((350,0)) # pass a tuple as the starting position
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.up, "Up") 
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s") # Lower case

game_is_on = True
while game_is_on:
    ball.move()
    time.sleep(ball.move_speed) #waits 0.1s, moves ball then waits again
    screen.update()

#Detect collision with the top and bottom wall. Ball bounces back.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#Detect collision with r_paddle and l_paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

#Detect if the ball goes out of bounds, rest the ball position to the center of the screen.
#The ball starts moving towards the other player.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_gains_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_gains_point()

#Game ends when one player scores 5 points.
    if scoreboard.compare_score():
        game_is_on = False

screen.exitonclick()
