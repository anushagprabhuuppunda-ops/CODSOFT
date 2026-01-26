import tkinter as tk
import random
import string
from unittest import result
def generate_password():
    try:
        length = int(lengthEnt.get())
        characters = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
        password = ""
        for i in range(length):
            password+=random.choice(characters)
            result.config(text="Generated Password: " + password)
    except ValueError:
        result.config(text="Please enter a valid number")
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#E6A6A6")
fr=tk.Frame(root,bg="#E6A6A6",height=300,width=400)
fr.pack(pady=20)

enter=tk.Label(fr, text="Enter Password Length:",bg="#E6A6A6", fg="black",width=20,height=2,font=("Times new roman", 15))
enter.pack(side="left",pady=10)
#enter.grid(row=0,column=0,pady=10)

lengthEnt = tk.Entry(fr,width=30,font=("Arial", 12))
lengthEnt.pack(side="right",pady=10)
#lengthEnt.grid(row=0,column=1,pady=10)

btn=tk.Button(root, text="Generate Password", command=generate_password,bg="#49f360", fg="black",activebackground="#B0BA7D",height=1,font=("Arial", 12,"italic"),relief="solid",bd=2)
btn.pack(pady=10,padx=10)
#btn.grid(pady=10,padx=20)
result = tk.Label(root, text="",width=50,height=2 ,bg="#E6A6A6", fg="#0D1910",font=("courier", 15,"bold"))
result.pack(pady=15,padx=10)
#result.grid(pady=10)
root.mainloop()