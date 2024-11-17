import tkinter as tk
import math

# Creating the root window
root = tk.Tk()
root.title("Advanced Calculator")
root.configure(bg='#d6e0f5')  # Light background color

# Variables
expression = ""
input_text = tk.StringVar()
dark_mode = False

# Function to update expression in the entry box
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the entry box
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the expression
def btn_equal():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Function to calculate square root
def btn_sqrt():
    try:
        global expression
        result = str(math.sqrt(float(expression)))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Function to toggle dark mode
def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.configure(bg='#2e2e2e')  # Dark background color
        input_field.configure(bg='#4a4a4a', fg='white')
    else:
        root.configure(bg='#d6e0f5')  # Light background color
        input_field.configure(bg='white', fg='black')

# Creating the entry field
input_field = tk.Entry(root, textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4, bg='white', fg='black')
input_field.grid(row=0, column=0, columnspan=4)

# Memory storage for M+, M-, MR, MC
memory = 0

# Memory functions
def btn_m_plus():
    global memory, expression
    if expression:
        memory += float(expression)

def btn_m_minus():
    global memory, expression
    if expression:
        memory -= float(expression)

def btn_mr():
    input_text.set(str(memory))

def btn_mc():
    global memory
    memory = 0

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('sqrt', 5, 0), ('M+', 5, 1), ('M-', 5, 2), ('MR', 5, 3),
    ('MC', 6, 0), ('%', 6, 1), ('**', 6, 2), ('Dark Mode', 6, 3)
]

# Adding buttons to the calculator
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_equal)
    elif text == "C":
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_clear)
    elif text == "sqrt":
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_sqrt)
    elif text == "M+":
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_m_plus)
    elif text == "M-":
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_m_minus)
    elif text == "MR":
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_mr)
    elif text == "MC":
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=btn_mc)
    elif text == "Dark Mode":
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=toggle_mode)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'), command=lambda txt=text: btn_click(txt))
    button.grid(row=row, column=col)

# Key Bindings
root.bind('<Return>', lambda event: btn_equal())  # Enter key for "="
root.bind('<BackSpace>', lambda event: btn_clear())  # Backspace key for "C"

# Start the GUI event loop
root.mainloop()
