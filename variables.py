from math import * 
from decimal import * 
import csv
import numpy as np

 
#Variables 
run = 1
#Character 
p_crit = 1812
p_direct = 1559
p_det = 1342
p_weapon = 105 
p_auto = 94 
p_attackpower = 2873 
#Abilities 
HeavyThrust = 180 
#Constants 
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
#While Loop Variables
stats = [ "Determination", "Crit", "Direct Hit" ] 
stat_flags = [True, True, True]
det_data1 = 1
crit_data1 = 1
direct_data1 = 1
#Multiply Section 
DetMult = (1000 + floor((SSA * (p_det - basemain)) / jobmod )) / 1000 
DirectChance = floor( p_direct - basesub) / 39.09 * 0.01 
DirectMult = (DirectChance * 1.25 + (1 - DirectChance)) 
CritChance = floor((0.05 + (p_crit - basesub) /108.5 * 0.01) *1000) / 1000 
CritDamage = floor(p_crit - basesub)/108.5 * 0.01 +1.4 
CritMult = (CritDamage * CritChance) + (1 - CritChance) 
AttackPower = (1 + floor(SSA * (p_attackpower - basemain) / basemain) /100) 
 
   
#If told to run then run Forest run! 
if run : 
	print("Character Stats") 
	print("Direct:", str(p_direct) + "\n" "Crit:", str(p_crit) + "\n" "Determination:", str(p_det) + "\n") 
	print("Stat Multipliers") 
	print("\n".join(map(str, [DirectChance,DetMult,DirectMult])) + "\n")
	print("\n".join(map(str, [CritChance,CritDamage,CritMult,AttackPower])) + "\n")

#Input Damage Calculations
request = input("Test Ability Damage? y/n  ") 
if request == "y" : 
    print("HeavyThrust: ", (int(((HeavyThrust) / 100) *  (DetMult) * (DirectMult) * (CritMult) * (p_weapon) * (AttackPower)))) 
	
#User Meld Input
det_request = int(input("Input Max Det: "))
crit_request = int(input("Input Max Crit: "))
direct_request = int(input("Input Max Direct: "))
request6 = int(input("Input Max Possible Meld: "))
	
#Step Damage Increase
data_list = ['det3.csv','crit.csv','direct.csv']
datafile = [np.loadtxt(file, delimiter=",") for file in data_list]
request2 = input("Find Best Stats?")
if request2 == "y" :
	det_data = np.searchsorted(np.squeeze(datafile[0][0]), (p_det + (int)(det_request)), side='left')
	crit_data = np.searchsorted(np.squeeze(datafile[1][0]), (p_crit + (int)(crit_request)), side='left')
	direct_data = np.searchsorted(np.squeeze(datafile[2][0]), (p_direct + (int)(direct_request)), side='left')
	print("\n".join([str(datafile[0][1, det_data-1]), str(datafile[1][1, crit_data-1]), str(datafile[2][1, direct_data-1]) ]))

#Loop finding best stat until x resolves
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
	#Print relevant info
		print('------------------------')
		print(stats[beststat_ind] ) 
		print('Multiplier: ' + str(bestmults[beststat_ind]))
		print('Materia: ' + str(beststat_val))			
	#Debug Prints
		#print(x)
		#print(beststat_ind)
		#print(beststat_remainder)
		#print(stat_flags)