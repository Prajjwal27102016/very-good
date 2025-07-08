from tkinter import *


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("615x690+400+100")
        self.root.configure(bg="#00ffea")

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.main_frame = Frame(self.root, bd=18, relief=RIDGE, bg="#FF00D9")
        self.main_frame.grid(sticky="nsew")
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        self.wigetframe = Frame(self.main_frame, bd=0, bg="#00ffea")
        self.wigetframe.grid(sticky="nsew")
        for i in range(6):  # 1 for display, 5 for buttons
            self.wigetframe.rowconfigure(i, weight=1)
        for j in range(4):
            self.wigetframe.columnconfigure(j, weight=1)

        self.lblDisplay = Label(self.wigetframe, width=30, height=2, bg='white', font=('arial', 24, 'bold'), anchor='e')
        self.lblDisplay.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.input_button = ""

        # Row 1
        self.create_buttons("←", 1, 0)
        self.create_buttons("CE", 1, 1)
        self.create_buttons("C", 1, 2)
        self.create_buttons("±", 1, 3)
        # Row 2
        self.create_buttons("7", 2, 0)
        self.create_buttons("8", 2, 1)
        self.create_buttons("9", 2, 2)
        self.create_buttons("+", 2, 3)
        # Row 3
        self.create_buttons("4", 3, 0)
        self.create_buttons("5", 3, 1)
        self.create_buttons("6", 3, 2)
        self.create_buttons("-", 3, 3)
        # Row 4
        self.create_buttons("1", 4, 0)
        self.create_buttons("2", 4, 1)
        self.create_buttons("3", 4, 2)
        self.create_buttons("×", 4, 3)
        # Row 5
        self.create_buttons("0", 5, 0)
        self.create_buttons(".", 5, 1)
        self.create_buttons("/", 5, 2)
        self.create_buttons("=", 5, 3)

    def create_buttons(self, value, row, column):
        btn = Button(
            self.wigetframe,
            text=value,
            font=('arial', 22, 'bold'),
            command=lambda v=value: self.button_click(v)
        )
        btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

    def button_click(self, text):
        if text == "←":
            self.input_button = self.input_button[:-1]
        elif text == "CE" or text == "C":
            self.input_button = ""
        elif text == "=":
            try:
                # Replace × and ÷ with * and / for eval
                expression = self.input_button.replace("×", "*").replace("/", "/")
                self.input_button = str(eval(expression))
            except Exception:
                self.input_button = "0"
        elif text in ("+", "-", "×", "/", ".", "±") or text.isdigit():
            self.input_button += text
        self.lblDisplay.config(text=self.input_button)


root = Tk()
app = Calculator(root)
root.mainloop()


