import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

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
    action.configure(text="Hello"+name.get()+' '+numberChosen.get())

#Changing our Label
ttk.Label(win,text="Enter a name: ").grid(column=0,row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=0,row=1)
#Adding button
action = ttk.Button(win,text="Click Me!",command=clickMe)
action.grid(column=3,row=1)

#action.configure(state="disabled")

ttk.Label(win,text="Choose number").grid(column=1,row=0)
number=tk.StringVar()
numberChosen = ttk.Combobox(win,width=12,textvariable=number,state='readonly')
numberChosen['values']=(1,2,4,42,100)
numberChosen.grid(columns=2,row=1)
numberChosen.current(0)

#Creating three checkbuttons
chVarDis=tk.IntVar()
check1=tk.Checkbutton(win,text="Disabled",variable=chVarDis,state="Disabled")
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn=tk.IntVar()
check2=tk.Checkbutton(win,text="Unchecked",variable=chVarUn,state="Disabled")
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W)

chVarEn=tk.IntVar()
check3=tk.Checkbutton(win,text="Enabled",variable=chVarEn,state="Disabled")
check3.select()
check3.grid(column=2,row=4,sticky=tk.W)

#Radio button
COLOR1="Blue"
COLOR2="GOLD"
COLOR3="RED"

def redCall():
    redSe1=redVar.get()
    if redSe1 == 1:win.configure(background=COLOR1)
    elif redSe1==2:win.configure(background=COLOR2)
    elif redSe1 ==3:win.congigure(background=COLOR3)

#create threee radio buttons using one variable

redVar=tk.IntVar()
red1=tk.Radiobutton(win,text=COLOR1,variable=redVar,value=1,command=redCall)
red1.grid(column=0,row=5,sticky=tk.W)

red2 = tk.Radiobutton(win, text=COLOR2, variable=redVar, value=2, command=redCall)
red2.grid(column=1, row=5, sticky=tk.W)

red3 = tk.Radiobutton(win, text=COLOR3, variable=redVar, value=3, command=redCall)
red3.grid(column=2, row=5, sticky=tk.W)

#using a scrolled text controt

scrolW=30
scrolH =3
scr = scrolledtext.ScrolledText(win,width=scrolW,height=scrolH,wrap=tk.WORD)
scr.grid(column=0,columnspan=3)

nameEntered.focus() #please cursor into name Entry
win.mainloop()
