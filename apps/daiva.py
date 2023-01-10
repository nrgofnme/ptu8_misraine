from tkinter import *
from random import randint
from PIL import ImageTk, Image

class Daiva:
    def __init__(self, main) -> None:
        self.main = main
        self.main.title('Homosaurus Rex')
        self.f_langas = Frame(self.main)
        self.l_spejimas = Label(self.f_langas, text='Atspėk skaičių (1-10), kad pamatytum mane su dinozauro kostiumu')
        self.e_spejimas = Entry(self.f_langas)
        self.b_spejimas = Button(self.f_langas, text='Spejimas', command=self.spejimas)

        self.f_langas.pack()
        self.l_spejimas.pack(side=TOP)
        self.e_spejimas.pack()
        self.b_spejimas.pack()

    def spejimas(self):
        kartai = 0
        atsakymas = randint(1, 10)
        while kartai < 3:
            spejimas = int(self.e_spejimas.get())
            # neveikia kartu skaiciavimas
            kartai += 1
            if spejimas != atsakymas:
                self.l_nepataikei = Label(self.f_langas, text=f'Tavo spėjimas - {self.e_spejimas.get()} - neteisingas. Spėk dar kartą')
                self.l_nepataikei.pack()
                self.e_spejimas.delete(0, END)
            elif spejimas == atsakymas:
                self.e_spejimas.delete(0, END)
                self.l_atspejai = Label(self.f_langas, text='Sveikinu, štai Homosaurus Rex nuotrauka')
                nuotrauka = ImageTk.PhotoImage(Image.open('images\daiva\dino.jpg'))
                self.l_nuotrauka = Label(self.f_langas, image=nuotrauka)
                self.l_atspejai.pack()
                self.l_nuotrauka.pack()
            else:
                self.l_neatspejai = Label(self.f_langas, text='Neatspėjai, štai paguodai kačiuko nuotrauka')
                nuotrauka2 = ImageTk.PhotoImage(Image.open('images\daiva\cat.jpg'))
                self.l_nuotrauka2 = Label(self.f_langas, image=nuotrauka2)
                self.l_neatspejai.pack()
                self.l_nuotrauka2.pack()
                break

        self.main.mainloop()