from tkinter import *
from apps.destytojas import Destytojas
from apps.kesgame import KesGame


class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        self.b_kesgame = Button(self.f_catalog, width=10, text="Kesgame", command=self.run_kesgame)
        
        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.b_kesgame.pack()
        self.f_catalog.pack()
       
    
    
    
    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)


    def run_kesgame(self):
        self.window_kesgame = Toplevel(self.main)
        self.game = KesGame(self.window_kesgame) 
        self.game.pack_configure() 
    