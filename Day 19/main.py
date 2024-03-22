from turtle import *

tiny = Turtle()
screen = Screen()


def move_forwards():
    tiny.forward(100)


screen.listen()
screen.onkey(move_forwards, "w")
screen.exitonclick()
