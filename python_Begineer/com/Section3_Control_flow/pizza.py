# you want to buy a pizza in your shop add topings according to your choice

print("welcome to srinadh pizza what would you like to have sir")
bill = 0;
pizza_size = input("enter the size of the pizza ")

if pizza_size == "s":
    bill = 200
    print(f"you ordered small pizza the price of the pizza is {bill + 20}")
elif pizza_size == "m":
    bill = 400
    print(f"you ordered medium pizza the price of the pizza is {bill + 30}")
else:
    bill = 600
    print(f"you ordered large  pizza the  price of the pizza is {bill + 40}")
