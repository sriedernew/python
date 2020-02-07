from tkinter import *
import tkinter.font
window = Tk()
window.title("paddelpaddel")
window.geometry('600x200')
lbl = Label(window, text="Boot:")
lbl.grid(column=0, row=0)
lbltxt =  Label(window, text="Bitte Boot eintragen",font = ("arial",12,"bold"))
lbltxt.grid(column=3, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
def clicked():
    eingabe = txt.get()
    lbltxt.configure(text=eingabe)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()