import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")
#win.resizable(0,0)

#Modify adding a Label
aLabel = ttk.Label(win,text="A Label")
aLabel.grid(column=0,row=0)
#Button Click Event Function
#ttk.Label(win,text="A Label").grid(column=0,row=0)
#win.mainloop()


#Button Click Event Function

def clickMe():
    action.configure(text="** I have been Clocked!")
    aLabel.configure(foreground="red")
    aLabel.configure(text="a Red Label")

#Adding button
action = ttk.Button(win,text="Click Me!",command=clickMe)
action.grid(column=1,row=0)

win.mainloop()
