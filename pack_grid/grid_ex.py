import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("240x100")
root.title("Login")
root.resizable(0, 0)

def user_choice():
    u = username_entry.get()
    p = password_entry.get()
    print(f"{u} enter {p} for password")

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

# username
username_label = ttk.Label(root, text="Username: ")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, sticky=tk.E, padx=5, pady=5)
username_entry.focus()

# password
password_label = ttk.Label(root, text='Password: ')
password_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)

# login button
login_button = ttk.Button(root, text="Login", command=user_choice)
login_button.grid(row=2, column=1, sticky=tk.E)


# close with push esc button
root.bind('<Escape>', lambda _: root.destroy())
root.bind('<Return>', lambda _: user_choice())

if __name__ == '__main__':
    root.mainloop()