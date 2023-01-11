from tkinter import *
from PIL import ImageTk, Image

class Edvardas:
    def __init__(self, main):
        self.main = main
        self.main.title("Kai sergi ir bandai apkrauti smegenis...")
        self.f_remelis = Frame(self.main)
        photo = ImageTk.PhotoImage(Image.open('images/edvard_img/nuclear.jpg'))
        self.l_image = Label(self.main, image=photo)
        self.b_close = Button(self.f_remelis, text="Vanish", width=15, command=self.close_window)
        self.b_close.configure(bg="white", background="black", fg="red", border=5)

        self.l_image.pack(side=TOP, fill=BOTH, expand=YES)
        self.b_close.pack()
        self.f_remelis.pack()

        self.main.mainloop()

    def close_window(self):
        self.main.destroy()


