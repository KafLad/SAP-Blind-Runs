######################
#       GUI         #
#  From SBT Branch  #
#####################


import tkinter as tk
from tkinter import font as tkfont

class BotApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}
        for F in (StartPage, LocationSetup, RunGame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



### This page will serve as a "menu" to navigate to the location setup & the Running Pages
class StartPage(tk.Frame):
    
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Location Setup",
                            command=lambda: controller.show_frame("LocationSetup"))
        button2 = tk.Button(self, text="Go to Bot Startup",
                            command=lambda: controller.show_frame("RunGame"))
        
        button1.pack()
        button2.pack()


### This page will serve as a means to dynamically locate where the mouse should be moving to
class LocationSetup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Location Setup Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        
        button.pack()


### This page will serve as a GUI indicator of what the bot is doing as well as a place to start running the script
class RunGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Bot Running Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()


app = BotApp()
app.mainloop()