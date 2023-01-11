from tkinter import *
from apps.destytojas import Destytojas
from apps.kesgame import KesGame
from apps.edvardas import Edvardas
from apps.daiva import Daiva
from apps.sandra import Sandra
from apps.redas import Redas
from apps.egle import Egle
from apps.airida import Airida
from apps.dovydas import Studenciokas
from apps.monika import Studente
from apps.igno_app import IgnoApp
from apps.giedrius import Giedrius
from apps.lina import Lina
from apps.donatas import Donatas


class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, width=10, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, width=10, text="Destytojas", command=self.run_destytojas)
        self.b_giedrius = Button(self.f_catalog, width=10, text="Giedrius", command=self.run_giedrius)
        self.b_ignas = Button(self.f_catalog, width=10, text="Ignas",command=self.run_ignas)
        self.b_lina = Button(self.f_catalog, width=10, text="Lina", command=self.run_lina)
        self.b_studente = Button(self.f_catalog, width=10, text='Monika', command=self.run_studente)
        self.b_studenciokas = Button(self.f_catalog, width=10, text="Dovydas", command=self.run_kryptis)
        self.b_airida = Button(self.f_catalog, width=10, text="Airida", command=self.run_airida)
        self.b_egle = Button(self.f_catalog, width=10, text="Eglė", command=self.run_egle)
        self.b_donatas = Button (self.f_catalog, width=10, text='Donatas', command=self.run_donatas)
        self.b_redas = Button(self.f_catalog, width=10, text="Redas", command=self.run_redas)
        self.b_sandra = Button(self.f_catalog, width=10, text="Sandra", command=self.run_sandra)
        self.b_daiva = Button(self.f_catalog, width=10, text='Daiva', command=self.run_daiva)
        self.b_edvardas = Button(self.f_catalog, width=10, text="Edvardas", command=self.run_edvardas)
        self.b_kesgame = Button(self.f_catalog, width=10, text="Kesgame", command=self.run_kesgame)
        
        self.l_pasirinkimai.pack(side=TOP)
        self.b_destytojas.pack()
        self.b_ignas.pack()
        self.b_giedrius.pack()
        self.b_lina.pack()
        self.b_studente.pack()
        self.b_studenciokas.pack()
        self.b_airida.pack()
        self.b_egle.pack()
        self.b_donatas.pack()
        self.b_redas.pack()
        self.b_sandra.pack()
        self.b_daiva.pack()
        self.b_edvardas.pack()
        self.b_kesgame.pack()
        self.f_catalog.pack()

    def run_redas(self):
        self.window_redas = Toplevel(self.main)
        self.app = Redas(self.window_redas)

    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)

    def run_kesgame(self):
        self.window_kesgame = Toplevel(self.main)
        self.game = KesGame(self.window_kesgame) 
        self.game.pack_configure() 
    
    def run_edvardas(self):
        self.window_edvardas = Toplevel(self.main)
        self.app = Edvardas(self.window_edvardas)
        
    def run_daiva(self):
        self.window_daiva = Toplevel(self.main)
        self.app = Daiva(self.window_daiva)

    def run_sandra(self):
        self.window_sandra = Toplevel(self.main)
        self.app = Sandra(self.window_sandra)
    
    def run_egle(self):
        self.window_egle = Toplevel(self.main)
        self.app = Egle(self.window_egle)

    def run_airida(self):
        self.window_airida = Toplevel(self.main)
        self.app = Airida(self.window_airida)

    def run_kryptis(self):
        self.window_studenciokas = Toplevel(self.main)
        self.app = Studenciokas(self.window_studenciokas)

    def run_studente(self):
        self.window_studente = Toplevel(self.main)
        self.app2 = Studente(self.window_studente)

    def run_ignas(self):
        self.window_my_app = Toplevel(self.main)
        self.app = IgnoApp(self.window_my_app)

    def run_giedrius(self):
        self.window_giedrius = Toplevel(self.main)
        self.app = Giedrius(self.window_giedrius)

    def run_lina(self):
        self.window_lina = Toplevel(self.main)
        self.app = Lina(self.window_lina)

    def run_donatas(self):
        self.window_donatas = Toplevel(self.main)
        self.app = Donatas(self.window_donatas)
