from tkinter import *
import webbrowser
from PIL import ImageTk, Image

class Redas():
    def __init__(self, main):
        self.main = main
        self.main.title("Redo kodas")
        self.f_demo = Frame(self.main)
        photo = ImageTk.PhotoImage(Image.open('images/redas/golpas.jpg'))
        self.l_paveiksliukas = Label(self.main, image=photo)
        self.b_linkas = Button(self.f_demo, text="My Github", width=10, command=self.open_redas_github)
        self.b_youtubas = Button(self.f_demo, text="The 2023 X7", width=10, command=self.open_youtube)
        self.b_close = Button(self.f_demo, text="Close", width=10, command=self.close_window)

        self.l_paveiksliukas.pack(side=TOP, fill=BOTH, expand=YES)
        self.b_linkas.pack()
        self.b_youtubas.pack()
        self.b_close.pack()
        self.f_demo.pack(side=BOTTOM)

        self.main.mainloop()

    def open_redas_github(self):
        webbrowser.open_new_tab("https://github.com/redasmarc/")

    def open_youtube(self):
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=zNrgNVH59Ng")

    def close_window(self):
        self.main.destroy()
