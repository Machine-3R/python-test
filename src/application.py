
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
