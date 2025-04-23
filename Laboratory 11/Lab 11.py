import tkinter as tk


root = tk.Tk()
root.title("Calculator")
root.geometry("326x450")
#root.configure(bg = 'Light blue')

def click(event):
    text = event.widget["text"]
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0,tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Syntax error")
    elif text == "C":
        entry.delete(0, tk.END)
    #elif text == "DEL":
    #    entry.delete(0)
    else:
        entry.insert(tk.END, text)

result = tk.StringVar()

entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=1, pady=1, ipadx=1, ipady=1)

# C, 9,8,7,6,5,4,3,2,1,0,÷,x,-,+,.,=
buttons = [["C"],["7", "8", "9", "/"],
           ["4", "5", "6", "*"],
           ["1", "2", "3", "-"],
           ["0", ".", "+", "="]]

buttonstyle = {"font":("Arial", 12, "bold"), "width":6, "height":3, "bd":5}#,"bg":"Light grey", "activebackground":"Light Blue"}
for x, row in enumerate(buttons, 1):
    for y, btntext in enumerate(row):
        btn = tk.Button(root, text=btntext, **buttonstyle, padx=2, pady=2)
        btn.grid(row=x, column=y, sticky="nsew", padx=2, pady=2)
        btn.bind("<Button-1>", click)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(len(buttons)+1):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()