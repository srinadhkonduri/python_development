# creating student grades

student_scores = {
    "srinadh" : 88,
    "radha" : 94,
    "chaitu" : 90,
    "sureedu" : 99,
    "shiva" : 96
}

# creating an empty dictionary
student_grades = {}
# score = 0
# looping through every student

for student in student_scores:
    score = student_scores[score]
    if score > 90:
        student_grades[student] = "outstanding"
    elif score > 80:
        student_grades[student] = "acceptable"
    elif score > 70:
        student_grades[student] = "need to improve"

print(student_scores)