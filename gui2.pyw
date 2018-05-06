from tkinter import *
import variables


master = Tk()
master.title("FFXIV Quick Math")
master.geometry("400x400")
Label(master, text="Determination").grid(row=0)
Label(master, text="Direct Hit").grid(row=1)
Label(master, text="Crit").grid(row=2)
B = Button(top, text = "Hello", command = stat_extrapolate)
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

mainloop()