# raising our own exceptions
height = float(input("enter the height = "))
weight = int(input("enter your weight = "))

# here we are raising our own exceptions i the case
if height > 3:
    raise ValueError("human height should not be greater than 3 meters")

bmi = weight / height ** 2

print(bmi)
