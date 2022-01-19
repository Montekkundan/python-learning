# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
r_letters = int(input("How many letters would you like in your password?\n"))
r_symbols = int(input(f"How many symbols would you like?\n"))
r_numbers = int(input(f"How many numbers would you like?\n"))

pwd = []
for char in range(1, r_letters + 1):
    pwd.append(random.choice(letters))
for char in range(1, r_symbols + 1):
    pwd.append(random.choice(symbols))
for char in range(1, r_numbers + 1):
    pwd.append(random.choice(numbers))

random.shuffle(pwd)
password = ""
for char in pwd:
    password += char
print(f"Password is {password}")
