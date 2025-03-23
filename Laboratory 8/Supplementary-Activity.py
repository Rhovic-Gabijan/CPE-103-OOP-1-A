import tkinter as tk
import math
from tkinter import messagebox

history_list = []

# Functions for calculation
def add():
    try:
        global history_list
        result_val = (float(entry1.get()) + float(entry2.get()))
        result.set(result_val)
        history_list.append(f"{entry1.get()} + {entry2.get()} = {result_val}")
    except ValueError:
        result.set("Error! Invalid input.")

def subtract():
    try:
        global history_list
        result_val = (float(entry1.get()) - float(entry2.get()))
        result.set(result_val)
        history_list.append(f"{entry1.get()} - {entry2.get()} = {result_val}")
    except ValueError:
        result.set("Error! Invalid input.")

def multiply():
    try:
        global history_list
        result_val = (float(entry1.get()) * float(entry2.get()))
        result.set(result_val)
        history_list.append(f"{entry1.get()} x {entry2.get()} = {result_val}")
    except ValueError:
        result.set("Error! Invalid input.")

def divide():
    try:
        global history_list
        result_val = (float(entry1.get()) / float(entry2.get()))
        result.set(result_val)
        history_list.append(f"{entry1.get()} / {entry2.get()} = {result_val}")
    except ZeroDivisionError:
        result.set("Error! Division by zero.")
        history_list.append(f"{entry1.get()} / {entry2.get()} = Error! Division by zero")
    except ValueError:
        result.set("Error! Invalid input.")
#Advance Operations
def squareroot():
    try:
        global history_list
        value = float(entry1.get())
        result_val = math.sqrt(value)
        result.set(result_val)
        history_list.append(f"√{value} = {result_val}")
    except ValueError:
        result.set("Error! Invalid input.")

def power():
    try:
        global history_list
        value = float(entry1.get())
        expo = float(entry2.get())
        result_val = value**expo
        result.set(result_val)
        history_list.append(f"{value}^{expo} = {result_val}")
    except ValueError:
        result.set("Error! Invalid input.")

def sin():
    try:
        global history_list
        value = float(entry1.get())
        result_val = math.sin(math.radians(value))
        result.set(result_val)
        history_list.append(f"sin({value}) = {result_val}")
    except ValueError:
        result.set("Error! Invalid input.")

def cos():
    try:
        global history_list
        value = float(entry1.get())
        result_val = math.cos(math.radians(value))
        result.set(result_val)
        history_list.append(f"cos({value}) = {result_val}")
    except ValueError:
        result.set("Error! Invalid input.")

def tan():
    try:
        global history_list
        value = float(entry1.get())
        result_val = math.tan(math.radians(value))
        result.set(result_val)
        history_list.append(f"tan({value}) ={result_val}")
    except ValueError:
        result.set("Error! Invalid input.")

#Buttons
def validate_input():
    try:
        float(entry1.get())
        float(entry2.get())
        return True
    except ValueError:
        messagebox.showerror("Error! Input valid numbers")
        return False

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

def show_history():
    if not history_list:
        messagebox.showinfo("History", "No calculations yet.")
        return

    history_window = tk.Toplevel(root)
    history_window.title("History")

    history_listbox = tk.Listbox(history_window, height=10, width=50)
    history_listbox.pack(padx = 20, pady = 10)

    for entry in history_list:
        history_listbox.insert(tk.END, entry)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300+10+10")

# Create StringVar to hold the result
result = tk.StringVar()

#Create layout
tk.Label(root, text="Enter first number:", font=("Arial", 12)).grid(row=0, column=0)
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:", font=("Arial", 12)).grid(row=1, column=0)
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.grid(row=1, column=1)

#Buttons for Operations
button_style ={"font":("Arial", 10), "width":12, "height":1, "bg":"Light Blue" }

tk.Button(root, text="Add", command=add, **button_style).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=subtract, **button_style).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=multiply, **button_style).grid(row=3, column=0)
tk.Button(root, text="Divide", command=divide, **button_style).grid(row=3, column=1)

tk.Button(root, text="Square Root", command=squareroot, **button_style).grid(row=4, column=0)
tk.Button(root, text="Power", command=power, **button_style).grid(row=4, column=1)
tk.Button(root, text="Sine", command=sin, **button_style).grid(row=5, column=0)
tk.Button(root, text="Cosine", command=cos, **button_style).grid(row=5, column=1)
tk.Button(root, text="Tangent", command=tan, **button_style).grid(row=6, column=0)

tk.Button(root, text ="History", command=show_history, **button_style).grid(row =6, column = 1)
tk.Button(root, text ="Clear", command = clear, **button_style).grid(row =7, column = 1)


#Label to Show result
tk.Label(root, text="Result:", font=("Arial", 12)).grid(row=8, column=0)
result_label = tk.Label(root, textvariable=result, font=("Arial", 12))
result_label.grid(row=8, column=1)

#Start the main loop
root.mainloop()