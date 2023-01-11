from tkinter import *
from apps.destytojas import Destytojas
from apps.redas import Redas

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        self.b_redas = Button(self.f_catalog, text="Redas", command=self.run_redas)
        
        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.f_catalog.pack()
        self.b_redas.pack()

    def run_redas(self):
        self.window_redas = Toplevel(self.main)
        self.app = Redas(self.window_redas)

    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)
