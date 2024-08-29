# avg height in a class of 4 students

# the above method is used to take input in python

avg_height = input("enter the height : ").split()
for n in range(0,len(avg_height)):
    avg_height[n] = int(avg_height[n])
total_height = 0
for heights in avg_height:
    total_height += heights
print(total_height)


avg_student = input("enter the number of students in the class : ").split()
for n in range(0,len(avg_student)):
    avg_student[n] = int(avg_student[n])
avg_students = [1,2,3,4,5]
total_heights = 0
for number in avg_students:
    total_heights += number
print(total_heights)


avg_height_of_students = total_height / total_heights
print("the avg height if the students",round(avg_height_of_students))

# another method is by taking list comphresion

# a,b,c,d,e = [int(x) for x in input("enter the values : ").split()]
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)


