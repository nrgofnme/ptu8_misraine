from tkinter import *
from apps.destytojas import Destytojas
from apps.daiva import Daiva

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        self.b_daiva = Button(self.f_catalog, text='Daiva', command=self.run_daiva)
        
        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.b_daiva.pack()
        self.f_catalog.pack()

    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)

    def run_daiva(self):
        self.window_daiva = Toplevel(self.main)
        self.app = Daiva(self.window_daiva)