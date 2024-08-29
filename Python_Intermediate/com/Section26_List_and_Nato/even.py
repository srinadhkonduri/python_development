list_of_string = ['1', '2', '3', '4', '5', '6', '7']
numbers = [int(x) for x in list_of_string]
print(numbers)
odd_numbers = [num for num in numbers if num % 2 == 1]
print(odd_numbers)
