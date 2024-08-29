# using range function in python
# add all numbers between 1 to 100

# adding whole numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)


# adding even numbers from 1 t0 100 skipping odd numbers between
totals = 0
for range in range(0, 101, 2):
    totals += range
print(totals)