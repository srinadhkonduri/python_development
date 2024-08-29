# creating a turtle graphics called import turtle graphics
# importing the turtle module
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)

my_screen = Screen()
print(my_screen)
my_screen.getshapes()
my_screen.exitonclick()

from prettytable import prettytable
table = prettytable()
table.add_column("pokemon name",["pikachu","charminder","blastoise"])
print(table)