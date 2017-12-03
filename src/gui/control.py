import tkinter as tk

class Control(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Control")
        self.geometry('250x150+1200+100')

        self.increaser = tk.Button(self, text="+")
        self.increaser.pack()

        self.decreaser = tk.Button(self, text="-")
        self.decreaser.pack()
