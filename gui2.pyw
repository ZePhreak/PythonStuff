from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.ttk as ttk
import tkinter as tk
import time
from math import * 
import csv
import numpy as np

#Variables
stats = [ "Determination", "Crit", "Direct Hit" ] 
stat_flags = [True, True, True]
det_data1 = 1
crit_data1 = 1
direct_data1 = 1

#Load CSVS
data_list = ['det3.csv','crit.csv','direct.csv']
datafile = [np.loadtxt(file, delimiter=",") for file in data_list]



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


#Tab 2
page2 = ttk.Frame(nb)
nb.add(page2, text='Stat Extrapolation')
#Input Variables
Label(page2, text="Max Determination:", anchor="e", width=15).grid(row=0)
Label(page2, text="Max Direct Hit:", anchor="e", width=15).grid(row=1)
Label(page2, text="Max Critical Hit:", anchor="e", width=15).grid(row=2)
Label(page2, text="Max Stat Meld:", anchor="e", width=15).grid(row=3)

e4 = Entry(page2)
e5 = Entry(page2)
e6 = Entry(page2)
e7 = Entry(page2)

e4.grid(row=0, column=1)
e5.grid(row=1, column=1)
e6.grid(row=2, column=1)
e7.grid(row=3, column=1)

#Extrapolation Info Output
statinfo1 = Label(page2, text ="Waiting", anchor="e", width=15)
statinfo1.grid(row=0, column=2)
Label(page2, text ="Waiting", anchor="e", width=15).grid(row=0)
Label(page2, text ="Waiting", anchor="e", width=15).grid(row=0)
Label(page2, text ="Waiting", anchor="e", width=15).grid(row=0)

def showstats1():
	det_request = time.strftime(e4.get())
	lbl7.configure(text = updated_label4)
	direct_request = time.strftime(e5.get())
	lbl8.configure(text = updated_label5)
	crit_request = time.strftime(e6.get())
	lbl9.configure(text = updated_label6)
	request6 = time.strftime(e7.get())
	lbl10.configure(text = updated_label7)
	
button1 = Button(page2, text="Update", command = showstats1)
button1.grid(column=1, row= 4, padx =10)
button2 = Button(page2, text="Calculate", command = stat_extrapolate)
button2.grid(column=3, row= 1, padx =10)
#Stat Extrapolation
def stat_extrapolate():
	i = 0
	while not stat_flags == [False, False, False]:
		#Setting some variables
			x = floor(request6 / 40 ) * 40
			det_array = [0,0]
			crit_array = [0,0]
			direct_array = [0,0]
	#Search by player stats + max possible stat as long as it doesn't exceed max possible meld if state = true
			if stat_flags[0]: 
				det_data1 = np.searchsorted(np.squeeze(datafile[0][0]), (p_det + min(int(det_request), x)), side='left')
				det_array = datafile[0][:, det_data1-1]
			if stat_flags[1]:
				crit_data1 = np.searchsorted(np.squeeze(datafile[1][0]), (p_crit + min(int(crit_request), x)), side='left')
				crit_array = datafile[1][:, crit_data1-1]
			if stat_flags[2]:
				direct_data1 = np.searchsorted(np.squeeze(datafile[2][0]), (p_direct + min(int(direct_request), x)), side='left')
				direct_array = datafile[2][:, direct_data1-1]
	#Find the highest of the searches and mark it as found
			mult_data = np.array( [det_array, crit_array, direct_array] ).T
			bestmults = mult_data[1]
			beststat_ind = np.argmax(bestmults)
			beststat_val = mult_data[0][beststat_ind]
			beststat_remainder = floor(beststat_ind / 40 ) * 40
	#Update Variables
			stat_flags[beststat_ind] = False
			if beststat_ind == 0:
				x = x - min(det_request, x)
			if beststat_ind == 1:
				x = x - min(crit_request, x)
			if beststat_ind == 2:
				x = x - min(direct_request, x)
	#Separate each runs output into separate variables
			if i == 0:
				stat_extra1 = bestmults[beststat_ind]
				stat_extra2 = beststat_val
				stat_info1 = stats[beststat_ind]
				statinfo1.configure(text = stat_extra1)
			if i == 1:
				stat_extra3 = bestmults[beststat_ind]
				stat_extra4 = beststat_val
				stat_info2 = stats[beststat_ind] 
			if i == 2:
				stat_extra5 = bestmults[beststat_ind]
				stat_extra6 = beststat_val
				stat_info3 = stats[beststat_ind] 
			i = i + 1




#End

mainloop()