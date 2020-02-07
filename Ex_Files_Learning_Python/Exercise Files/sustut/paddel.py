from tkinter import *

def clicked():
    name = ent_name.get()
    boot = ent_boot.get()
    strecke = ent_strecke.get()
    zeit = ent_zeit.get()
    f = open("paddelei.txt","a+")
    text = "{},{},{},{}\n"
    f.write(text.format(name, boot, strecke, zeit))
    f.close()

window = Tk()
window.title("paddelpaddel")
window.geometry('500x200')
headline = Label(window,anchor='w',text="Eingabe Paddler:",font = ("arial",12,"bold"), justify='left',pady=10,padx=10)
headline.grid(column=0, row=0)

lbl_name = Label(window,anchor='w',text="Name:",width='10', justify='left',pady=5)
lbl_name.grid(column=0, row=1)
ent_name = Entry(window,width=30)
ent_name.grid(column=1, row=1)

lbl_boot = Label(window,anchor='w',text="Boot:",width='10', justify='left',pady=5)
lbl_boot.grid(column=0, row=2)
ent_boot = Entry(window,width=30)
ent_boot.grid(column=1, row=2)

lbl_strecke = Label(window,anchor='w',text="Strecke:",width='10', justify='left',pady=5)
lbl_strecke.grid(column=0, row=3)
ent_strecke = Entry(window,width=30)
ent_strecke.grid(column=1, row=3)

lbl_zeit = Label(window,anchor='w',text="Zeit:",width='10', justify='left',pady=5)
lbl_zeit.grid(column=0, row=4)
ent_zeit = Entry(window,width=30)
ent_zeit.grid(column=1, row=4)

btn = Button(window, text="save",command=clicked)
btn.grid(column=1,row=5,pady=10,ipadx=20)
quit_btn = Button(window, text="ende", command=window.quit)
quit_btn.grid(column=0,row=5,ipadx=20)

window.mainloop()
