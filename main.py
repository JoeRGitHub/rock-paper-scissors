# Project: Rock Paper Scissors

import random

playAgain = "yes"

computer = 0
user = 0


def paper(compter_choices, user_choices, computer, user):
    if compter_choices == "rock" and user_choices == "paper":
        print(
            f"You chose {user_choices}, Computer chose {compter_choices}\nYou win!")
        user += 1
    else:
        print(
            f"You chose {user_choices}, Computer chose {compter_choices}\nYou lose!")
        computer += 1
    return computer, user


def rock(compter_choices, user_choices, computer, user):
    if compter_choices == "scissors" and user_choices == "rock":
        print(
            f"You chose {user_choices}, Computer chose {compter_choices}\nYou win!")
        user += 1
    else:
        print(
            f"You chose {user_choices}, Computer chose {compter_choices}\nYou lose!")
        computer += 1
    return computer, user


def scissors(compter_choices, user_choices, computer, user):
    if compter_choices == "paper" and user_choices == "scissors":
        print(
            f"You chose {user_choices}, Computer chose {compter_choices}\nYou win!")
        user += 1
    else:
        print(
            f"You chose {user_choices}, Computer chose {compter_choices}\nYou lose!")
        computer += 1
    return computer, user


while playAgain == "yes":

    compter_choices = random.choice(["rock", "paper", "scissors"])
    user_choices = input("Choose: rock, paper, scissors :").lower()

    if compter_choices == user_choices:
        print(
            f"You chose {user_choices}, Computer chose {compter_choices}\nTie!")
    elif user_choices == "paper":
        computer, user = paper(compter_choices, user_choices, computer, user)
    elif user_choices == "rock":
        computer, user = rock(compter_choices, user_choices, computer, user)
    elif user_choices == "scissors":
        computer, user = scissors(
            compter_choices, user_choices, computer, user)

    print(f"User Score: {user}, Computer Score: {computer}")
    playAgain = input(
        "Play again? (yes to continue, 'q' to quit): ").lower()
if computer > user:
    print("The machines won! 👾")
else:
    print("The man won! 🧔‍♂️")
