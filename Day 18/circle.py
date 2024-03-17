from turtle import *
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(angle):
    for step in range(int(360/angle)):
        tiny.circle(200)
        tiny.color(random_color())
        tiny.setheading(tiny.heading() + angle)


colormode(255)
tiny = Turtle()
tiny.pensize(2)
tiny.speed("fastest")


draw_spirograph(1)
# tiny.heading()


screen = Screen()
screen.exitonclick()

# 174
