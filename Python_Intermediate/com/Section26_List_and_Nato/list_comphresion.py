numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)
name = "srinadh"
new_name = [letter for letter in name]
print(new_name)
double_number = [num * 9 for num in range(1,5)]
print(double_number)

names = ['a', 'b', 'c', 'd', 'e']
new_names = [name for name in names if len(names) < 5]
print(new_names)