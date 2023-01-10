from tkinter import *
from apps.destytojas import Destytojas
from apps.monika import Studente

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        
        self.b_studente = Button(self.f_catalog, text='Studente', command=self.run_studente)

        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.b_studente.pack()
        self.f_catalog.pack()
        
    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)

    def run_studente(self):
        self.window_studente = Toplevel(self.main)
        self.app2 = Studente(self.window_studente)
