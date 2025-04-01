import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

# Creating tkinter window and set dimensions
window = tk.Tk()
window.title('Combobox')
window.geometry('500x300')
window.configure(bg="#E3A869")


def choice(event):
    month = event.widget.get()
    print("Your birth month", month)


# label text for title
ttk.Label(window, text="Choose your birth date",
          background='light yellow', foreground="black",
          font=("Times New Roman", 15)).grid(row=0, column=1)

# Set label
ttk.Label(window, text="Select your Birth Month :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=1, padx=5, pady=25)
ttk.Label(window, text="Select your Birth Day :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=2, padx=5, pady=25)
ttk.Label(window, text="Select your Birth Year :",
          font=("Times New Roman", 12)).grid(column=0,
                                             row=3, padx=5, pady=25)

# Combo box per Month
n = tk.StringVar()
month = ttk.Combobox(window, width=27, textvariable=n)

month['values'] = (' January',
                     ' February',
                     ' March',
                     ' April',
                     ' May',
                     ' June',
                     ' July',
                     ' August',
                     'September',
                     'October',
                     'November',
                     'December')

month.grid(column=1, row=1)
month.current()

#Combo box per Day
x = tk.StringVar()
day = ttk.Combobox(window, width=27, textvariable=x)


day['values'] = [str(i) for i in range(1,32)]

day.grid(column=1, row=2)
day.current()

#Combo Box per year
y = tk.StringVar()
year = ttk.Combobox(window, width=27, textvariable=y)

year['values'] = [str(t) for t in range(1900, 2025)]

year.grid(column=1, row=3)
year.current()

def choice():
    showinfo(
            title = "Selection",
            message = f'Your Birth Date is: {n.get()} {x.get()}, {y.get()}')

ttk.Button(window, text="Confirm", command=choice).grid(column=1, row=4)
window.mainloop()