# drawing a dashed line using python turtle graphics
import turtle as t
tim = t.Turtle()
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()