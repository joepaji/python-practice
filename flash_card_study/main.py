#!/usr/bin/env python3
from utils import *
import tkinter
import pandas
import random

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def correct_action():
    words_to_learn.remove(current_card)
    next_card()

def wrong_action():
    next_card()

BACKGROUND_COLOR = "#B1DDC6"
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

data = pandas.read_csv('data/french_words.csv')
words_to_learn = data.to_dict(orient="records")
current_card = random.choice(words_to_learn)

canvas = tkinter.Canvas(width=800, height=526)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263, text="", font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

canvas.itemconfig(canvas_image, image=card_back_img)

wrong_image = tkinter.PhotoImage(file='images/wrong.png')
wrong_button = tkinter.Button(image=wrong_image,highlightthickness=0, command=wrong_action)
wrong_button.grid(row=1, column=0)

correct_image = tkinter.PhotoImage(file='images/right.png')
correct_button = tkinter.Button(image=correct_image, highlightthickness=0, command=correct_action)
correct_button.grid(row=1, column=1)

next_card()

window.mainloop()