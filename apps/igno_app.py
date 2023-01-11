from tkinter import *

class IgnoApp():
    def __init__(self, main):
        self.main = main
        self.main.title("Igno TODO programa")
        self.main.geometry("300x400")

        self.frame_top = Frame(self.main)
        self.frame_bottom = Frame(self.main)
        self.label = Label(self.frame_top, text="Tasks: 0")
        self.list_box = Listbox(self.frame_top)
        self.scroolbar = Scrollbar(self.frame_top, command=self.list_box.yview)
        self.list_box.config(yscrollcommand=self.scroolbar.set)
        self.input = Entry(self.frame_bottom)
        self.button_add = Button(self.frame_bottom, text="Add task", width=10, comman=self.add_task)
        self.button_delete = Button(self.frame_bottom, text="Delete task", width=10, command=self.delete_task)
        self.button_clear_list = Button(self.frame_bottom,text="Clear All", width=10, command=self.clear_list )
        self.button_close = Button(self.frame_bottom, text="Close", width=10,command=self.main.destroy)
        
        self.frame_top.pack()
        self.frame_bottom.pack()
        self.label.pack()
        self.list_box.pack(side=LEFT)
        self.scroolbar.pack(side=RIGHT, fill=Y)
        self.input.pack()
        self.button_add.pack()
        self.button_delete.pack()
        self.button_clear_list.pack()
        self.button_close.pack()
        self.count_tasks()
    
    def count_tasks(self):
        tasks_amount = len(self.list_box.get(0, END))
        self.label['text'] = f"Tasks: {tasks_amount}"

    def add_task(self):
        input_text = self.input.get()
        if input_text != '':
            self.list_box.insert(END, input_text)
            self.input.delete(0, END)
            self.count_tasks()
        
    def delete_task(self):
        self.list_box.delete(self.list_box.curselection())
        self.count_tasks()

    def clear_list(self):
        self.list_box.delete(0, END)
        self.count_tasks()
    
    
