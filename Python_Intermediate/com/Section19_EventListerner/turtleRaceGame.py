# building a turtle race game
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)

# creating a variable called user bet program
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race ? enter a color")

y_positions = [-70, -40, -10, 20, 50, 80, 110, 140]
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red", "purple"]
# every time we are creating a new instance of the turtle so, we are creating an empty list of the turtle
all_turtles = []
# creating a graphical turtle using turtle module
for turtle_index in range(0, 8):
    new_turtles = Turtle(shape="turtle")
    new_turtles.penup()
    new_turtles.color(colors[turtle_index])

    # here while running the code in the pyhon language all turtles are placed in the same positions
    # to avoid this we will create a list of y positions
    # if we directly pass the y positions in the code a float error will occur in the index
    # to avoid this error we need to represent the turtle index
    new_turtles.goto(x=-250, y=y_positions[turtle_index])
    all_turtles.append(new_turtles)

#     creating a code to run the turtles in the race
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            # if the winning color turtle is reached to the last of the x coordinate we will stop the race
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won the {winning_color} color turtle is the winner")
            else:
                print(f"you have lose the {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()