from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.configure(bg="#2c3e50")  # Background color

# Styling constants
BTN_BG = "#34495e"
BTN_FG = "white"
FONT = ("Helvetica", 16)
ENTRY_FONT = ("Helvetica", 24, "bold")
ENTRY_BG = "#ecf0f1"
ENTRY_FG = "#2c3e50"

# Frame to mimic border/shadow for Entry
entry_frame = Frame(root, bg="#95a5a6", padx=2, pady=2)
entry_frame.grid(row=0, column=0, columnspan=4, pady=20, padx=10)

# Styled Entry widget inside frame
e = Entry(entry_frame, width=18, borderwidth=0, font=ENTRY_FONT,
          bg=ENTRY_BG, fg=ENTRY_FG, justify="right", relief=FLAT)
e.pack(ipady=10, ipadx=5)

# Functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    global f_num, math
    f_num = int(e.get())
    math = "addition"
    e.delete(0, END)

def button_sub():
    global f_num, math
    f_num = int(e.get())
    math = "subtraction"
    e.delete(0, END)

def button_mul():
    global f_num, math
    f_num = int(e.get())
    math = "multiply"
    e.delete(0, END)

def button_divide():
    global f_num, math
    f_num = int(e.get())
    math = "divide"
    e.delete(0, END)

def button_equal():
    second_number = int(e.get())
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + second_number)
    elif math == "subtraction":
        e.insert(0, f_num - second_number)
    elif math == "multiply":
        e.insert(0, f_num * second_number)
    elif math == "divide":
        if second_number == 0:
            e.insert(0, "Error")
        else:
            e.insert(0, f_num / second_number)

# Button creation function
def create_button(text, row, col, command, colspan=1, width=5):
    button = Button(root, text=text, padx=20, pady=20, command=command,
                    bg=BTN_BG, fg=BTN_FG, font=FONT, width=width)
    button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

# Number buttons
create_button("1", 3, 0, lambda: button_click(1))
create_button("2", 3, 1, lambda: button_click(2))
create_button("3", 3, 2, lambda: button_click(3))
create_button("4", 2, 0, lambda: button_click(4))
create_button("5", 2, 1, lambda: button_click(5))
create_button("6", 2, 2, lambda: button_click(6))
create_button("7", 1, 0, lambda: button_click(7))
create_button("8", 1, 1, lambda: button_click(8))
create_button("9", 1, 2, lambda: button_click(9))
create_button("0", 4, 0, lambda: button_click(0))

# Operation buttons
create_button("+", 1, 3, button_add)
create_button("-", 2, 3, button_sub)
create_button("*", 3, 3, button_mul)
create_button("/", 4, 3, button_divide)
create_button("Clear", 4, 1, button_clear, colspan=2, width=11)
create_button("=", 5, 0, button_equal, colspan=4, width=35)

root.mainloop()