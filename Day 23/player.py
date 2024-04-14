from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 25
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_point()
        self.setheading(90)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def start_point(self):
        self.goto(STARTING_POSITION)

    def next_level(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
            # self.goto(STARTING_POSITION)
