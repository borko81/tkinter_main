import itertools
import tkinter as tk
import tkinter.ttk as ttk


style_1 = {
    "fg": "red",
    "bg": "black",
    "activebackground": "gold",
    "activeforeground": "dim gray",
}
style_2 = {
    "fg": "yellow",
    "bg": "grey",
    "activebackground": "chocolate",
    "activeforeground": "blue4",
}

style_cycle = itertools.cycle([style_1, style_2])
style = ttk.Style()

def switch_style():
    style = next(style_cycle)
    button.configure(**style)


win = tk.Tk()

label = tk.Label(win, text="Some kind of text is here", style="TButton")
label.pack()
button = tk.Button(win, text="Button", command=switch_style)
button.pack(padx=100, pady=50)

win.mainloop()
