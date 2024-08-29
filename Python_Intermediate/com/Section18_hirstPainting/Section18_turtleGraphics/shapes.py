# drawing different shapes in maths using turtle
# first while drawing any shape or coding in the turtle module
# we need to import the turtle module for sure
import turtle as t
import random
# we should give a name to the turtle
tim = t.Turtle()
# here we are drawing an 8 number of side shape

# how many sides we want should be defined
# num_sides = 7

# importing the color for the shapes that we have drawn so far
colors = ["black"]
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(50)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)