from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("400x450")
root.configure(bg="#2c3e50")

tasks = []

def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        pass

# UI elements
entry = Entry(root, font=("Helvetica", 14))
entry.pack(pady=20)

add_btn = Button(root, text="Add Task", width=15, command=add_task, bg="#3498db", fg="white")
add_btn.pack()

del_btn = Button(root, text="Delete Task", width=15, command=delete_task, bg="#e74c3c", fg="white")
del_btn.pack(pady=10)

listbox = Listbox(root, font=("Helvetica", 14), width=30, height=10, selectbackground="#1abc9c")
listbox.pack(pady=20)

root.mainloop()
