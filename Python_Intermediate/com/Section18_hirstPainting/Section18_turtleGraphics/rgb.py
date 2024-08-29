import turtle as t
import random

tim = t.Turtle()

# creating a rgb color generator


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
# pensize is used to thick the pointer
tim.pensize(15)
# speed is used to increase the speed of the pointer
tim.speed("fastest")

for _ in range(200):
    tim.color(random_colors())
    tim.forward(30)
    tim.setheading(random.choice(directions))