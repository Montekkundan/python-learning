print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
import os
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\" \n")
if direction.lower() == "left":
    way = input("You\'ve come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. ""Type \"swim\" to swim "
                "across.\n")
    if way.lower() == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you "
                     "choose?\n")
        if door.lower() == "yellow":
            print("You found the treasure! You Win!")
            os.system("pause")
        elif door.lower() == "red":
            print("It's a room full of fire. YOU DIED!")
            print("-------- GAME OVER --------")
            os.system("pause")
        elif door.lower() == "blue":
            print("You enter a room of beasts. YOU DIED!")
            print("-------- GAME OVER --------")
            os.system("pause")
        else:
            print("You chose a door that doesn't exist.")
            print("-------- GAME OVER --------")
            os.system("pause")
    else:
        print("You are attacked by a trout. YOU DIED!")
        print("-------- GAME OVER --------")
        os.system("pause")
else:
    print("You've fallen into a hole. YOU DIED!")
    print("-------- GAME OVER --------")
    os.system("pause")
