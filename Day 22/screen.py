from turtle import Screen as BaseScreen


class MyScreen(BaseScreen):
    def __init__(self):
        super().__init__()
        self.setup(width=500, height=300)
        self.bgcolor("black")
        self.title("My Pong Game")
        self.exitonclick()
