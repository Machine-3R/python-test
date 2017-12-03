#!/usr/bin/env python

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

class Result(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Result")
        self.geometry('250x150+1500+100')

        self.label = tk.Label(self)
        self.label.pack()

class Application:
    value=0
    def __init__(self, controlGUI, resultGUI):
        self.control = controlGUI
        self.result = resultGUI
        self.control.increaser.bind("<Button-1>", self.handle_increment)
        self.control.decreaser.bind("<Button-1>", self.handle_decrement)
        self.result.label['text'] = self.value;
        
        self.control.mainloop()
        self.result.mainloop()
    
    def handle_increment(self, event):
        self.increase()
        self.result.label['text'] = self.value
    
    def handle_decrement(self, event):
        self.decrease()
        self.result.label['text'] = self.value
    
    def increase(self):
        self.value = self.value + 1
        
    def decrease(self):
        self.value = self.value - 1
        
    def __del__(self):
        print("Bye")
