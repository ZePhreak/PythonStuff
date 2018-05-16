from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import time
import pickle


#Pickles! Saving inputs
def savestats():
	p_det = time.strftime(gui3.e1.get())
	p_direct = time.strftime(gui3.e2.get())
	p_crit = time.strftime(gui3.e3.get())
	det_request = time.strftime(gui3.e4.get())
	direct_request = time.strftime(gui3.e5.get())
	crit_request = time.strftime(gui3.e6.get())
	request6 = time.strftime(gui3.e7.get())
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
	s1 = askopenfilename(initialdir = "%userprofile%\Documents",title = "Select file",filetypes = (("Build File","*.p"),("all files","*.*")))
	f1 = open(s1, 'rb')
	p_det_l = int(pickle.load(f1))
	p_direct_l = int(pickle.load(f1))
	p_crit_l = int(pickle.load(f1))
	det_request_l = int(pickle.load(f1))
	direct_request_l = int(pickle.load(f1))
	crit_request_l = int(pickle.load(f1))
	request6_l = int(pickle.load(f1))
	#Set Labels
	global p_det, p_direct, p_crit
	gui3.p_det.set(p_det_l)
	gui3.p_direct.set(p_direct_l)
	gui3.p_crit.set(p_crit_l)
