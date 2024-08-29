# creating a function that finds how many paints of cans we need to paint
# a wall
import math


def paint_area_calc(height,width,covarage):
    result = (height * width) /covarage
    print(f"you need {math.ceil(result)} cans to paint the wall")


paint_area_calc(5,5,6)