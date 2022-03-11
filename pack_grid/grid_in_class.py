from socket import if_nameindex
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("240x100")
        self.title("Login")
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.create_widgets()

    def create_widgets(self):
        self.e = tk.Entry(self, text="Enter something")
        self.e.grid(row=0, column=0)

        self.b = tk.Button(self, text="Button", command=self.my_func)
        self.b.grid(row=0, column=1)

    def my_func(self):
        print(self.e.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()
