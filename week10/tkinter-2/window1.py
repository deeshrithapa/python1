# display a widow with a button
import tkinter
from tkinter import *
from window2 import Window2

def displayWin2():
    Window2()  # Call __init__() function
window = Tk()
window.title(" main window")
window.geometry("200x200")
window.resizable(False, False)
btnWin2 = Button(text="Window-2", command=displayWin2)
btnWin2.place(x=20, y=20)

window.mainloop()