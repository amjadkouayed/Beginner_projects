from turtle import Turtle, Screen
from prettytable import PrettyTable
import random


tim = Turtle()
screen = Screen()
tim.shape("classic")

tim.speed(0)

screen.colormode(255)

def generate_random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_direction():
    directions = random.randint(0, 360)
    tim.setheading(directions)


def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        tim.pencolor(generate_random_rgb())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

draw_spirograph(10)




    



screen.exitonclick()




























# table = PrettyTable()
# table.add_column("city", ["Berlin", "Hamburg", "Munich", "Cologne", "Frankfurt", "Stuttgart", "dusseldorf"])
# table.add_column("Population", ["3.52m","1.79m", "1.45m", "1.06m", "733,000", "625,000", "610,000" ])
# table.align = "l"
# print(table)