import random
from os import system, name

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def dealing_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for a in range(2):
        user_cards.append(dealing_cards())
        computer_cards.append(dealing_cards())

    while not game_over:
        user_score = calculate(user_cards)
        computer_score = calculate(computer_cards)
        print(f"Your cards, {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else:
            user_ask = input("Type 'y' to get another card or type 'n' to pass: ")
            if user_ask == 'y':
                user_cards.append(dealing_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(dealing_cards())
        computer_score = calculate(computer_cards)
    print(f" Your final hand: {user_cards}, your final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == 'y':
    clear()
    game()
