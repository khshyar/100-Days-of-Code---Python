from turtle import *
import random


def random_walk(steps):
    for step in range(steps):
        tiny.forward(50)
        tiny.setheading(random.choice(direction))
        tiny.color(random_color())


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tiny = Turtle()
colormode(255)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
          "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]

tiny.speed(10)
tiny.pensize(10)
random_walk(200)
# tiny.right(angle / start_shape)
# for shape in range(10):
#     while
#     new_angle = angle / start_shape
#     tiny.forward(10)
#     tiny.right(new_angle)


# dashed
# for _ in range(20):

#     tiny.forward(10)
#     tiny.up()
#     tiny.forward(10)
#     tiny.down()


screen = Screen()

screen.exitonclick()
