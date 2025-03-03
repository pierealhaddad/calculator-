import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title('Simple Calculator')

# Create a frame to hold the calculator components
container = tk.Frame(root, bg="lightblue", padx=10)
container.pack()

# Input field for calculations
input_field = tk.Entry(container, relief=tk.SUNKEN, borderwidth=3, width=30)
input_field.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

def insert_value(value):
    """Inserts the clicked button value into the entry field."""
    input_field.insert(tk.END, value)

def evaluate_expression():
    """Evaluates the mathematical expression entered and displays the result."""
    try:
        result = str(eval(input_field.get()))
        input_field.delete(0, tk.END)
        input_field.insert(0, result)
    except Exception:
        messagebox.showerror("Error", "Invalid Expression")

def clear_entry():
    """Clears the input field."""
    input_field.delete(0, tk.END)

# Define button labels and their respective positions
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1),
    ('+', 5, 0), ('-', 5, 1), ('*', 5, 2),
    ('/', 6, 0)
]

# Create and position numeric and operator buttons
for (text, row, col) in buttons:
    button = tk.Button(container, text=text, padx=15, pady=5, width=3, command=lambda t=text: insert_value(t))
    button.grid(row=row, column=col, pady=2)

# Special buttons for clear and equals operations
tk.Button(container, text="Clear", padx=15, pady=5, width=12, command=clear_entry).grid(row=6, column=1, columnspan=2, pady=2)
tk.Button(container, text="=", padx=15, pady=5, width=9, command=evaluate_expression).grid(row=7, column=0, columnspan=3, pady=2)

# Run the Tkinter event loop
root.mainloop()