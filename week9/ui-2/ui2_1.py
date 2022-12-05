# pip install
from tkinter import Tk

window = Tk()  # declare and initialise
window.geometry("250x350")  # resize , breadthxheight
window.resizable(False, False)  # resizable -> False
window.title("Main Window ")  # change title of window
window.mainloop()  # display, used at last
