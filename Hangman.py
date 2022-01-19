import random
# import only system from os
from os import system, name

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print(logo)
chosen_word = input("shhh input the secret word!\n")
display_list = []
word_length = len(chosen_word)
print(f"The chosen word is {chosen_word}")
for blank in range(word_length):
    display_list += "_"
print(display_list)
end = False
lives_left = 6
while not end:


    guess = input("Guess a letter\n").lower()
    # clear()
    if guess in display_list:
        print(f"You've already guessed {guess}, try another letter.")
    # check guessed letter

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display_list[position] = letter
    print(display_list)
    # check for wrong guess
    if guess not in chosen_word:
        lives_left -= 1
        print(f"You guessed {guess}, which is wrong. You loose a life. \nLives left : {lives_left}")
        if lives_left == 0:
            end = True
            print("You lose!")
    # check if word is guessed if the blanks are cleared
    if "_" not in display_list:
        end = True
        print("You win!")
    print(stages[lives_left])
