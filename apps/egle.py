from tkinter import *
from PIL import ImageTk, Image



class Egle():

    def __init__(self, main):
        self.main = main
        self.main.title("Eglės skaičiuoklė")
        self.langas = Frame(self.main)
        self.langas.geometry = ("1200x300")
        self.langas.configure(bg="#F3EFE0")
        photo = ImageTk.PhotoImage(Image.open('images/egle/kmi.png'))
        px=10
        py=10
       
        self.teiginys = Label(self.langas, text="PASISKAIČIUOKITE SAVO KŪNO MASĖS INDEKSĄ", relief=SUNKEN, bg="#22A39F", fg="#F3EFE0", font=('Helvetica bold', 24))
        self.u_ugis = Label(self.langas, text="ĮVESKITE SAVO ŪGĮ CM.: ", border=5, bg="#22A39F", fg="#F3EFE0", font=('Helvetica bold', 14))
        self.ugis_ivestis = Entry(self.langas, bd=4, relief=SUNKEN, bg="#22A39F", width=5)
        self.s_svoris = Label(self.langas, text="ĮVESKITE SAVO SVORĮ KG.: ", border=5, bg="#22A39F", fg="#F3EFE0", font=('Helvetica bold', 14))
        self.svoris_ivestis = Entry(self.langas, bd=4, relief=SUNKEN, bg="#22A39F", width=5)
        self.skaiciuoti = Button(self.langas, text="SKAIČIUOTI", command=self.kmi_skaiciuokle, bd=10, highlightbackground="#F3EFE0", fg="#22A39F", font=('Helvetica bold', 20))
        self.parodymas = Label(self.langas, text="", relief=SUNKEN, bd=10, bg="#22A39F")
        self.paveiksliukas = Label(self.main, image=photo)
        self.langas.bind('<Return>', self.kmi_skaiciuokle)
  
        self.teiginys.grid(row=0, column=0, padx=px, pady=py)
        self.u_ugis.grid(row=3, column=0, padx=px, pady=py)
        self.ugis_ivestis.grid(row=4, column=0, padx=1, pady=1)
        self.s_svoris.grid(row=1, column=0, padx=px, pady=py)
        self.svoris_ivestis.grid(row=2, column=0, padx=1, pady=1)
        self.skaiciuoti.grid(row=5, column=0, padx=px, pady=py)
        self.parodymas.grid(row=6, column=0, padx=px, pady=py)
        self.langas.pack()
        self.paveiksliukas.pack()

        self.langas.mainloop()

    def kmi_skaiciuokle(self):
        ugis = int(self.ugis_ivestis.get())
        svoris = int(self.svoris_ivestis.get())
        kmi = svoris / (ugis/100)**2
        self.parodymas['text'] = f'{kmi:.1f}'

