from turtle import *

tiny = Turtle()
screen = Screen()


def move_forwards():
    tiny.forward(2)


def move_back():
    tiny.back(100)


def set_head_right():
    angle = tiny.heading()
    tiny.seth(angle - 1)


def set_head_left():
    angle = tiny.heading()
    tiny.seth(angle + 1)


def clear():
    tiny.clear()
    tiny.penup()
    tiny.home()
    tiny.pendown()


screen.listen()
screen.onkeypress(move_forwards, "Up")
screen.onkeypress(set_head_right, "Right")
screen.onkeypress(move_back, "Down")
screen.onkeypress(set_head_left, "Left")
screen.onkeypress(clear, "c")


screen.exitonclick()
