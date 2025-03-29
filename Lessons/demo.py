from tkinter import *

window = Tk()
window.title("Using grid manager")
window.geometry("400x250")

txtfld1 = Entry(window, justify="center")
txtfld1.grid(row=0, column=0)
txtfld1.insert(END,"row 0, column 0")

txtfld2 = Entry(window, justify="center")
txtfld2.grid(row=0, column=1)
txtfld2.insert(END,"row 0, column 1")

txtfld3 = Entry(window, justify="center")
txtfld3.grid(row=0, column=2)
txtfld3.insert(END,"row 0, column 2")

txtfld4 = Entry(window, justify="center")
txtfld4.grid(row=1, column=0)
txtfld4.insert(END,"row 1, column 0")

txtfld5 = Entry(window, justify="center")
txtfld5.grid(row=1, column=1)
txtfld5.insert(END,"row 2, column 0")

txtfld6 = Entry(window, justify="center")
txtfld6.grid(row=1, column=2)
txtfld6.insert(END,"row 3, column 0")

yscroll = Scrollbar(window)
yscroll.grid(row =3, column = 2, sticky='nsw')
listbox = Listbox(window, yscrollcommand=yscroll.set)
listbox.grid(row =3, column = 1, padx=5,pady=5)

yscroll.config(command=listbox.yview)

for x in range(1,51):
    listbox.insert(END, x)


window.mainloop()
