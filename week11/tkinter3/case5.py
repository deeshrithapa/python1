import sys
import tkinter
from tkinter import *
from tkinter import ttk

def close():
    sys.exit()

window = Tk()
window.title("UI")
window.geometry("450x400")
window.resizable(False, False)

lblId = Label(window, text='ID')
lblId.place(x=20, y=20)

cmb1 = ttk.Combobox(window)
cmb1['values']= ('Value1', 'Value2', 'Value3',)
cmb1.place(x=90, y=20)

lblName= Label(window, text='Name')
lblName.place(x=20, y=60)
txtName = Entry(window, width=20)
txtName.place(x=90, y=60)

lblAddress= Label(window, text='Address')
lblAddress.place(x=20, y=100)
txtAddress= Entry(window, width=20)
txtAddress.place(x=90, y=100)

btnClose= Button(window, text='Close')
btnClose.place(x=90, y=150)





window.mainloop()
