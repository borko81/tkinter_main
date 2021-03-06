import tkinter as tk
from tkinter import ttk
import itertools


root = tk.Tk()

paddy = {"padx": 100, "pady": 50}


def button_clicked():
    print("Button was clicked")


def select(option):
    print(option)


def return_presses(event):
    print("return key pressed")


choice = "Rock Paper Scissors".split()
cycke = itertools.cycle(choice)

label = tk.Label(root)
label["text"] = "Hello"
label.pack()

button = tk.Button(root)
button.config(text="button")
button.config(**paddy)
button.config(command=lambda: select(next(cycke)))
button.bind('<Return>', return_presses)
button.focus()
button.pack()

root.mainloop()
