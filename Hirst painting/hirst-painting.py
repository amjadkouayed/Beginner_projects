import colorgram
from turtle import Turtle, Screen
from prettytable import PrettyTable
import random

# colours = colorgram.extract('hirstimage.jpg', 25)
# rgb_colours = []

# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colours.append(new_color)

# print(rgb_colours)


""" requirments:
10x10 rows color dots
dots should be 20 in size
they should be spaced apart by 50 paces

"""

color_list = [(203, 155, 91), (118, 162, 194), (157, 82, 53), (149, 64, 96), (65, 99, 144), (164, 153, 54), (219, 231, 240), (62, 122, 87), (191, 133, 157), (129, 183, 161), (187, 91, 123), (127, 29, 49), (225, 203, 124), (198, 96, 73), (78, 23, 52), (83, 155, 131), (44, 54, 104), (137, 37, 31), (153, 209, 193), (97, 123, 173), (77, 153, 164), (36, 38, 77)]
color_list2 = [(0,0,0), (255,0,255), (255,255,0), (0,255,255)]

tim = Turtle()
screen = Screen()
screen.colormode(255)



tim.hideturtle()
tim.speed(0)
tim.setheading(220)
tim.penup()
tim.forward(340)
tim.setheading(0)
tim.shape("turtle")




def newline():
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)


for _ in range(10):
    for i in range(10):
        tim.dot(40, random.choice(color_list2))
        tim.forward(50)
    newline()
    

    







screen.exitonclick()