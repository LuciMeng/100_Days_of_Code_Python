import turtle
from turtle import Turtle, Screen
import random
# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)


#Removed background colors
color_list = [(239, 221, 114), (18, 111, 193), (224, 59, 93), (235, 150, 74), (142, 88, 49), (115, 147, 211), (212, 127, 164), (34, 195, 118), (107, 106, 195), (137, 182, 20), (189, 17, 39), (232, 55, 45), (245, 147, 183), (112, 191, 149), (190, 47, 70), (19, 186, 208), (44, 52, 106), (145, 229, 168), (135, 220, 239), (202, 211, 7), (18, 154, 118), (239, 171, 152), (33, 43, 76), (111, 42, 40), (179, 174, 225), (250, 7, 37)]
turtle.colormode(255)
painting = Turtle()
painting.speed(0)
painting.hideturtle()
start_x = -250
start_y = -250
painting.penup()
painting.goto(start_x, start_y)


for _ in range(100):
    painting.dot(20, random.choice(color_list))
    painting.penup()
    painting.forward(50)
    if painting.xcor() > start_x + 50*9:
        start_y += 50
        painting.goto(start_x, start_y)

screen = Screen()
screen.exitonclick()
