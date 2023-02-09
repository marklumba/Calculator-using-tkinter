import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(0, 0)
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("+", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("-", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("*", 3, 3)

        self.create_button("C", 4, 0)
        self.create_button("0", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("/", 4, 3)

    def create_button(self, text, row, column):
        button = tk.Button(self, text=text, font=("Arial", 20), width=5, height=2, command=lambda: self.click(text))
        button.grid(row=row, column=column)

    def click(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, text)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
