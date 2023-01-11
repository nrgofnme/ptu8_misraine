from tkinter import *
from apps.main import MainApp

def run_main_app():
    root = Tk()
    root.title("PTU8 Mišrainė")
    root.geometry("500x500")
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_main_app()