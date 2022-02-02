import os

logo = ''' 
 _____________________
|  _________________  |                                     
| | Montek       0. | |
| |_________________| | ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
|  ___ ___ ___   ___  | ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗            
| | 7 | 8 | 9 | | + | | ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
| |___|___|___| |___| | ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
| | 4 | 5 | 6 | | - | | ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
| |___|___|___| |___| | ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| | 
|_____________________| 
                        
                                              
'''

print(logo)


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate():
    n1 = float(input("What's the first number: "))

    for symbol in operations:
        print(symbol)
    user_continue = True
    while user_continue:
        user_choice = input("Pick an operation from above\n")
        n2 = float(input("What's the next number: "))
        calc = operations[user_choice]
        answer = calc(n1, n2)
        print(f"{n1} {user_choice} {n2} = {answer}")
        user_choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type end to stop: ")
        if user_choice == 'y':
            n1 = answer
        elif user_choice == 'n':
            user_continue = False
            calculate()
        elif user_choice == 'end':
            user_continue = False
            os.system("pause")

calculate()
