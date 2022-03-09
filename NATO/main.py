

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
p_dic = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("Enter a word: \n").upper()
output = [p_dic[letter] for letter in word]
print(output)