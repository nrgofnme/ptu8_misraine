from tkinter import *
from tkinter import messagebox
import webbrowser
from PIL import ImageTk, Image

class Giedrius():
    def __init__(self, main):
        self.main = main
        self.main.title("Giedriaus langas")
        self.f_demo = Frame(self.main)
        photo = ImageTk.PhotoImage(Image.open('images/giedrius/giedrius_img1.jpg'))
        self.l_paveiksliukas = Label(self.main, image=photo)
        self.b_linkas = Button(self.f_demo, text="GitHub", width=10, command=self.__open_giedrius_github)
        self.b_dntpress = Button(self.f_demo, text="Nespausti", bg="red", fg="white", width=10, command=self.__dont_press_giedrius)
        self.b_close = Button(self.f_demo, text="Close", width=10, command=self.__close_giedrius_window)

        self.l_paveiksliukas.pack(side=TOP, fill=BOTH, expand=YES)
        self.b_linkas.pack()
        self.b_dntpress.pack()
        self.b_close.pack()
        self.f_demo.pack(side=BOTTOM)

        self.main.mainloop()

    def __open_giedrius_github(self):
        webbrowser.open_new_tab("https://github.com/gisora/")

    def __close_giedrius_window(self):
        self.main.destroy()

    def __dont_press_giedrius(self):
        while True:
            o = "e"
            webbrowser.open_new_tab("https://bit.ly/3BlS71b")
            for _ in range(10):
                o *= 2
                messagebox.showerror(title=":)", message=f"Ohhhh n{o} !!!!")
            if messagebox.askquestion(title="Klausimėlis", message="Gal pakartojam? :)") == "no":
                break