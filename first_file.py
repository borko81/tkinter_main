import tkinter as tk


class Windows(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "Hello"
        self.label_text = tk.Label(self, text=self.title)
        self.label_text.pack(fill=tk.BOTH, expand=True, padx=100, pady=50)

        hello_button = tk.Button(self, text="Say Hello",
            command=self.say_hello)
        
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        
        goodbye_button = tk.Button(self, text="Say Goodbye",
            command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
        
    def say_hello(self):
        self.label_text.configure(text="Say Hello")

    def say_goodbye(self):
        self.label_text.configure(text="Say Goodbye")
        self.after(2000, self.destroy)


if __name__ == "__main__":
    window = Windows()
    window.mainloop()
