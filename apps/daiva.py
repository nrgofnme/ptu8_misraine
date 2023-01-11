from tkinter import *
from random import randint
from PIL import ImageTk, Image

class Daiva:
    def __init__(self, main) -> None:
        self.main = main
        self.main.title('Homosaurus Rex')
        self.f_langas = Frame(self.main)
        self.l_spejimas = Label(self.f_langas, text='Atspėk skaičių (1-5), kad pamatytum mane su dinozauro kostiumu')
        self.e_spejimas = Entry(self.f_langas)
        self.b_spejimas = Button(self.f_langas, text='Spejimas', command=self.spejimas)
        self.l_rezultatas = Label(self.f_langas, text=None)
        self.l_nuotrauka = Label(self.f_langas, image=None)

        self.f_langas.pack()
        self.l_spejimas.pack(side=TOP)
        self.e_spejimas.pack()
        self.b_spejimas.pack()
        self.l_rezultatas.pack()
        self.l_nuotrauka.pack()

        self.main.mainloop()
        
    def spejimas(self):
        atsakymas = randint(1, 5)
        spejimas = int(self.e_spejimas.get())
        if spejimas == atsakymas:
            self.l_rezultatas['text'] = 'Sveikinu, štai Homosaurus Rex nuotrauka'
            nuotrauka = ImageTk.PhotoImage(Image.open('images/daiva/dino.jpg'))
            self.l_nuotrauka['image'] = nuotrauka
            self.e_spejimas.delete(0, END)
        else:
            self.l_rezultatas['text'] = 'Nepataikei, štai paguodai kačiuko nuotrauka'
            nuotrauka2 = ImageTk.PhotoImage(Image.open('images/daiva/cat.jpg'))
            self.l_nuotrauka['image'] = nuotrauka2
        self.main.mainloop()