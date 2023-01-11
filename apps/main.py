from tkinter import *
from apps.destytojas import Destytojas
from apps.airida import Airida

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        self.airida_mygtukas = Button(self.main, text="Airida", command=self.run_airida)
        
        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.f_catalog.pack()
        self.airida_mygtukas.pack()

    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)

    def run_airida(self):
        self.window_airida = Toplevel(self.main)
        self.app = Airida(self.window_airida)



