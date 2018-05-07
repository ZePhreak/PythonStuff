from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import sleep



#MainApp
master = Tk()
master.title("FFXIV Quick Math")
master.geometry("400x400")
	
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

Label(page1, text="Determination").grid(row=0)
Label(page1, text="Direct Hit").grid(row=1)
Label(page1, text="Crit").grid(row=2)

e1 = Entry(page1)
e2 = Entry(page1)
e3 = Entry(page1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

#Show Stats Function
def showstats():
	if not e1.get():
		messagebox.showinfo("Information","Informative message")
	global s1
	s1.set(e1.get())
	master.update()

button = Button(page1, text="Update", command = showstats)
button.place(x = 215,y = 15)

#Setting Stat Info Block
s1 = ('waiting')
#Show Stat Block
lbl1 = Label(page1, textvariable= s1)
lbl1.grid(column=2, row=1)
#Loop Till Updates




#Tab 2
page2 = ttk.Frame(nb)
nb.add(page2, text='Stat Extrapolation')


#End
master.update()
mainloop()