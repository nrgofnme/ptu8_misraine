from tkinter import *
from apps.destytojas import Destytojas
from apps.edvardas import Edvardas

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        self.b_edvardas = Button(self.f_catalog, text="Edvardas", command=self.run_edvardas)
        
        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.b_edvardas.pack()
        self.f_catalog.pack()

    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)

    def run_edvardas(self):
        self.window_edvardas = Toplevel(self.main)
        self.app = Edvardas(self.window_edvardas)