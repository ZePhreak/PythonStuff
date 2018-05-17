from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import tkinter as tk
import time
import pickle
import var


#Pickles! Saving inputs
def savestats():
	p_det = var.p_det
	p_direct = var.p_direct
	p_crit = var.p_crit
	det_request = var.det_request
	direct_request = var.direct_request
	crit_request = var.crit_request
	request6 = var.request6
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

#Load Pickle
def loadstats():
	try:
		s1 = askopenfilename(initialdir = "%userprofile%\Documents",title = "Select file",filetypes = (("Build File","*.p"),("all files","*.*")))
		f1 = open(s1, 'rb')
		p_det = int(pickle.load(f1))
		p_direct = int(pickle.load(f1))
		p_crit = int(pickle.load(f1))
		det_request = int(pickle.load(f1))
		direct_request = int(pickle.load(f1))
		crit_request = int(pickle.load(f1))
		request6 = int(pickle.load(f1))
		#Set Labels
		var.p_det = p_det
		var.p_direct = p_direct
		var.p_crit = p_crit
		var.det_request = det_request
		var.direct_request = direct_request
		var.crit_request = crit_request
		var.request6 = request6
	except:
		pass
