from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.ttk as ttk
import tkinter as tk
import time
#from variables import stat_extrapolate



#MainApp
master = Tk()
master.title("FFXIV Quick Math")
master.geometry("500x300")
	


#Tab Stuff
rows = 0
while rows < 50:
	master.rowconfigure(rows, weight=1)
	master.columnconfigure(rows, weight=1)
	rows += 1
 
#Tab Placement
nb = ttk.Notebook(master)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
#Tab 1
page1 = ttk.Frame(nb)
nb.add(page1, text='Character Stats')

Label(page1, text="Determination:", anchor="e", width=12).grid(row=0)
Label(page1, text="Direct Hit:", anchor="e", width=12).grid(row=1)
Label(page1, text="Critical Hit:", anchor="e", width=12).grid(row=2)

e1 = Entry(page1)
e2 = Entry(page1)
e3 = Entry(page1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

#Show Stats Function
def showstats():
	updated_label = time.strftime(e1.get())
	lbl4.configure(text = updated_label)
	updated_label2 = time.strftime(e2.get())
	lbl5.configure(text = updated_label2)
	updated_label3 = time.strftime(e3.get())
	lbl6.configure(text = updated_label3)

button = Button(page1, text="Update", command = showstats)
button.grid(column=3, row= 1, padx =10)

#Setting Stat Info Block
#Show Stat Block
lbl1 = Label(page1, text = 'Determination:', anchor="e", width=12)
lbl1.grid(column=4, row=0)
lbl2 = Label(page1, text = 'Direct Hit:', anchor="e", width=12)
lbl2.grid(column=4, row=1)
lbl3 = Label(page1, text = 'Critical Hit:', anchor="e", width=12)
lbl3.grid(column=4, row=2)
lbl4 = Label(page1, text = 'Waiting')
lbl4.grid(column=5, row=0)
lbl5 = Label(page1, text = 'Waiting')
lbl5.grid(column=5, row=1)
lbl6 = Label(page1, text = 'Waiting')
lbl6.grid(column=5, row=2)
#Loop Till Updates




#Tab 2
page2 = ttk.Frame(nb)
nb.add(page2, text='Stat Extrapolation')




#End

mainloop()