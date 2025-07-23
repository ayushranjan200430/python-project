import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        pool = ""
        password = []

        selected_types = [
            (include_lower, string.ascii_lowercase),
            (include_upper, string.ascii_uppercase),
            (include_digits, string.digits),
            (include_symbols, string.punctuation),
        ]

        for var, chars in selected_types:
            if var.get():
                pool += chars
                password.append(random.choice(chars))

        if not pool:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password += random.choices(pool, k=length - len(password))
        random.shuffle(password)
        final_password = ''.join(password)
        generated_password.set(final_password)
        rate_strength(final_password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(generated_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def rate_strength(pw):
    types_used = sum([
        any(c.islower() for c in pw),
        any(c.isupper() for c in pw),
        any(c.isdigit() for c in pw),
        any(c in string.punctuation for c in pw)
    ])
    if len(pw) >= 12 and types_used >= 3:
        strength.set("Strength:  Strong")
    elif len(pw) >= 8 and types_used >= 2:
        strength.set("Strength: Moderate")
    else:
        strength.set("Strength:  Weak")

def toggle_theme():
    if is_dark.get():
        root.configure(bg="#1e1e1e")
        for widget in root.winfo_children():
            widget.configure(bg="#1e1e1e", fg="white")
    else:
        root.configure(bg="white")
        for widget in root.winfo_children():
            widget.configure(bg="white", fg="black")

# GUI Setup
root = tk.Tk()
root.title(" Password Generator")
root.geometry("440x420")
root.resizable(False, False)

is_dark = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Dark Mode", variable=is_dark, command=toggle_theme).pack(pady=5)

tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify='center')
length_entry.pack()

tk.Label(root, text="Select character types to include:", font=("Arial", 11)).pack(pady=10)
include_lower = tk.BooleanVar(value=True)
include_upper = tk.BooleanVar(value=True)
include_digits = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Lowercase (a-z)", variable=include_lower, font=("Arial", 11)).pack(anchor='w', padx=30)
tk.Checkbutton(root, text="Uppercase (A-Z)", variable=include_upper, font=("Arial", 11)).pack(anchor='w', padx=30)
tk.Checkbutton(root, text="Digits (0-9)", variable=include_digits, font=("Arial", 11)).pack(anchor='w', padx=30)
tk.Checkbutton(root, text="Symbols (!@#$...)", variable=include_symbols, font=("Arial", 11)).pack(anchor='w', padx=30)

tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=15)
generated_password = tk.StringVar()
tk.Entry(root, textvariable=generated_password, font=("Arial", 12), width=30, justify='center').pack()

tk.Button(root, text=" Copy to Clipboard", font=("Arial", 11), command=copy_to_clipboard).pack(pady=5)
strength = tk.StringVar(value="Strength: ")
tk.Label(root, textvariable=strength, font=("Arial", 11)).pack(pady=5)

toggle_theme()  # Apply initial theme
root.mainloop()