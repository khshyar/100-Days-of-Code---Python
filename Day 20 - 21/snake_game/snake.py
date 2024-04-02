from turtle import Screen, Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def add_turtle(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_turtle(position)

    def eat_food(self):
        self.add_turtle(self.turtles[-1].position())

    def move(self):
        for turtle_num in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[turtle_num - 1].xcor()
            new_y = self.turtles[turtle_num - 1].ycor()
            self.turtles[turtle_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def set_head_up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def set_head_right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def set_head_left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def set_head_down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    # def pos_last_snake(self):
    #     new_x = self.turtles[len(self.turtles)-1].xcor()
    #     new_y = self.turtles[len(self.turtles)-1].ycor()
    #     last_pos = [(new_x, new_y)]
    #     return last_pos

    # def add_new_snake(self):
    #     new_turtle = Turtle(shape="square")
    #     new_turtle.color("white")
    #     new_turtle.penup()
    #     new_pos = pos_last_snake()
    #     new_turtle.goto(new_pos)
    #     self.turtles.append(new_turtle)
    # def snake_pos(self):
    #     return self.turtles[0].pos()
