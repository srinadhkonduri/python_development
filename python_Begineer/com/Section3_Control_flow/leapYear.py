# checking weather the given year is leap year or not
year = int(input("enter the following year = "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0 :
            print("leap year")
        else:
            print("not leap year")
    else:
        print("not leap year")
else:
    print("not leap year")