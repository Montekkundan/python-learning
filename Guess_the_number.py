import random
import os

logo = '''

░██████╗░██╗░░░██╗███████╗░██████╗░██████╗  ████████╗██╗░░██╗███████╗
██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝  ╚══██╔══╝██║░░██║██╔════╝
██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░  ░░░██║░░░███████║█████╗░░
██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗  ░░░██║░░░██╔══██║██╔══╝░░
╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝  ░░░██║░░░██║░░██║███████╗
░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░
████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗
██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝                                                                                                                                                 
                                                                                                                                                           
'''

easy_difficulty = 10
hard_difficulty = 5


def check(guess, answer, turns):
    """Checks the answer, returns the number of turns left."""
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
        os.system("pause")


def difficulty():
    asking_user = True
    while asking_user:
        user_choice = input("Choose a difficulty 'easy' or 'hard': \n").lower()
        if user_choice == "easy":
            asking_user = False
            return easy_difficulty

        elif user_choice == "hard":
            asking_user = False
            return hard_difficulty

        else:
            print("Invalid input, type again!")


print(logo)


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)

    turns = difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check(guess, answer, turns)
        if turns == 0:
            print("You run out of guesses, you lose!")
            print(f"The answer was: {answer}")
            os.system("pause")
            return

game()
