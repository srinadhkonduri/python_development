# creating a number guessing game
# choosing a random number between 1 and 100
# make the function to set difficulty level
# guessing number is actual matching the computer number
# track the number of turns and reduce it by one if they get wrong
from random import randint

# function to check user answer to actual answer
# declaring some global variables in the code
HARD_LEVEL = 5
EASY_LEVEL = 10


def check_answer(guess, answer, turns):
    if answer > guess:
        print("to high")
        return turns -1
    elif answer < guess:
        print("to low")
        return turns -1
    else:
        print(f"you got it the answer is {answer}")


# make function to set difficulty
def set_difficulty():
    level = input("select a level 'easy or 'hard' ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


# making this code whole function to run again
def game():
    print("welcome to number guessing game")
    print("i am thinking a number between 1 to 100")
    answer = randint(1, 100)
    # print(answer)

    # making the code to set difficult
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"you have {turns} number of turns left to guess the number")
        # let user get the number
        guess = int(input("make a guess = "))
        # actually you have to track the number of attempts and every time
        # you should reduce it by one
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you have lost the game ")
            return
        elif guess != answer:
            print("guess again")


game()
