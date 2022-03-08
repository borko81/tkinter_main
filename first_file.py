import datetime
import tkinter as tk
import tkinter.messagebox as msgbox


class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "Hello"
        self.label_text = tk.Label(self, text=self.title)
        self.label_text.pack(fill=tk.BOTH, expand=True, padx=100, pady=10)
        
        self.entry_var = tk.StringVar()
        self.name_entry = tk.Entry(self, textvar=self.entry_var)
        self.name_entry.pack(fill=tk.BOTH, expand=True, padx=100, pady=20)
        self.name_entry.focus()

        hello_button = tk.Button(self, text="Say Hello",
            command=self.say_hello)
        
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        
        goodbye_button = tk.Button(self, text="Say Goodbye",
            command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
        
    def say_hello(self):
        name = self.name_entry.get()
        self.label_text.configure(text="Hello {}".format(name))
        msgbox.showinfo(f"{datetime.datetime.now().strftime('%d.%m.%Y')}", "Message box")

    def say_goodbye(self):
        self.label_text.configure(text="Say Goodbye")
        if msgbox.askyesno("Close", "Would you like to close the box"):
            self.after(2000, self.destroy)
        else:
            self.label_text.configure(text="Stay open")


if __name__ == "__main__":
    window = Windows()
    window.mainloop()
