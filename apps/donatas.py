from tkinter import *
import webbrowser
from PIL import ImageTk, Image

class Donatas():
    def __init__(self, main):
        self.main = main
        self.main.title("Donato bandymas")
        self.f_demo = Frame(self.main)
        photo = ImageTk.PhotoImage(Image.open('images/donatas/elniukai.jpeg'))
        self.l_paveiksliukas = Label(self.main, image=photo)
        self.b_linkas = Button(self.f_demo, text="mano kodas", width=10, command=self.open_donatas_github)
        self.b_close = Button(self.f_demo, text="uzdaryti", width=10, command=self.close_window)
        
        self.l_paveiksliukas.pack(side=TOP, fill=BOTH, expand=YES)
        self.b_linkas.pack()
        self.b_close.pack()
        self.f_demo.pack(side=BOTTOM)

        self.main.mainloop()

    def open_donatas_github(self):
        webbrowser.open_new_tab("https://github.com/DTuomas/")

    def close_window(self):
        self.main.destroy()