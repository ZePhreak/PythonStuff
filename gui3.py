from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.ttk as ttk
import tkinter as tk
import time
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from math import *
import csv
import numpy as np
from numpy import arange, sin, pi
import pickle
#Graph Imports
import matplotlib as mpl
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2TkAgg)
from matplotlib.figure import Figure
import re
from decimal import *
mpl.use('TkAgg')

#Variables
stats = [ "Determination", "Crit", "Direct Hit" ]
det_data1 = 1
crit_data1 = 1
direct_data1 = 1
p_det = 0
p_direct = 0
p_crit = 0
det_request = 0
direct_request = 0
crit_request = 0
request6 = 0
stat_extra1 = 0
stat_extra2 = 0
stat_extra3 = 0
stat_extra4 = 0
stat_extra5 = 0
stat_extra6 = 0
stat_info1 = 0
stat_info2 = 0
stat_info3 = 0

#Load CSVS
data_list = ['det3.csv','crit.csv','direct.csv','tenacity.csv','ss.csv']
datafile = [np.loadtxt(file, delimiter=",") for file in data_list]




#MainApp
master = Tk()
master.title("FFXIV Quick Math")
master.geometry("1200x650")

#Tab Stuff
rows = 0
while rows < 50:
	master.rowconfigure(rows, weight=1)
	master.columnconfigure(rows, weight=1)
	rows += 1

#Tab Placement
nb = ttk.Notebook(master)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

######################################## Character Stats ########################################
page1 = ttk.Frame(nb)
nb.add(page1, text='Character Stats')

#Start showing info
Label(page1, text="Determination:", anchor="e", width=12).grid(row=0)
Label(page1, text="Direct Hit:", anchor="e", width=12).grid(row=1)
Label(page1, text="Critical Hit:", anchor="e", width=12).grid(row=2)

e1 = Entry(page1).grid(row=0, column=1)
e2 = Entry(page1).grid(row=1, column=1)
e3 = Entry(page1).grid(row=2, column=1)


#Show Stats Function
def showstats():
	p_det = time.strftime(e1.get())
	lbl4.configure(text = p_det)
	p_direct = time.strftime(e2.get())
	lbl5.configure(text = p_direct)
	p_crit = time.strftime(e3.get())
	lbl6.configure(text = p_crit)

button = Button(page1, text="Update", command = showstats)
button.place(x=100, y=68)
#button.grid(column=3, row= 1)

#Setting Stat Info Block
#Show Stat Block
lbl1 = Label(page1, text = 'Determination:', anchor="e", width=12)
lbl1.grid(column=4, row=0)
lbl2 = Label(page1, text = 'Direct Hit:', anchor="e", width=12)
lbl2.grid(column=4, row=1)
lbl3 = Label(page1, text = 'Critical Hit:', anchor="e", width=12)
lbl3.grid(column=4, row=2)
lbl4 = Label(page1, text = 'Waiting...')
lbl4.grid(column=5, row=0)
lbl5 = Label(page1, text = 'Waiting...')
lbl5.grid(column=5, row=1)
lbl6 = Label(page1, text = 'Waiting...')
lbl6.grid(column=5, row=2)

######################################## Tab 2 ########################################
page2 = ttk.Frame(nb)
nb.add(page2, text='Stat Extrapolation')
#Input Variables
p = PanedWindow(page2, bg="grey", borderwidth=1, height=85, orient=VERTICAL)
p.grid(row=0, column=0)
Label(p, text="Max Determination:", anchor="e", width=15).grid(row=0)
Label(p, text="Max Direct Hit:", anchor="e", width=15).grid(row=1)
Label(p, text="Max Critical Hit:", anchor="e", width=15).grid(row=2)
Label(p, text="Max Stat Meld:", anchor="e", width=15).grid(row=3)

e4 = Entry(p)
e5 = Entry(p)
e6 = Entry(p)
e7 = Entry(p)

e4.grid(row=0, column=1)
e5.grid(row=1, column=1)
e6.grid(row=2, column=1)
e7.grid(row=3, column=1)

#Extrapolation Info Output
#Info
p2 = PanedWindow(page2, bg="grey", borderwidth=1, orient=VERTICAL)
p2.grid(row=0, column=2)
Label(p2, text = "Stat: ", anchor="e", width=10).grid(row=0, column=2)
Label(p2, text = "Multiplier: ", anchor="e", width=10).grid(row=1, column=2)
Label(p2, text = "Materia: ", anchor="e", width=10).grid(row=2, column=2)
#1st Stat
p1 = PanedWindow(page2, bg="grey", borderwidth=1, orient=VERTICAL)
p1.grid(row=0, column=3)
statinfo1 = Label(p1, text ="Waiting...", anchor="w", width=12)
statinfo1.grid(row=0, column=3)
statinfo2 = Label(p1, text ="Waiting...", anchor="w", width=12)
statinfo2.grid(row=1, column=3)
statinfo3 = Label(p1, text ="Waiting...", anchor="w", width=12)
statinfo3.grid(row=2, column=3)
#2nd Stat
p3 = PanedWindow(page2, bg="grey", borderwidth=1, orient=VERTICAL)
p3.grid(row=0, column=4)
statinfo4 = Label(p3, text ="Waiting...", anchor="w", width=12)
statinfo4.grid(row=0, column=4)
statinfo5 = Label(p3, text ="Waiting...", anchor="w", width=12)
statinfo5.grid(row=1, column=4)
statinfo6 = Label(p3, text ="Waiting...", anchor="w", width=12)
statinfo6.grid(row=2, column=4)
#3rd Stat
p4 = PanedWindow(page2, bg="grey", borderwidth=1, orient=tk.VERTICAL)
p4.grid(row=0, column=5)
statinfo7 = Label(p4, text ="Waiting...", anchor="w", width=12)
statinfo7.grid(row=0, column=5)
statinfo8 = Label(p4, text ="Waiting...", anchor="w", width=12)
statinfo8.grid(row=1, column=5)
statinfo9 = Label(p4, text ="Waiting...", anchor="w", width=12)
statinfo9.grid(row=2, column=5)

def showstats1():
	det_request = time.strftime(e4.get())
	#lbl7.configure(text = updated_label4)
	direct_request = time.strftime(e5.get())
	#lbl8.configure(text = updated_label5)
	crit_request = time.strftime(e6.get())
	#lbl9.configure(text = updated_label6)
	request6 = time.strftime(e7.get())
	#lbl10.configure(text = updated_label7)

button1 = Button(page2, text="Update", command = showstats1)
button1.place(x=100, y=90)
#button1.grid(column=1, row= 4)

#Graph Stat Extrapolation
fig = plt.Figure(figsize=(5.5, 5), dpi=100)
global a
a = fig.add_subplot(111)
x = datafile[0][0]
x1 = datafile[0][1]
y = datafile[1][0]
y1 = datafile[1][1]
z = datafile[2][0]
z1 = datafile[2][1]
t = datafile[3][0]
t1 = datafile[3][1]
s = datafile[4][0]
s1 = datafile[4][1]
global canvas
canvas = FigureCanvasTkAgg(fig, master=page2)
plt.ion()

#Graph Plotting
#Checking State
showDet = IntVar(value=1)
showCrit = IntVar(value=1)
showDirect = IntVar(value=1)
showTen = IntVar(value=1)
showS = IntVar(value=1)

#State of Checkboxes (CLEAN UP)################################################################
def stat_state():
	if showDet:
		if det_plot.get_visible():
			det_plot.set_visible(False)
		else:
			det_plot.set_visible(True)
		a.legend()
		canvas.draw()

def stat_state1():
	if showCrit:
		if crit_plot.get_visible():
			crit_plot.set_visible(False)
		else:
			crit_plot.set_visible(True)
		a.legend()
		canvas.draw()

def stat_state2():
	if showDirect:
		if direct_plot.get_visible():
			direct_plot.set_visible(False)
		else:
			direct_plot.set_visible(True)
		a.legend()
		canvas.draw()

def stat_state3():
	if showTen:
		if ten_plot.get_visible():
			ten_plot.set_visible(False)
		else:
			ten_plot.set_visible(True)
		a.legend()
		canvas.draw()

def stat_state4():
	if showS:
		if s_plot.get_visible():
			s_plot.set_visible(False)
		else:
			s_plot.set_visible(True)
		a.legend()
		canvas.draw()

###########################################################################################
#Setting up Graph
det_plot, = a.plot(x, x1, label='Determination')
crit_plot, = a.plot(y, y1, label='Crit')
direct_plot, = a.plot(z, z1, label='Direct')
ten_plot, = a.plot(t, t1, label='Tenacity')
s_plot, = a.plot(s, s1, label="Skill/Spell Speed")

toolbar_frame = Frame(page2)
toolbar_frame.place(x=400,y=600)
toolbar = NavigationToolbar2TkAgg(canvas, toolbar_frame)
toolbar.update()
toolbar.grid(row=9, column=9)
a.legend()
a.set_title('Stats')
a.set_xlabel('Materia')
a.set_ylabel('Modifier')
fig.patch.set_facecolor('#F0F0F0')
a.set_facecolor(('#F0F0F0'))

# a tk.DrawingArea
canvas.draw()
canvas.get_tk_widget().grid(column=1, row= 7)
canvas._tkcanvas.grid(column=1, row= 7)

#Show Stat Button
Checkbutton(page2, text="Determination", variable=showDet, command=stat_state).place(x=780, y=200)
Checkbutton(page2, text="Crit", variable=showCrit, command=stat_state1).place(x=780, y=220)
Checkbutton(page2, text="Direct", variable=showDirect, command=stat_state2).place(x=780, y=240)
Checkbutton(page2, text="Tenacity", variable=showTen, command=stat_state3).place(x=780, y=260)
Checkbutton(page2, text="S Speed", variable=showS, command=stat_state4).place(x=780, y=280)

#Stat Extrapolation
def stat_extrapolate():
	#Variables
	stat_flags = [True, True, True]
	statinfo1.configure(text = 'Input Stats')
	statinfo2.configure(text = 'Input Stats')
	statinfo3.configure(text = 'Input Stats')
	statinfo4.configure(text = 'Input Stats')
	statinfo5.configure(text = 'Input Stats')
	statinfo6.configure(text = 'Input Stats')
	statinfo7.configure(text = 'Input Stats')
	statinfo8.configure(text = 'Input Stats')
	statinfo9.configure(text = 'Input Stats')
	i = 0
	#p_det = int(time.strftime(e1.get()))
	#p_direct = int(time.strftime(e2.get()))
	#p_crit = int(time.strftime(e3.get()))
	#det_request = int(time.strftime(e4.get()))
	#direct_request = int(time.strftime(e5.get()))
	#crit_request = int(time.strftime(e6.get()))
	#request6 = int(time.strftime(e7.get()))

	while not stat_flags == [False, False, False]:
		#Setting some variables
			x = floor(int(request6) / 40 ) * 40
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
				global stat_extra1
				global stat_extra2
				global stat_info1
				stat_extra1 = bestmults[beststat_ind]
				stat_extra2 = beststat_val
				stat_info1 = stats[beststat_ind]
				statinfo1.configure(text = stat_info1)
				statinfo2.configure(text = stat_extra1)
				statinfo3.configure(text = stat_extra2)
			if i == 1:
				global stat_extra3
				global stat_extra4
				global stat_info2
				stat_extra3 = bestmults[beststat_ind]
				stat_extra4 = beststat_val
				stat_info2 = stats[beststat_ind]
				statinfo4.configure(text = stat_info2)
				statinfo5.configure(text = stat_extra3)
				statinfo6.configure(text = stat_extra4)
			if i == 2:
				global stat_extra5
				global stat_extra6
				global stat_info3
				stat_extra5 = bestmults[beststat_ind]
				stat_extra6 = beststat_val
				stat_info3 = stats[beststat_ind]
				statinfo7.configure(text = stat_info3)
				statinfo8.configure(text = stat_extra5)
				statinfo9.configure(text = stat_extra6)
				d1 = (stat_extra2, stat_extra1)
				d2 = (stat_extra4, stat_extra3)
				d3 = (stat_extra6, stat_extra5)
				a.legend([])
				##########Lazy Colour Set#######
				if stat_info1 == 'Crit':
					c1 = 'orange'
				if stat_info1 == 'Determination':
					c1 = 'blue'
				if stat_info1 == 'Direct Hit':
					c1 = 'green'
				if stat_info2 == 'Crit':
					c2 = 'orange'
				if stat_info2 == 'Determination':
					c2 = 'blue'
				if stat_info2 == 'Direct Hit':
					c2 = 'green'
				if stat_info3 == 'Crit':
					c3 = 'orange'
				if stat_info3 == 'Determination':
					c3 = 'blue'
				if stat_info3 == 'Direct Hit':
					c3 = 'green'
				##########Lazy Colour Set End#######
				ps1 = a.scatter(d1[0],d1[1],40,c1, label=stat_info1)
				ps2 = a.scatter(d2[0],d2[1],40,c2, label=stat_info2)
				ps3 = a.scatter(d3[0],d3[1],40,c3, label=stat_info3)
				a.legend()
				canvas.draw()
				ps1.remove()
				ps2.remove()
				ps3.remove()
			i = i + 1




button2 = Button(page2, text="Calculate", command = stat_extrapolate)
#button2.place(x=380, y=90)
button2.grid(column=4, row= 4)


#Pickles! Saving inputs
def savestats():
	p_det = time.strftime(e1.get())
	p_direct = time.strftime(e2.get())
	p_crit = time.strftime(e3.get())
	det_request = time.strftime(e4.get())
	direct_request = time.strftime(e5.get())
	crit_request = time.strftime(e6.get())
	request6 = time.strftime(e7.get())
	#Dump each variable
	s = filedialog.asksaveasfilename(defaultextension=".p",initialdir = "%userprofile%\Documents",title = "Select file",filetypes = (("Build File",".p"),("all files","*.*")))
	f = open(s, 'wb')
	pickle.dump(p_det, f)
	pickle.dump(p_direct, f)
	pickle.dump(p_crit, f)
	pickle.dump(det_request, f)
	pickle.dump(direct_request, f)
	pickle.dump(crit_request, f)
	pickle.dump(request6, f)
button3 = Button(page1, text="Save", command = savestats)
button3.place(x=150, y=68)

#Load Pickle
def loadstats():
	s1 = askopenfilename(initialdir = "%userprofile%\Documents",title = "Select file",filetypes = (("Build File","*.p"),("all files","*.*")))
	f1 = open(s1, 'rb')
	global p_det
	global p_direct
	global p_crit
	global det_request
	global direct_request
	global crit_request
	global request6
	p_det = int(pickle.load(f1))
	p_direct = int(pickle.load(f1))
	p_crit = int(pickle.load(f1))
	det_request = int(pickle.load(f1))
	direct_request = int(pickle.load(f1))
	crit_request = int(pickle.load(f1))
	request6 = int(pickle.load(f1))
	#Set Labels
	lbl4.configure(text = p_det)
	lbl5.configure(text = p_direct)
	lbl6.configure(text = p_crit)
	#Show load
	#messagebox.showinfo("Title", [p_det, p_direct, p_crit, det_request, direct_request, crit_request, request6] )

#load pickle button
button4 = Button(page1, text="Load", command = loadstats)
button4.place(x=125, y=98)

######################################## Tab 3 - Gear Comparison ########################################
page3 = ttk.Frame(nb)
nb.add(page3, text='Gear Comparison')

Label(page3, text="Item 1", width=12).grid(row=0)
Label(page3, text="Item 2", width=12).grid(row=0, column=2)
Label(page3, text="Attack Power", width=12).grid(row=1, column=1)
Label(page3, text="Determination", width=12).grid(row=2, column=1)
Label(page3, text="Direct Hit", width=12).grid(row=3, column=1)
Label(page3, text="Critical Hit", width=12).grid(row=4, column=1)
Label(page3, text="S Speed", width=12).grid(row=5, column=1)

#Item 1
ap = IntVar()
ap1 = IntVar()
det = IntVar()
det1 = IntVar()
dh = IntVar()
dh1 = IntVar()
ch = IntVar()
ch1 = IntVar()
ss = IntVar()
ss1 = IntVar()
Entry(page3, textvariable=ap).grid(row=1)
Entry(page3, textvariable=det).grid(row=2)
Entry(page3, textvariable=dh).grid(row=3)
Entry(page3, textvariable=ch).grid(row=4)
Entry(page3, textvariable=ss).grid(row=5)

#Item 2
Entry(page3, textvariable=ap1).grid(row=1, column=2)
Entry(page3, textvariable=det1).grid(row=2, column=2)
Entry(page3, textvariable=dh1).grid(row=3, column=2)
Entry(page3, textvariable=ch1).grid(row=4, column=2)
Entry(page3, textvariable=ss1).grid(row=5, column=2)

#More Damage
Label(page3, text="Item 1", width=12).grid(row=0)
Label(page3, text="Item 2", width=12).grid(row=0, column=2)
Label(page3, text="Attack Power", width=12).grid(row=1, column=1)
Label(page3, text="Determination", width=12).grid(row=2, column=1)
Label(page3, text="Direct Hit", width=12).grid(row=3, column=1)
Label(page3, text="Critical Hit", width=12).grid(row=4, column=1)
Label(page3, text="S Speed", width=12).grid(row=5, column=1)

#Math
jobmod = 2170
basemain = 292
basesub = 364
CrtMb = 400
CrtA = 200
CrtCb = 50
DHA = 550
DetA = 130
SSA = 130
TNCA = 100
DetMult = (1000 + floor((SSA * (p_det - basemain)) / jobmod )) / 1000
DirectChance = floor( p_direct - basesub) / 39.09 * 0.01
DirectMult = (DirectChance * 1.25 + (1 - DirectChance))
CritChance = floor((0.05 + (p_crit - basesub) /108.5 * 0.01) *1000) / 1000
CritDamage = floor(p_crit - basesub)/108.5 * 0.01 +1.4
CritMult = (CritDamage * CritChance) + (1 - CritChance)
#AttackPower = (1 + floor(SSA * (p_attackpower - basemain) / basemain) /100)


#Compare Function
def compare_ap():
	AP = ap.get()
	AP1 = ap1.get()
	DET = det.get()
	DET1 = det1.get()
	DH = dh.get()
	DH1 = dh1.get()
	CH = ch.get()
	CH1 = ch1.get()
	SS = ss.get()
	SS1 = ss1.get()
	AttackPower1 = (1 + floor(SSA * (AP - basemain) / basemain) /100)
	AttackPower2 = (1 + floor(SSA * (AP1 - basemain) / basemain) /100)
	DetMult1 = (1000 + floor((SSA * (DET - basemain)) / jobmod )) / 1000
	DetMult2 = (1000 + floor((SSA * (DET1 - basemain)) / jobmod )) / 1000
	DirectChance1 = floor(DH - basesub) / 39.09 * 0.01
	DirectChance2 = floor(DH1 - basesub) / 39.09 * 0.01
	DirectMult1 = (DirectChance1 * 1.25 + (1 - DirectChance1))
	DirectMult2 = (DirectChance2 * 1.25 + (1 - DirectChance2))
	CritChance1 = floor((0.05 + (CH - basesub) /108.5 * 0.01) *1000) / 1000
	CritDamage1 = floor(CH - basesub)/108.5 * 0.01 +1.4
	CritMult1 = (CritDamage1 * CritChance1) + (1 - CritChance1)
	CritChance2 = floor((0.05 + (CH1 - basesub) /108.5 * 0.01) *1000) / 1000
	CritDamage2 = floor(CH1 - basesub)/108.5 * 0.01 +1.4
	CritMult2 = (CritDamage2 * CritChance2) + (1 - CritChance2)
	#Label Stuff
	AP_Inc = int((AttackPower2 - AttackPower1) *1000)/1000
	print(DetMult2, DetMult1)
	DET_Inc = int((DetMult2 - DetMult1) *1000)/1000
	DH_Inc = int((DirectMult2 - DirectMult1) *1000)/1000
	C_Inc = int((CritMult2 - CritMult1) *1000)/1000
	aplb.configure(text=AP_Inc)
	aplb1.configure(text=DET_Inc)
	aplb2.configure(text=DH_Inc)
	aplb3.configure(text=C_Inc)

aplb = Label(page3, text='Waiting', width=12)
aplb.grid(row=1, column=3)
aplb1 = Label(page3, text='Waiting', width=12)
aplb1.grid(row=2, column=3)
aplb2 = Label(page3, text='Waiting', width=12)
aplb2.grid(row=3, column=3)
aplb3 = Label(page3, text='Waiting', width=12)
aplb3.grid(row=4, column=3)



button = Button(page3, text="Calculate", command = compare_ap)
button.place(x=135, y=135)
######################################## Tab 4 - Rotation Planner ########################################
page4 = ttk.Frame(nb)
nb.add(page4, text='Rotation Planner')

#Ability Select
global Abilities
Abilities = ["Waiting for Input"]
var1 = StringVar(master)
var1.set(Abilities[0])
w1 = OptionMenu(page4, var1, Abilities)
w1.grid(row=1,column=0)

# Key-value dictionary with job name, ability list
ability_dict = {
	"Dragoon": ["Heavy Thrust","Impulse Drive", "Disembowel", "Chaos Thrust", "Wheeling Thrust", "Fang and Claw","True Thrust","Vorpal Thrust","Full Thrust"],
	"Bard" : ["Bard", "Ability"],
	"Red Mage" : ["adsf"]
}

def Class(var):
	Abilities = ability_dict[var]
	w1["menu"].delete(0,"end")
	for a in Abilities:
		w1["menu"].add_command(label = a, command = Ability())
		tk._setit(var1, a)
		#var1.set(Abilities[0])
		#Ability()
		#print(var1)


#Find Ability CSV
global ability2
ability2 = "Waiting"
def Ability():
	ability_data = np.genfromtxt('abilities.csv', delimiter=',', dtype=None)
	#tk._setit(ability1, var1.get())
	ability1 = var1.get()
	print(ability1)
	ability1_search = np.where(ability_data[0] == ability1, ability_data[2], ability_data[1])
	ability2 = ability1_search[1]
	print(ability2)

Label(page4, text=ability2, anchor="e", width=12).grid(row=1, column=1)


#Class Select
Classes = ["Bard","Black Mage","Dragoon","Machinist","Monk","Ninja","Red Mage","Samurai","Summoner"]
var = StringVar(master)
var.set("Pick Class")
w = OptionMenu(page4, var, *Classes, command=Class)
w.grid(row=0,column=0)



#End
master.iconbitmap(r'data\jump.ico')
mainloop()
