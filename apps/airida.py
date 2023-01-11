from tkinter import *


class Airida():
    def __init__(self, main):
        self.main = main
        self.main.title("Pasisveikinimo langas")
        self.l_vardas = Label(self.main, text='Iveskite varda', border=5)
        self.e_vardas = Entry(self.main)
        self.mygtukas = Button(self.main, text="Patvirtinti", command=self.pasisveikinti)
        self.l_pasisveikinimas = Label(self.main, text="Pasisveikinimo vieta", relief=SUNKEN, border=2)

        self.l_vardas.grid(row=0, column=0, sticky=E)
        self.e_vardas.grid(row=0, column=1)
        self.mygtukas.grid(row=0, column=2)
        self.l_pasisveikinimas.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.main.mainloop()

    def pasisveikinti(self):
        self.l_pasisveikinimas['text'] = f"Labas, {self.e_vardas.get()}"
        self.e_vardas.delete(0, END)