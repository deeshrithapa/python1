import sys
import tkinter
from tkinter import *
from class1 import insert
from class2 import Customer

def save():
    cid = int(txtCid.get())
    name = txtName.get()
    address = txtAddress.get()
    email = txtEmail.get()
    phone_number = txtPhone.get()

    nb1 = Customer(cid,name, address, email, phone_number)
    result = insert(nb1)
    if (result == True):
        print("Insert Successfully")
    else:
        print("Error to insert")

def close():
    sys.exit()


window = Tk()
window.title("CUSTOMERS")
window.geometry("400x400")
window.resizable(False, False)
window.configure(bg="grey")

lblCid = Label(window, text='Cid')
lblCid.place(x=20, y=20)
lblCid.configure(bg="grey")
txtCid = Entry(window, width=20)
txtCid.place(x=110, y=20)

lblName = Label(window, text='Name')
lblName.place(x=20, y=50)
lblName.configure(bg="grey")
txtName = Entry(window, width=20)
txtName.place(x=110, y=50)

lblAddress = Label(window, text='Address')
lblAddress.place(x=20, y=80)
lblAddress.configure(bg="grey")
txtAddress = Entry(window, width=20)
txtAddress.place(x=110, y=80)

lblEmail = Label(window, text='Email')
lblEmail.place(x=20, y=110)
lblEmail.configure(bg="grey")
txtEmail = Entry(window, width=20)
txtEmail.place(x=110, y=110)

lblPhone = Label(window, text='Phone number')
lblPhone.place(x=20, y=140)
lblPhone.configure(bg="grey")
txtPhone = Entry(window, width=20)
txtPhone.place(x=110, y=140)

btnSave= Button(window, text='Save', command=save)
btnSave.place(x=110, y=180)
btnSave= Button(window, text='Close', command=close)
btnSave.place(x=160, y=180)

window.mainloop()

