# -*- coding: utf-8 -*-
from tkinter import *

class App():
    def __init__(self,root):
        Label(text="Press any key to continue!").grid(row=0,column=0)
        self.state = 'startup'

    def loop(self):       
        # some method to check if the user has pressed any key goes here
        if self.state == 'startup':
            Label(text="The Game is starting now!").grid(row=0,column=0)
        elif self.state == 'running':
            Label(text="Key Pressed!").grid(row=0,column=0)

        root.after(20, self.loop)

    def key(self,event):
        if self.state == 'startup':
            self.state = 'running'


root = Tk() 
game_app = App(root)
root.bind('<Key>',game_app.key)
root.after(20, game_app.loop)
root.mainloop()