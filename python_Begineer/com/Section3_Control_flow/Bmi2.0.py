# checking the body mass index

weight = int(input("enter you weight = "))
height = float(input("enter your height in meters = "))

bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi}, you are under weight")
elif bmi < 25:
    print(f"your bmi is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are slightly over weight")
elif bmi < 35:
    print(f"your bmi is {bmi}, you are obese")
else:
    print(f"your bmi is {bmi}, you are really obese")