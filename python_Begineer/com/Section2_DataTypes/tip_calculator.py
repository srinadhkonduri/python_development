print("welcome to the bill calculator")
bill = float(input("enter the bill amount = "))
tip = float(input("how much tip you would like to give = "))

number_of_person = float(input("enter the number of persons you want to split the bill = "))
# this is the main formula of calculating the tip
final_price = bill * (1 + tip / 100)
print(final_price)
