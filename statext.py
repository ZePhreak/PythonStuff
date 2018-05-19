import numpy as np
from math import *
stats = [ "Determination", "Crit", "Direct Hit" ]

#Load CSVS
data_list = ['det3.csv','crit.csv','direct.csv','tenacity.csv','ss.csv']
datafile = [np.loadtxt(file, delimiter=",") for file in data_list]


def stat_extrapolate():
	import var
	#Variables#
	stat_flags = [True, True, True]
	r = 0
	x = floor(float(var.request6) / 40 ) * 40
	#Variables#
	for i in range(3):
		det_array = [0,0]
		crit_array = [0,0]
		direct_array = [0,0]
	#Search by player stats + max possible stat as long as it doesn't exceed max possible meld if state = true
		if stat_flags[0]:
			det_data1 = np.searchsorted(np.squeeze(datafile[0][0]), (float(var.p_det) + min(int(var.det_request), x)), side='left')
			det_array = datafile[0][:, det_data1-1]
		if stat_flags[1]:
			crit_data1 = np.searchsorted(np.squeeze(datafile[1][0]), (float(var.p_crit) + min(int(var.crit_request), x)), side='left')
			crit_array = datafile[1][:, crit_data1-1]
		if stat_flags[2]:
			direct_data1 = np.searchsorted(np.squeeze(datafile[2][0]), (float(var.p_direct) + min(int(var.direct_request), x)), side='left')
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
			x = x - min(var.det_request, x)
		if beststat_ind == 1:
			x = x - min(var.crit_request, x)
		if beststat_ind == 2:
			x = x - min(var.direct_request, x)
#Separate each runs output into separate variables
		if i == 0:
			stat_extra1 = bestmults[beststat_ind]
			stat_extra2 = beststat_val
			stat_info1 = stats[beststat_ind]
			var.stat_info1 = stat_info1
			var.stat_extra1 = stat_extra1
			var.stat_extra2 = stat_extra2
		if i == 1:
			stat_extra3 = bestmults[beststat_ind]
			stat_extra4 = beststat_val
			stat_info2 = stats[beststat_ind]
			var.stat_info2 = stat_info2
			var.stat_extra3 = stat_extra3
			var.stat_extra4 = stat_extra4
		if i == 2:
			import gui3
			stat_extra5 = bestmults[beststat_ind]
			stat_extra6 = beststat_val
			stat_info3 = stats[beststat_ind]
			var.stat_info3 = stat_info3
			var.stat_extra5 = stat_extra5
			var.stat_extra6 = stat_extra6
			gui3.callback(3)

def scatter():
	print("Scatter Called")
	var.legend([])
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
