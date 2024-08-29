student_dict = {
    "student": ["a", "b", "c"],
    "score": [45, 56, 67]
}
# looping through the dictionary
# for (key , value) in student_dict.items():
#     print(value)


# looping through the dictionary using pandas
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)