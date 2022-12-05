import sys
import tkinter
from tkinter import *
from tkinter import messagebox


def save():
    #  read from text box
    strId = txtId.get()
    if strId.isnumeric():
        tmpId = int(strId)
        if tmpId>=1 and tmpId<=99:
            messagebox.showinfo("Title", "Valid Id")
        else:            messagebox.showinfo("Title", "Id out of range")
    else:
        messagebox.showinfo("Title", "Invalid data type")

    strName = txtName.get()
    if strName.isalpha():
        messagebox.showinfo("Title", "valid Id")
    else:
        messagebox.showinfo("Title", "Invalid data type")

    strAddress = txtAddress.get()
    if strAddress.isalnum():
        messagebox.showinfo("Title", "valid id")
    else:
        messagebox.showinfo("Title", "Invalid data type ")

def close():
    sys.exit()

window = Tk()
window.title("Validation Test")
window.geometry("450x400")
window.resizable(False, False)

lblId = Label(window, text='ID:')  # must be numeric and range 1-100
lblId.place(x=20, y=20)
txtId= Entry(window, width=20)
txtId.place(x=100, y=20)


lblName = Label(window, text='Full Name:')
lblName.place(x=20, y=50)
txtName= Entry(window, width=20)
txtName.place(x=100, y=50)

lblAddress = Label(window, text='Address:')
lblAddress.place(x=20, y=80)
txtAddress = Entry(window, width=20)
txtAddress.place(x=100, y=80)




btnSave = Button(window, text='save', command=save)
btnSave.place(x=60, y=350)

btnClose = Button(window, text='close', command=close)
btnClose.place(x=100, y=350)

window.mainloop()

# id, name, address, phone, email, mobile, price, atm card
