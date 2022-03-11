from tkinter import Tk, Text, ttk
import tkinter as tk

root = Tk()

def show_input_text():
    t = text.get('2.0', 'end')
    # for line in t.split('\n'):
    #     print(line.strip())
    print(t)


root.resizable(False, False)
root.title("Text Widget Example")

f = ttk.Frame(root)
f.grid(column=0, row=0)

text = Text(f, height=10, fg='red')
text.focus()
text.pack()
text.insert('1.0', "Enter something:")

b = tk.Button(f, text="Show", command=show_input_text)
b.pack(fill='x', expand=True)

scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.grid(row=0, column=1, sticky='NS')
text['yscrollcommand'] = scrollbar.set

root.bind('<Return>', lambda _: show_input_text())

root.mainloop()