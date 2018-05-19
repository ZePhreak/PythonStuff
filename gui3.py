#MainImports
import func
import var
import statext
#
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

#Callback
def callback(number):
	import var
	if number == 1:
		print('Load Stats Called')
		global lbl4, lbl5, lbl6
		func.loadstats()
		lbl4.configure(text = var.p_det)
		lbl5.configure(text = var.p_direct)
		lbl6.configure(text = var.p_crit)
	if number == 2:
		try:
			print('Stat Extrapolate Called')
			statext.stat_extrapolate()
			statinfo1.configure(text = var.stat_info1)
			statinfo2.configure(text = var.stat_extra1)
			statinfo3.configure(text = var.stat_extra2)
			statinfo4.configure(text = var.stat_info2)
			statinfo5.configure(text = var.stat_extra3)
			statinfo6.configure(text = var.stat_extra4)
			statinfo7.configure(text = var.stat_info3)
			statinfo8.configure(text = var.stat_extra5)
			statinfo9.configure(text = var.stat_extra6)
		except:
			pass
	if number == 3:
		print('Regraph Called')
		regraph()

#Main Protected
def gui():
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

	e1 = Entry(page1)
	e1.grid(row=0, column=1)
	e2 = Entry(page1)
	e2.grid(row=1, column=1)
	e3 = Entry(page1)
	e3.grid(row=2, column=1)


	#Show Stats Function
	def showstats():
		import var
		var.p_det = e1.get()
		lbl4.configure(text = var.p_det)
		var.p_direct = e2.get()
		lbl5.configure(text = var.p_direct)
		var.p_crit = e3.get()
		lbl6.configure(text = var.p_crit)

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
		import var
		var.det_request = e4.get()
		var.direct_request = e5.get()
		var.crit_request = e6.get()
		var.request6 = e7.get()

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
	global showDet, showCrit, showDirect, showTen, showS
	showDet = IntVar(value=1)
	showCrit = IntVar(value=1)
	showDirect = IntVar(value=1)
	showTen = IntVar(value=1)
	showS = IntVar(value=1)


	#State of Checkboxes (CLEAN UP)################################################################
	def stat_state():
		det_plot.set_visible(not det_plot.get_visible())
		try:
			det_plot1.set_visible(not det_plot1.get_visible())
		except:
			pass
		a.legend()
		canvas.draw()

	def stat_state1():
		crit_plot.set_visible(not crit_plot.get_visible())
		try:
			crit_plot1.set_visible(not crit_plot1.get_visible())
		except:
			pass
		a.legend()
		canvas.draw()

	def stat_state2():
		direct_plot.set_visible(not direct_plot.get_visible())
		try:
			direct_plot1.set_visible(not direct_plot1.get_visible())
		except:
			pass
		a.legend()
		canvas.draw()

	def stat_state3():
		ten_plot.set_visible(not ten_plot.get_visible())
		try:
			ten_plot1.set_visible(not ten_plot1.get_visible())
		except:
			pass
		a.legend()
		canvas.draw()

	def stat_state4():
		s_plot.set_visible(not s_plot.get_visible())
		try:
			s_plot1.set_visible(not s_plot1.get_visible())
		except:
			pass
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
	a.grid()
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

	#Graph Redraw
	def regraph():
		print('regraphing')
		a.clear()
		global det_plot1, crit_plot1, direct_plot1, ten_plot1, s_plot1
		c1 = 'orange'
		c2 = 'blue'
		c3 = 'green'
		det_plot1, = a.plot(x, x1, label='Determination')
		crit_plot1, = a.plot(y, y1, label='Crit')
		direct_plot1, = a.plot(z, z1, label='Direct')
		ten_plot1, = a.plot(t, t1, label='Tenacity')
		s_plot1, = a.plot(s, s1, label="Skill/Spell Speed")
		ps1 = a.scatter(var.d1[0],var.d1[1],40,c1, label=var.stat_info1)
		ps2 = a.scatter(var.d2[0],var.d2[1],40,c2, label=var.stat_info2)
		ps3 = a.scatter(var.d3[0],var.d3[1],40,c3, label=var.stat_info3)
		a.set_title('Stats')
		a.set_xlabel('Materia')
		a.set_ylabel('Modifier')
		a.grid()
		a.legend()
		canvas.draw()



	#Show Stat Button
	Checkbutton(page2, text="Determination", variable=showDet, command=stat_state).place(x=780, y=200)
	Checkbutton(page2, text="Crit", variable=showCrit, command=stat_state1).place(x=780, y=220)
	Checkbutton(page2, text="Direct", variable=showDirect, command=stat_state2).place(x=780, y=240)
	Checkbutton(page2, text="Tenacity", variable=showTen, command=stat_state3).place(x=780, y=260)
	Checkbutton(page2, text="S Speed", variable=showS, command=stat_state4).place(x=780, y=280)



	#def scatter():
	#					d1 = (var.stat_extra2, var.stat_extra1)
	#					d2 = (var.stat_extra4, var.stat_extra3)
	#					d3 = (var.stat_extra6, var.stat_extra5)
	#					var.legend([])
	#					##########Lazy Colour Set#######
	#					if stat_info1 == 'Crit':
	#						c1 = 'orange'
	#					if stat_info1 == 'Determination':
	#						c1 = 'blue'
	#					if stat_info1 == 'Direct Hit':
	#						c1 = 'green'
	#					if stat_info2 == 'Crit':
	#						c2 = 'orange'
	#					if stat_info2 == 'Determination':
	#						c2 = 'blue'
	#					if stat_info2 == 'Direct Hit':
	#						c2 = 'green'
	#					if stat_info3 == 'Crit':
	#						c3 = 'orange'
	#					if stat_info3 == 'Determination':
	#						c3 = 'blue'
	#					if stat_info3 == 'Direct Hit':
	#						c3 = 'green'
	#					##########Lazy Colour Set End#######
	#					a.clear()
	#					global det_plot1, crit_plot1, direct_plot1, ten_plot1, s_plot1
	#					showDet.get()
	#					det_plot1, = a.plot(x, x1, label='Determination')
	#					crit_plot1, = a.plot(y, y1, label='Crit')
	#					direct_plot1, = a.plot(z, z1, label='Direct')
	#					ten_plot1, = a.plot(t, t1, label='Tenacity')
	#					s_plot1, = a.plot(s, s1, label="Skill/Spell Speed")
	#					ps1 = a.scatter(d1[0],d1[1],40,c1, label=stat_info1)
	#					ps2 = a.scatter(d2[0],d2[1],40,c2, label=stat_info2)
	#					ps3 = a.scatter(d3[0],d3[1],40,c3, label=stat_info3)
	#					a.set_title('Stats')
	#					a.set_xlabel('Materia')
	#					a.set_ylabel('Modifier')
	#					a.grid()
	#					a.legend()
	#					canvas.draw()




	button2 = Button(page2, text="Calculate", command = lambda number = 2: callback(number) )
	#button2.place(x=380, y=90)
	button2.grid(column=4, row= 4)


	#Load and Save Buttons
	button3 = Button(page1, text="Save", command = func.savestats)
	button3.place(x=150, y=68)

	button4 = Button(page1, text="Load", command =lambda number = 1 : callback(number))
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


	#Find Ability CSV
	global ability2
	ability2 = "Waiting"
	def Ability():
		ability_data = np.genfromtxt('abilities.csv', delimiter=',', dtype=None)
		#tk._setit(ability1, var1.get())
		ability1 = var1.get()
		ability1_search = np.where(ability_data[0] == ability1, ability_data[2], ability_data[1])
		ability2 = ability1_search[1]

	Label(page4, text=ability2, anchor="e", width=12).grid(row=1, column=1)


	#Class Select
	Classes = ["Bard","Black Mage","Dragoon","Machinist","Monk","Ninja","Red Mage","Samurai","Summoner"]
	var = StringVar(master)
	var.set("Pick Class")
	w = OptionMenu(page4, var, *Classes, command=Class)
	w.grid(row=0,column=0)

	master.iconbitmap(r'data\jump.ico')
	mainloop()

#End
if __name__ == "__main__":
	gui()
