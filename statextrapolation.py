import var
import numpy as np

#Load CSVS
data_list = ['det3.csv','crit.csv','direct.csv','tenacity.csv','ss.csv']
datafile = [np.loadtxt(file, delimiter=",") for file in data_list]



def stat_extrapolate():
	#Variables#
	stat_flags = [True, True, True]
	i = 0
	x = floor(float(var.request6) / 40 ) * 40
	det_array = [0,0]
	crit_array = [0,0]
	direct_array = [0,0]
	#Variables#
	while not stat_flags == [False, False, False]:
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
				x = x - min(float(var.det_request), x)
				print(x)
			if beststat_ind == 1:
				x = x - min(float(var.crit_request), x)
				print(x)
			if beststat_ind == 2:
				x = x - min(float(var.direct_request), x)
				print(x)
	#Separate each runs output into separate variables
			if i == 0:
				global stat_extra1
				global stat_extra2
				global stat_info1
				stat_extra1 = bestmults[beststat_ind]
				stat_extra2 = beststat_val
				stat_info1 = stats[beststat_ind]
				var.stat_info1 = stat_info1
				var.stat_extra1 = stat_extra1
				var.stat_extra2 = stat_extra2
				stat+extra 2
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
				var.stat_info2 = stat_info2
				var.stat_extra3 = stat_extra3
				var.stat_extra4 = stat_extra4
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
				var.stat_info3 = stat_info3
				var.stat_extra5 = stat_extra5
				var.stat_extra6 = stat_extra6
				scatter()
			i = i + 1
