from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False,
                   align="Center", font=("Arial", 25, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False,
                   align="Center", font=("Arial", 25, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
