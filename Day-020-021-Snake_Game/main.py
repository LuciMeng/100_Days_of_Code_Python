from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Step 1 - Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #Turn off the tracer, more smooth

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up") #Not .up() -> don't want to call func now.
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Below -> Gets the snake auto move forward
game_is_on = True
while game_is_on:
    screen.update() # all seg positions change then the screen redraws once.
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.score_update()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect tail collision.
    for segment in snake.segments[1:]: #Skip the snake.head position [0]
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
