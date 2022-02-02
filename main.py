import turtle
import colorgram
import random

timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

# TODO:1:Creaating the colors list by extracting color from other images
# color_list = colorgram.extract('hirst painting.jpg', 30)
# rgb_colors = []
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     shade = (r, g, b)
#     rgb_colors.append(shade)
# print(rgb_colors)


usable_colors = [(173, 79, 34), (240, 224, 82), (47, 35, 25), (213, 152, 86), (22, 25, 66), (146, 27, 40),
                 (44, 44, 118), (164, 22, 16), (53, 87, 151), (126, 161, 216), (206, 86, 127), (151, 53, 85),
                 (27, 42, 28), (213, 81, 63), (142, 182, 143), (115, 107, 197), (65, 31, 36), (78, 117, 61),
                 (197, 128, 158), (82, 87, 32), (202, 140, 44), (152, 211, 189), (161, 179, 230), (87, 154, 107),
                 (249, 223, 1), (61, 147, 169)]
# TODO:2:Creating the picture using the Colors extracted
timmy.penup()
timmy.hideturtle()
# Solution 1: Using Goto method of turtle
# x = 0.0
# y = 0.0
# for i in range(10):
#
#     for j in range(10):
#         chosen = random.choice(usable_colors)
#         timmy.forward(50)
#         timmy.dot(20, chosen)
#     y = y + 50.0
#     timmy.goto(x, y)

# Solution 2: Using setheading method of turtle

timmy.setheading(225)
timmy.forward(400)
timmy.setheading(0)
total_dots = 100
for dots in range(1, total_dots + 1):
    timmy.dot(20, random.choice(usable_colors))
    timmy.forward(50)

    if dots % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen.screensize(4000, 4000)
screen.exitonclick()
