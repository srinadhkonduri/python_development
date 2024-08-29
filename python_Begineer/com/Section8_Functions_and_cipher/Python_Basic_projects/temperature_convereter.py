# making a temperature converter
# code for the following converter
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


print("temperature converter")
print("1 . c to f")
print("2 . f to c")

choice = input("enter your code (1/2):")
if choice == "1":
    celsius = float(input("enter temperature in celsius"))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} c is equal to {fahrenheit:.2f} F")
elif choice == "2":
    fahrenheit = float(input("enter temperature in fahrenheit"))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} f is equal to {celsius:.2f} C")
else:
    print("invalid input")
