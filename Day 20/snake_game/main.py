from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

turtles = []
positions = [(0, 0), (-20, 0), (-40, 0)]
for i in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(positions[i])
    turtles.append(new_turtle)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for turtle_num in range(len(turtles)-1, 0, -1):
        new_x = turtles[turtle_num - 1].xcor()
        new_y = turtles[turtle_num - 1].ycor()
        turtles[turtle_num].goto(new_x, new_y)
    turtles[0].forward(20)
# 187
screen.exitonclick()
