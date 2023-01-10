from tkinter import *
from apps.destytojas import Destytojas
from apps.dovydas import Studenciokas

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        self.b_studenciokas = Button(self.f_catalog, text="Studenciokas", command=self.run_kryptis)

        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.f_catalog.pack()
        self.b_studenciokas.pack()

    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)

    def run_kryptis(self):
        self.window_studenciokas = Toplevel(self.main)
        self.app = Studenciokas(self.window_studenciokas)