import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        
        # create the entry widget to display the calculations
        self.display = tk.Entry(self.master, width=30, font=('Arial', 14), borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # create the buttons for the calculator
        self.create_button('1', 1, 0)
        self.create_button('2', 1, 1)
        self.create_button('3', 1, 2)
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('7', 3, 0)
        self.create_button('8', 3, 1)
        self.create_button('9', 3, 2)
        self.create_button('0', 4, 1)
        self.create_button('.', 4, 2)
        self.create_button('C', 4, 0)
        self.create_button('+', 1, 3)
        self.create_button('-', 2, 3)
        self.create_button('*', 3, 3)
        self.create_button('/', 4, 3)
        self.create_button('=', 5, 3)
        
        # keep track of the calculation
        self.current_calculation = ''
        
    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, padx=20, pady=10, font=('Arial', 12),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=col)
        
    def button_click(self, text):
        if text == 'C':
            # clear the display
            self.display.delete(0, tk.END)
            self.current_calculation = ''
        elif text == '=':
            try:
                # evaluate the current calculation and display the result
                result = str(eval(self.current_calculation))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.current_calculation = result
            except:
                # if the calculation is invalid, clear the display and start over
                self.display.delete(0, tk.END)
                self.current_calculation = ''
        else:
            # add the clicked button's text to the current calculation and display it
            self.current_calculation += text
            self.display.insert(tk.END, text)

# create the GUI window
root = tk.Tk()

# create the calculator app
calculator = Calculator(root)

# start the event loop
root.mainloop()

