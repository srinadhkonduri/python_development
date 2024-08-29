# making a greet function
# simple function
def my_greet():
    print("hello world")


# always return the function after 2 blank lines

my_greet()

print("------------------------------")

# function that allows for input

def greet_with_name(name):
    print(f"hello {name}")
    print(f"how do you do {name}")


greet_with_name("srinadh")

print("---------------------------------")

# function with two parameters

def great_with(name, localtion):
    print(f"hello {name}")
    print(f"you are in {localtion}")


great_with("srinadh", "hydrabad")

print("----------------------------------------")

# keyword arguments in python functions
def greets(a,b,c):
    print(f"the valule of a is {a}")
    print(f"the value of b is {b}")
    print(f"the value of c is {c}")


greets(a=3, b=2, c=1)