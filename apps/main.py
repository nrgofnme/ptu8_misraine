from tkinter import *
from apps.destytojas import Destytojas
from apps.giedrius import Giedrius

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        self.b_giedrius = Button(self.f_catalog, text="Giedrius", command=self.run_giedrius)

        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.b_giedrius.pack()
        self.f_catalog.pack()

    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)

    def run_giedrius(self):
        self.window_giedrius = Toplevel(self.main)
        self.app = Giedrius(self.window_giedrius)