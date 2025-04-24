import tkinter as tk
import math


def evaluate_expression():
    try:
        expression = entry.get()
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("log", "math.log10")
        expression = expression.replace("ln", "math.log")
        expression = expression.replace("√", "math.sqrt")
        expression = expression.replace("^", "**")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

def insert_text(text):
    entry.insert(tk.END, text)

def on_keypress(event):
    if event.keysym == "Return":
        evaluate_expression()


root = tk.Tk()
root.title("Scientific Calculator")


menu = tk.Menu(root)
root.config(menu=menu)
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear", command=clear_entry)

# --- Entry Field ---
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=10, ipady=10)
entry.bind("<Return>", on_keypress)

# --- Buttons ---
buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "log"],
    ["1", "2", "3", "-", "sin"],
    ["0", ".", "+", "cos", "tan"],
    ["(", ")", "^", "ln", "="],
    ["C"]
]

for r, row in enumerate(buttons, start=1):
    for c, label in enumerate(row):
        if label == "=":
            btn = tk.Button(root, text=label, font=("Arial", 16), bg="lightgreen",
                            command=evaluate_expression)
        elif label == "C":
            btn = tk.Button(root, text=label, font=("Arial", 16), bg="lightcoral",
                            command=clear_entry)
            btn.grid(row=r, column=0, columnspan=5, sticky="nsew", padx=2, pady=2)
            continue
        else:
            btn = tk.Button(root, text=label, font=("Arial", 16),
                            command=lambda txt=label: insert_text(txt))
        btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

# --- Make all rows/columns flexible ---
for i in range(5):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
