from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
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
machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

machine_on = True
print(logo)
while machine_on:
    print("\x1B[3mType 'off' to turn off machine. Type 'report' to see the resources of the machine\x1B[0m")
    print("\x1B[3mType 'reset' to reset the resources of the machine\x1B[0m")
    user_choice = input(f"What would you like? ({menu.get_items()}):\n")
    if user_choice == "off":
        machine_on = False
        print("\n-------------Goodbye-------------")
        os.system("pause")
    elif user_choice == "report":
        coffee_machine.report()
        machine.report()
        print("")
    elif user_choice == 'reset':
        coffee_machine.reset()
    else:
        coffee = menu.find_drink(user_choice)
        if coffee_machine.is_resource_sufficient(coffee) and machine.make_payment(coffee.cost):
            coffee_machine.make_coffee(coffee)


