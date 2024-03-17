from turtle import *
import random


tiny = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed",
          "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

angle = 360
start_shape = 3
start_pos = tiny.pos()

for i in range(10):

    for shape in range(start_shape):
        tiny.forward(50)
        tiny.right(angle / start_shape)

    start_shape += 1
    tiny.color(random.choice(colors))
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
