from socket import if_nameindex
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Pack Demo")
root.geometry("300x200")

label1 = tk.Label(
    root,
    text="Box 1",
    bg="red",
    fg="white"
)
label1.pack(ipadx=10, ipady=10, fill='x')

label2 = tk.Label(
    root,
    text="Box 2",
    bg="green",
    fg="white"
)
label2.pack(ipadx=10, ipady=10, fill='x')


label3 = tk.Label(
    root,
    text="Box 3",
    bg="cyan",
    fg="black"
)
label3.pack(ipadx=10, ipady=10, fill='x')

label4 = tk.Label(
    root,
    text="Left",
    bg="bisque",
    fg="black"
)
label4.pack(ipadx=10, ipady=10, fill='both', side='left', expand=True)

label5 = tk.Label(
    root,
    text="Center",
    bg="magenta",
    fg="black"
)
label5.pack(ipadx=10, ipady=10, fill='both', side='left', expand=True)

label6 = tk.Label(
    root,
    text="Right",
    bg="yellow",
    fg="black"
)
label6.pack(ipadx=10, ipady=10, side='left', expand=True, fill='both')


if __name__ == '__main__':
    root.mainloop()