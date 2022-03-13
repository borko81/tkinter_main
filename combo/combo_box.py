import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

root = tk.Tk()
root.geometry("300x200")
root.resizable(0, 0)
root.title("Combobox Widget")

label = ttk.Label(root, text="Please select a month:")
label.pack(fill=tk.X, padx=5, pady=5)

select_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=select_month)
month_cb.pack(fill=tk.X, padx=5, pady=5)
month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]
month_cb['state'] = 'readonly'


def month_changed(event):
    showinfo(
        title='Result',
        message=f'You select {month_cb.get()}'
    )

month_cb.bind('<<ComboboxSelected>>', month_changed)
current_month = datetime.datetime.now().strftime("%b")
month_cb.set(current_month)


if __name__ == '__main__':
    root.mainloop()