import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
p_dic = {row.letter: row.code for (index, row) in data.iterrows()}


def generarte():
    word = input("Enter a word: \n").upper()
    try:
        output = [p_dic[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generarte()
    else:
        print(output)


generarte()
