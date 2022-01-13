from tkinter import *
import pandas as pd
import random
from tkinter import messagebox
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
# -------------------------- Data reading -------------------------------------#
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    words_list = data.to_dict(orient="records")
else:
    words_list = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_list)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


# noinspection PyTypeChecker
def is_known():
    words_list.remove(current_card)
    if len(words_list) == 0:
        messagebox.showinfo(title="Done", message="Now you should know all the words")
        os.remove("data/words_to_learn.csv")
        window.quit()
    else:
        data_for_csv = pd.DataFrame(words_list)
        data_for_csv.to_csv("data/words_to_learn.csv", index=False)
        next_card()
# -------------------------- UI ------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)


# card canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2, sticky="EW")

# buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known = Button(image=check_image, highlightthickness=0, command=is_known)
known.grid(row=1, column=1)

next_card()

window.mainloop()