from threading import main_thread
from tkinter import Tk, Text, ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText



class App(Tk):

    def __init__(self):
        super().__init__()
        self.title('ScrolledText')
        l = tk.Label(self, text="Text processing")
        l.pack()
        s = ScrolledText(self, width=50, height=10)
        s.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        s.insert('1.0', 'Write something\n')
        separator = ttk.Separator(self, orient='horizontal')
        separator.pack(fill='x')
        s.focus()
        self.bind('<Escape>', s.destroy)

if __name__ == '__main__':
    app = App()
    app.mainloop()