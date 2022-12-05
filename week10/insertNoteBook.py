# pip install tk
# import library
from tkinter import Tk  # window
from tkinter import Label  # label
from tkinter import Entry  # text box
from tkinter import Button  # button
from notebookManager import insert
from notebook import Notebook


def save():

    #reading value from entry and send to library/middleware
    nid = int(txtNID.get())
    page = int(txtPage.get())
    price = float(txtPrice.get())
    nb1 = Notebook(nid, page, price)
    result = insert(nb1)
    if (result==True):
        print("Insert Successfully")
    else:
        print("Error to insert")



# declare and initialise
window = Tk()
window.geometry("250x350")
window.resizable(False, False)
window.title("Insert New Record")

lblNID = Label(window, text= "NID:")
lblPage = Label(window, text="Page:")
lblPrice = Label(window, text = "Price:")


txtNID = Entry(window, width=20)
txtPage = Entry(window, width=20)
txtPrice = Entry(window, width=20)




lblNID.place(x= 20, y=10)
lblPage.place(x=20, y=40)
lblPrice.place(x=20, y=70)

txtNID.place(x=70, y=10)
txtPage.place(x=70, y=40)
txtPrice.place(x=70, y=70)


btnSave= Button(window, text="Save", command=save)
btnSave.place(x=100, y=100)

btnClose = Button(window, text="close")
btnClose.place(x=200, y=100)



window.mainloop()  # display window

