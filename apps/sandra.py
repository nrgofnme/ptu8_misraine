from tkinter import *
import webbrowser
from PIL import ImageTk, Image

class Sandra():
    def __init__(self, main):
        self.main = main
        self.main.title("Mano Hobis")
        self.f_demo = Frame(self.main)
        photo = ImageTk.PhotoImage(Image.open('images/sandra/pabaiga2.jpg'))
        self.l_paveiksliukas = Label(self.main, image=photo)
        self.b_linkas_sandra = Button(self.f_demo, text="sandros kodas", width=10, command=self.open_sandra_github)
        self.b_close_sandra = Button(self.f_demo, text="einam namo", background="red", width=10, command=self.close_window)

        self.l_paveiksliukas.pack(side=TOP, fill=BOTH, expand=YES)
        self.b_linkas_sandra.pack()
        self.b_close_sandra.pack()
        self.f_demo.pack(side=BOTTOM)

        self.main.mainloop()

    def open_sandra_github(self):
        webbrowser.open_new_tab("https://github.com/SandraAngelOfDarkness/")

    def close_window(self):
        self.main.destroy()
