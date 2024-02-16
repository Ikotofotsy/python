#!/usr/bin/env python3
from tkinter import HIDDEN, NORMAL, Tk, Canvas
import pet

class App :
    def __init__(self) :
        self.root = Tk()
        self.configure_root()
        self.set_canvas(400, 400, 'grey')
        self.root.after(1000, self.blink)
        self.root.after(5000, self.sad)

    def configure_root(self) :
        self.root.resizable(False, False)
        self.root.geometry("-5+5")

    def set_canvas(self, width, height, bg_col) :
        self.canvas = Canvas(self.root, width = width, height = height)
        self.canvas.configure(bg = bg_col, highlightthickness = 0)
        self.pet = pet.face(self.canvas)
        self.canvas.pack()
    
    def blink(self) :
        self.pet.toggleEyes()
        self.root.after(250, self.pet.toggleEyes)
        self.root.after(3000, self.blink)
    
    def cheecky(self, event) :
        self.pet.toogle_tongue()
        self.pet.toogle_pupils()
        self.pet.hideHappy(event)
        self.root.after(1000, self.pet.toogle_tongue)
        self.root.after(1000, self.pet.toogle_pupils)

    def sad(self) :
        if self.pet.happy_level == 0 :
            self.canvas.itemconfigure(self.pet.mouth_happy, state = HIDDEN)
            self.canvas.itemconfigure(self.pet.mouth_normal, state = HIDDEN)
            self.canvas.itemconfigure(self.pet.mouth_sad, state = NORMAL)
        else :
            self.pet.happy_level-=1
        self.root.after(5000, self.sad)
            

if __name__ == '__main__' :
    app = App()
    app.canvas.bind('<Motion>', app.pet.showHappy)
    app.canvas.bind('<Leave>', app.pet.hideHappy)
    app.canvas.bind('<Double-1>', app.cheecky)
    app.root.mainloop()
    
    
    