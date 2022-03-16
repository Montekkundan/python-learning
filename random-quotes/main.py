from tkinter import *
import requests


def get_quote():
    response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
    response.raise_for_status()
    json_data = response.json()
    data = json_data['data']
    quote = data[0]["quoteText"]
    author = data[0]["quoteAuthor"]
    canvas.itemconfig(quote_text, text=quote)
    window.title(f"{author} says...")


window = Tk()
window.title("Random Quote...")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=300, height=414, bg="white", highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Random Quote", width=250, font=("Arial", 18, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

next_img = PhotoImage(file="next_button.png")
next_button = Button(image=next_img, highlightthickness=0, command=get_quote, borderwidth=0)
next_button.grid(row=1, column=0)

window.mainloop()
