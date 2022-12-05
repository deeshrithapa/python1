# display a widow with a button
import tkinter
from tkinter import *
from tkinter import ttk  # combobox
# from PIL import ImageTk, Image


class Window2():
    def __init__(self):
        window = Tk()
        window.title("Window-2")
        window.geometry("350x500")
        window.resizable(False, False)

        # Add Label
        lblCollege = Label(window, text='PCPS College')
        lblCollege.place(x=20, y=20)

        # Add Entry - text box - single line
        txtName = Entry(window, width=20)
        txtName.place(x=20, y=50)

        # Add Password box
        txtPass = Entry(window, width=20, show='*')
        txtPass.place(x=20, y=80)

        # Text- Comment box / Text Area
        txtComments = Text(window, width=30, height=3)
        txtComments.place(x=20, y=110)

        # radiobutton - Single selection from multiple options
        rb1 = Radiobutton(window, text="option-1", value='v1')
        rb2 = Radiobutton(window, text="option-2", value='v2')
        rb1.place(x=20, y=180)
        rb2.place(x=20, y=200)

        # checkbox - checkbox (select multiple values from multiple options)
        ck1 = Checkbutton(window, text="option-a")
        ck2 = Checkbutton(window, text="option-b")
        ck3 = Checkbutton(window, text="option-c")
        ck1.place(x=20, y=260)
        ck2.place(x=20, y=280)
        ck3.place(x=20, y=300)

        #combobox
        cmb1 = ttk.Combobox(window)
        cmb1['values']= ('Value1', 'Value2', 'Value3',)
        cmb1.place(x=20, y=340)

        # canvas - image viewer
        # pip install
        # tmpImage = Image.open('image.png')
        # imgFile = ImageTk.PhotoImage(tmpImage)
        # canvas = Canvas(window, width=150, height=150)
        # canvas.create_image(0,0, image=imgFile)
        # canvas.place(x=20, y=360)

        # button
        btnSave= Button(window, text='save')
        btnSave.place(x=20, y=380)





        window.mainloop()