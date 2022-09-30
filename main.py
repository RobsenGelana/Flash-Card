from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
#-----------------READING CSV FILE ------------------------#
df = pd.read_csv('data/french_words.csv')
to_learn = df.to_dict(orient='records')
current_card = {}

def random_word():
   global current_card
   current_card = random.choice(to_learn)
   canvas.itemconfig(card_title, text="French")
   canvas.itemconfig(card_word, text=current_card['French'])
#-----------------------------------------------------------#
#--------------------FLIP CARD -----------------------------#
def flip_card():
   canvas.itemconfig(card_title, text='English')
   canvas.itemconfig(card_word, text=current_card['English'])

#-----------------------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'normal'))
card_word = canvas.create_text(400, 263, text=f"word", font=('Ariel', 60, 'normal'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file='images/right.png')
right = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_word)
right.grid(column=1, row=1)

wrong_image = PhotoImage(file='images/wrong.png')
wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_word)
wrong.grid(row=1, column=0)

random_word()


window.mainloop()
