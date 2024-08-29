import turtle


def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_tortoise():
    # Set up the turtle
    turtle.speed(3)
    turtle.bgcolor("white")

    # Draw the shell
    draw_circle("green", 100, 0, -50)

    # Draw the head
    draw_circle("green", 50, 0, 100)

    # Draw the legs
    draw_circle("green", 30, -70, -130)
    draw_circle("green", 30, 70, -130)
    draw_circle("green", 30, -70, -10)
    draw_circle("green", 30, 70, -10)

    # Draw the eyes
    draw_circle("white", 10, -20, 140)
    draw_circle("white", 10, 20, 140)

    # Draw the pupils
    draw_circle("black", 5, -20, 145)
    draw_circle("black", 5, 20, 145)

    # Hide the turtle and display the drawing
    turtle.hideturtle()
    turtle.done()


# Run the program
draw_tortoise()
