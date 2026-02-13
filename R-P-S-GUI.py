import tkinter as tk
import random
ch=["Rock","Paper","Scissors"]
us=0
cs=0
def play(uc):
    global us,cs
    cc=random.choice(ch)
    chlbl.config(text=f"Your choice={uc} , Computer choice={cc}")
    if uc==cc:
        result.config(text="A Tie!")
    elif ((uc=="Rock" and cc=="Scissors")or (uc=="Scissors"and cc=="Paper")or(uc=="Paper"and cc=="Rock")):
        us+=1
        
    else:
        cs+=1
    score.config(text=f"Your score={us} , Computer score={cs}")
    if us>cs:
        result.config(text="You win!")
    elif cs>us:
        result.config(text="Computer wins!")

def playagain():
    global us,cs
    us=0
    cs=0
    score.config(text=f"Your score={us} , Computer score={cs}")
        
root=tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("500x300")
t=tk.Label(root,text="ROCK_PAPER_SCISSORS").grid(row=0,column=2,padx=5)

rb=tk.Button(root,text="Rock",command=lambda:play("Rock")).grid(row=2,column=1)
pb=tk.Button(root,text="Paper",command=lambda:play("Paper")).grid(row=2,column=2)
sb=tk.Button(root,text="Scissors",command=lambda:play("Scissors")).grid(row=2,column=3,padx=10)

chlbl=tk.Label(root)
chlbl.grid(row=4,column=2)
score=tk.Label(root)
score.grid(row=5,column=2)
result=tk.Label(root,text="Choose your move")
result.grid(row=6,column=2)


p=tk.Button(root,text="Play again",command=lambda:playagain(),bg="lightgreen")
p.grid(row=9,column=2)

root.mainloop()