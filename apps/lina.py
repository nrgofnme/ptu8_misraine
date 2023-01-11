from tkinter import *
from PIL import ImageTk, Image

class Lina():
    def __init__(self, main):
        self.main = main
        self.f_demo = Frame(self.main)
        pav = ImageTk.PhotoImage(Image.open('images/lina/20200508_145515.jpg'))
        self.l_paveiksliukas = Label(self.main, image=pav)
        self.b_uzdaryti = Button(self.f_demo, text="Uzdaryti", width=10, command=self.close_window)

        self.l_paveiksliukas.pack(side=TOP, fill=BOTH, expand=YES)
        self.b_uzdaryti.pack()
        self.f_demo.pack(side=BOTTOM)

        self.main.mainloop()

    def close_window(self):
        self.main.destroy()
