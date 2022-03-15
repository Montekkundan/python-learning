from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
learn_word = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    learn_word = original_data.to_dict(orient="records")
else:
    learn_word = data.to_dict(orient="records")


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn_word)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def known_cards():
    learn_word.remove(current_card)
    data = pandas.DataFrame(learn_word)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white", )
    canvas.itemconfig(card_background, image=back_img)


window = Tk()
window.title("Flash Card")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, borderwidth=0, command=next_word)
cross_button.grid(row=1, column=0)
check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, borderwidth=0, command=known_cards)
check_button.grid(row=1, column=1)
flip_timer = window.after(3000, func=flip_card)
next_word()
window.mainloop()
