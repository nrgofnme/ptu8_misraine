from tkinter import *
from apps.destytojas import Destytojas
from apps.sandra import Sandra

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        self.b_sandra = Button(self.f_catalog, text="Sandra", command=self.run_sandra)
        
        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.b_sandra.pack()
        self.f_catalog.pack()

    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)

    def run_sandra(self):
        self.window_sandra = Toplevel(self.main)
        self.app = Sandra(self.window_sandra)