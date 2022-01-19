import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image = [rock, paper, scissors]
a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if a>=3 or a<0:
    print("You inputed an invalid number : you lose!")
else:
    print(image[a])
    b = random.randint(0, 2)
    print("The computer chose:")
    print(image[b])

    if a == b:
        print("Draw")
    elif a == 0 and b == 1:
        print("You lose")
    elif a == 0 and b == 2:
        print("You win")
    elif a == 1 and b == 0:
        print("You win")
    elif a == 1 and b == 2:
        print("You lose")
    elif a == 2 and b == 0:
        print("You lose")
    elif a == 2 and b == 1:
        print("You win")

