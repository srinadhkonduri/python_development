# making a simple calculator
# function to add two numbers
def add(x, y):
    return x + y


# function to sub two numbers
def sub(x, y):
    return x - y


# function to multiply two numbers
def mul(x, y):
    return x * y


# function to div two numbers
def div(x, y):
    if y != 0:
        return x/y
    else:
        return "can't divide by zero"


# main calculator loop
while True:
    print("select operation")
    print("1 . add")
    print("2 . sub")
    print("3 . mul")
    print("4 . div")
    print("5 . quit")
    choice = input("enter choice (1/2/3/4/5):")
    if choice in ('1','2','3','4'):
        num1 = float(input("enter first number : "))
        num2 = float(input("enter second number :"))

        if choice == "1":
            print("result",add(num1,num2))
        elif choice == "2":
            print("result",sub(num1,num2))
        elif choice == "3":
            print("result",mul(num1,num2))
        elif choice == "4":
            print("result",div(num1,num2))
        elif choice == "5":
            print("goodbye")
        else:
            print("invalid output")
