# making a H game using the turtle graphics
# import turtle
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
tim.speed("fastest")
# creating a function that moves the turtle


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "f")
screen.onkey(move_backwards,"b")
screen.onkey(turn_left,"l")
screen.onkey(turn_right,"r")
screen.onkey(clear, "c")
screen.exitonclick()