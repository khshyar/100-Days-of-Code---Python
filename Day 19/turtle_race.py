from turtle import Turtle, Screen
import random

turtles = []
screen = Screen()
turtle_colors = ["red", "blue", "green", "yellow", "black"]
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Create turtles and assign each one a color from turtle_colors
for i in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[i])  # Assign color directly from the list
    new_turtle.penup()
    new_turtle.goto(-230, 100 - i * 50)  # Position turtles
    turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:  # Check if the turtle has crossed the finish line
            is_race_on = False
            winning_color = turtle.color()[0]
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(
                    f"You've lost! The {winning_color} turtle is the winner!")
            break
        # Move each turtle a random distance between 0 and 10
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
