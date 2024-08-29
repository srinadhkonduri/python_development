# check height 120 cm and check age > 18 < 18 == 18
bill = 0
height = int(input("enter your height in cm = "))
if height >= 120:
    print("you can ride the roller coaster")
    age = int(input("enter your age = "))
    if age < 12:
        bill = 5
        print("you should pay $5")
    elif age <= 18:
        bill = 7
        print("you should pay $7")
    elif 45 >= age >= 55:
        print("you should pay $0 you are free of cost to ride in the roller coaster")
    else:
        # this statement consider as adult
        print("you should pay $12")

    want_photos = input("do you want photos = ")
    if want_photos == "y":
        bill += 3
        print(f"your total bill is {bill}")
else:
    print("you cannot ride the roller coaster")