# pip install tk
# import library
import sys
from tkinter import Tk  # window
from tkinter import Label  # label
from tkinter import Entry  # text box
from tkinter import Button  # button
from notebookManager import search
from notebook import Notebook


def searchNotebook():
    #reading value from entry and send to library/middleware
    nid = int(txtNID.get())
    record = search(nid)
    if (record==None):
        print("Record not found")
        # txtPrice.insert(0, str(record.getPrice))
    else:
        txtPage.insert(0, str(record[1]))  # assign new text
        txtPrice.insert(0,str(record[2]))
        print("Record found!")

def close():
    sys.exit()


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


btnSearch= Button(window, text="Search", command=searchNotebook)
btnSearch.place(x=100, y=100)

btnClose = Button(window, text="Close", command=close)
btnClose.place(x=150, y=100)



window.mainloop()  # display window

