from tkinter import *
from apps.destytojas import Destytojas
from apps.egle import Egle

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        self.b_egle = Button(self.f_catalog, text="Eglė", command=self.run_egle)
        
        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.b_egle.pack()
        self.f_catalog.pack()

    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)
    
    def run_egle(self):
        self.window_egle = Toplevel(self.main)
        self.app = Egle(self.window_egle)
