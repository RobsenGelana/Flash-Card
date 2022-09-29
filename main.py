from email.mime import image
from tkinter import *
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"
#-----------------READING CSV FILE ------------------------#
data = pd.read_csv('data/french_words.csv')
df = data['English']
print(df)

#-----------------------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text="Word", font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file='images/right.png')
right = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR)
right.grid(column=1, row=1)

wrong_image = PhotoImage(file='images/wrong.png')
wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong.grid(row=1, column=0)





window.mainloop()
