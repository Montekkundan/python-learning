import os

logo = '''
                       .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' montek.
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'

'''

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
resources_copy = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def input_number(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Please type a number!")
            continue
        else:
            return user_input
            break


def is_resource(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f"Sorry there is not enough {items}.\n")
            return False
    return True


def process_money(choice, money):
    """Returns the total calculated from money inserted."""
    print(f"Your {choice} costs: {money}.")
    print("Please insert money.")
    total = input_number("how many 10 rupee notes?: ") * 10
    total += input_number("how many 20 rupee notes?: ") * 20
    total += input_number("how many 50 rupee notes?: ") * 50
    total += input_number("how many 100 rupee notes?: ") * 100
    return total


def transaction_successful_or_not(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.\n")
        return False


def coffee_maker(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item_copy in order_ingredients:
        resources[item_copy] -= order_ingredients[item_copy]
    print(f"Here is your {drink_name} . Enjoy!\n")


machine_on = True
print(logo)
while machine_on:
    spell_check = True
    while spell_check:
        print("\x1B[3mType 'off' to turn off machine. Type 'report' to see the resources of the machine\x1B[0m")
        print("\x1B[3mType 'reset' to reset the resources of the machine\x1B[0m")
        user_choice = input("What would you like? (espresso, latte, cappuccino).\n").lower()
        if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino" or user_choice == "off" or user_choice == "report" or user_choice == "reset":
            spell_check = False
        else:
            print("Invalid input! Type again.")
    if user_choice == "off":
        machine_on = False
        print("\n-------------Goodbye-------------")
        os.system("pause")
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}\n")
    elif user_choice == 'reset':
        for item in drink["ingredients"]:
            resources[item] = resources_copy[item]
        print("")
    else:
        drink = MENU[user_choice]
        if is_resource(drink["ingredients"]):
            payment = process_money(user_choice, drink["cost"])
            if transaction_successful_or_not(payment, drink["cost"]):
                coffee_maker(user_choice, drink["ingredients"])
