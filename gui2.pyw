from tkinter import *
from tkinter import ttk


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
def showstats():
	text = Text(page1)
	text.insert(INSERT, "Hello.....")
	#text1 = Text ( e1.get() )
	#text2 = Text ( e2.get() )
	#text3 = Text ( e3.get() )
text = Text(page1)
text.tag_add("here", "1.0", "1.4")
button = Button(page1, text="Print", command = showstats)
button.place(x = 215,y = 15)
button.invoke()


#Tab 2
page2 = ttk.Frame(nb)
nb.add(page2, text='Stat Extrapolation')


#End
mainloop()