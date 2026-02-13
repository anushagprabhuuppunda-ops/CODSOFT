import tkinter as tk
from tkinter import messagebox

# Function to perform calculation
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")
root.resizable(False, False)

# Labels & Entries
tk.Label(root, text="Enter First Number").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Buttons
tk.Button(root, text="+", width=5, command=lambda: calculate("+")).pack(pady=5)
tk.Button(root, text="-", width=5, command=lambda: calculate("-")).pack(pady=5)
tk.Button(root, text="×", width=5, command=lambda: calculate("*")).pack(pady=5)
tk.Button(root, text="÷", width=5, command=lambda: calculate("/")).pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Run the app
root.mainloop()
