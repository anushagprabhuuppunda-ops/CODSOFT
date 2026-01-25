import tkinter as tk
tasks=[]
def refresh():
    listbox.delete(0,tk.END)
    for task in tasks:
        if task["done"]:
          listbox.insert(tk.END,"✓"+task["title"])
        else:
            listbox.insert(tk.END,task["title"])
def add():
     title=entry.get()
     if title:
         tasks.append({"title":title,"done":False})
         entry.delete(0,tk.END)
         refresh()
def complete():
     try:
         index=listbox.curselection()[0]
         tasks[index]["done"]=True
         refresh()
     except:
         pass
def update():
    try:
        index=listbox.curselection()[0]
        newTitle=entry.get()
        if newTitle:
            tasks[index]["title"]=newTitle
            entry.delete(0,tk.END)
            refresh()
    except:
        pass
def delete():
    try:
        index=listbox.curselection()[0]
        tasks.pop(index)
        refresh()
    except:
        pass
root=tk.Tk()
root.title("To-Do list App")
root.geometry("400x400")
root.configure(bg="lightblue")
entry=tk.Entry(root,width=40,font=("ariel",12))
entry.pack(pady=10)

add=tk.Button(root,text="Add task",width=30,activebackground="green",activeforeground="White",command=add).pack(pady=5)
com=tk.Button(root,text="Complete task",width=30,command=complete).pack(pady=5)
upd=tk.Button(root,text="Update task",width=30,command=update).pack(pady=5)
delt=tk.Button(root,text="Delete task",width=30,command=delete).pack(pady=5)

listbox=tk.Listbox(root,width=40,height=10,fg="maroon",font=5)
listbox.pack(pady=10)
root.mainloop()             
                