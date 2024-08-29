# given a list finding the highest score in the list

# score = [12,34,56,70,99,98,54,23,45]
# this is the actual way to take multiple inputs from the user
score = input("enter the values : ").split()
for n in range(0,len(score)):
    score[n] = int(score[n])

highest_score = 0
for highest in score:

    # this is the formula for calculating the highest score
    if highest > highest_score:
        highest_score = highest
        print(highest_score)

print(f"the highest score in the list is {highest_score}")