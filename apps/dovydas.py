from tkinter import *
import webbrowser
from PIL import ImageTk, Image

class Studenciokas():
    def __init__(self, main):
        self.main = main
        self.main.title("Vandenu Monstras")
        self.f_demo = Frame(self.main)
        photo = ImageTk.PhotoImage(Image.open('images/studenciokas/pike.jpg'))
        self.l_paveiksliukas = Label(self.main, image=photo)
        self.b_linkas = Button(self.f_demo, text="my code", width=10, command=self.open_destytojas_github)
        self.b_close = Button(self.f_demo, text="close", width=10, command=self.close_window)

        self.l_paveiksliukas.pack(side=TOP, fill=BOTH, expand=YES)
        self.b_linkas.pack()
        self.b_close.pack()
        self.f_demo.pack(side=BOTTOM)

        self.main.mainloop()

    def open_destytojas_github(self):
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/River_Monsters#Season_Two_(2010)")

    def close_window(self):
        self.main.destroy()
