import random
from tkinter import *

class KesGame(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Dice Game")
        self.label = Label(self, text="Welcome to the Dice Game!")
        self.label.pack()
        self.roll_button = Button(self, text="Roll the dice!", command=self.roll)
        self.roll_button.pack()
        self.result_label = Label(self)
        self.result_label.pack()
        self.pack()

    def roll(self):
        number = random.randint(1, 6)
        self.result_label.config(text=f"You rolled a {number}")


if __name__ == "__main__":
    root = Tk()
    app = KesGame(root)
    app.mainloop()