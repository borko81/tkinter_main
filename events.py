import tkinter as tk
from tkinter import ttk
import itertools


root = tk.Tk()
root.title("Demo pack")
root.geometry("300x350")

def show_me(event):
    print(e.get())

e = tk.Entry(root)
e.bind('<Key>', show_me)
e.focus()
e.pack()

box1 = tk.Label(root,text="Box 1",bg="green",fg="white")

box1.pack(
    ipadx=10,
    ipady=10,
    expand=True,
    fill='both',
    side='left'
)

box2 = tk.Label(root, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=10, fill='both', expand=True)

root.mainloop()