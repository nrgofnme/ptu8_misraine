from tkinter import *
import webbrowser
from PIL import ImageTk, Image

class Studente():
    def __init__(self, main):
        self.main = main
        self.main.title('Kosmosas')
        self.f_budas = Frame(self.main)
        foto = ImageTk.PhotoImage(Image.open('images/monika/space.jpg'))
        self.l_message = Label(self.main, text='Kaip sekasi kosmonautams?', image=foto)
        self.b_labas = Button(self.f_budas, text='press this', width=10, command=self.show_palinkejimas)
        self.b_uzdaryti = Button(self.f_budas, text='close', width=10, command=self.close_window)

        self.l_message.pack(side=TOP, fill=BOTH, expand=YES)
        self.b_labas.pack()
        self.b_uzdaryti.pack()
        self.f_budas.pack(side=BOTTOM)

        self.main.mainloop()

    def show_palinkejimas(self):
        webbrowser.open_new_tab('https://hubblesite.org/contents/media/images/2022/027/01G4NK41T43PFGJ2QGF2AZ104B?page=2&filterUUID=5a370ecc-f605-44dd-8096-125e4e623945')

    def close_window(self):
        self.main.destroy()