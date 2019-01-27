import tkinter as tk

class Result(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Result")
        self.geometry('250x150+400+100')

        self.label = tk.Label(self)
        self.label.pack()
