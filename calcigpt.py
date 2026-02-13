import tkinter as tk
def calculate(operation):
    try:
        num1=float(entry1.get())
        num2=float(entry2.get())
        if operation == "+":
            result=num1+num2
        elif operation == "-":
            result=num1-num2    
        elif operation == "*":
            result=num1*num2    
        elif operation == "/":
            if num2 != 0:
                result=num1/num2    
            else:
                result="Error: Division by zero"
        elif operation == "%":   
            if num2 != 0:
                result=num1%num2    
            else:
                result="Error: Modulo by zero"
    except ValueError:
        result="Error: Invalid input"
    return result
