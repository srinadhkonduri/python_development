# checking if a number is divisible by 3 5 and 15

# target = 100
input = input("enter the following number").split()
for i in range(0 ,len(input)):
    input[i] = int(input[i])
for input in range(0 , 101):
    if input % 3 == 0 and input % 5 == 0:
        print("fizzbuzz")