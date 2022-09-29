from cgitb import text
from tkinter import *
import pandas as pd
import time
import random

BACKGROUND_COLOR = "#B1DDC6"
#-----------------READING CSV FILE ------------------------#
df = pd.read_csv('data/french_words.csv')
to_learn = df.to_dict(orient='records')
def random_word():
   current_card = random.choice(to_learn)
   canvas.itemconfig(card_title, text="French")
   canvas.itemconfig(card_word, text=current_card['French'])
   
#-----------------------------------------------------------#
#print(f'{random_word()}')

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file='images/card_front.png')
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
