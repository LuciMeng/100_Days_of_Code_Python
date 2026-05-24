from turtle import Turtle, Screen
import random

is_game_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which color of turtle do you choose?").lower()
colors = ["red", "orange", "yellow", "green", "blue",  "purple"]
start_position_x = -230
start_position_y = -110
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(start_position_x, start_position_y)
    start_position_y += 45
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_game_on = False
            if winning_color == user_bet:
                print(f"You win!! The {winning_color} turtle wins the bet!")
            else:
                print(f"You lose! The {winning_color} turtle wins the bet.")
            break


screen.exitonclick()

# instance timmy = Turtle()
#          Object  Class
# turtle is the module.
