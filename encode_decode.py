import os

logo = ''' 

███████╗███╗░░██╗░█████╗░░█████╗░██████╗░███████╗  ██████╗░███████╗░█████╗░░█████╗░██████╗░███████╗
██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
█████╗░░██╔██╗██║██║░░╚═╝██║░░██║██║░░██║█████╗░░  ██║░░██║█████╗░░██║░░╚═╝██║░░██║██║░░██║█████╗░░
██╔══╝░░██║╚████║██║░░██╗██║░░██║██║░░██║██╔══╝░░  ██║░░██║██╔══╝░░██║░░██╗██║░░██║██║░░██║██╔══╝░░
███████╗██║░╚███║╚█████╔╝╚█████╔╝██████╔╝███████╗  ██████╔╝███████╗╚█████╔╝╚█████╔╝██████╔╝███████╗
╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═════╝░╚══════╝  ╚═════╝░╚══════╝░╚════╝░░╚════╝░╚═════╝░╚══════╝ '''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B'
            , 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',',
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '`', '[', ']', ';', '"', '\\', '\'', '/', '{', '}', ':', '|', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B'
            , 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',',
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '`', '[', ']', ';', '"', '\\', '\'', '/', '{', '}', ':', '|', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', '0']
print(logo + '\n')


def cipher(user_text, user_shift, user_direction):
    final_text = ""
    if user_direction == 'decode':
        user_shift *= -1
    for char in user_text:
        if char in alphabet:
            position = alphabet.index(char)
            change = position + user_shift
            final_text += alphabet[change]
        else:
            final_text += char
    print(f"The {user_direction}d text is: {final_text}\n")


continue_program = True
while continue_program:
    input_direction = True
    while input_direction:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode' or direction == 'decode':
            input_direction = False
        else:
            print("Invalid input. Type again!")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    shift = shift % 176

    cipher(user_text=text, user_shift=shift, user_direction=direction)

    ask = input("Type \'yes\' to go again. Otherwise type \'no\'.\n")
    if ask == 'no':
        continue_program = False
        print("\n-------------Goodbye-------------")
        os.system("pause")

# def encrypt(user_text, user_shift):
#     cipher = ""
#     for letter in user_text:
#         position = alphabet.index(letter)
#         change = position + user_shift
#         change_letter = alphabet[change]
#         cipher += change_letter
#     print(f"The encoded text is {cipher}")
#
#
# def decrypt(cipher, user_shift):
#     decrypted_cipher = ""
#     for letter in cipher:
#         position = alphabet.index(letter)
#         change = position - user_shift
#         change_letter = alphabet[change]
#         decrypted_cipher += change_letter
#     print(f"The decoded text is {decrypted_cipher}")


# if direction == 'encode':
#     encrypt(user_text=text, user_shift=shift)
# elif direction == 'decode':
#     decrypt(cipher=text, user_shift=shift)
