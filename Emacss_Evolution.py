import numpy as np
import globalz as glb
import subprocess
from os import listdir
from os.path import isfile, join
import os
import glob


NCluster=glb.NCluster
bin_num=glb.bin_num
m_bin=glb.m_bin
r_bin=glb.r_bin


def run(x):
	return subprocess.Popen(x, shell=True, stdout=subprocess.PIPE).stdout.read()


def Emacss():

	filename='Initial.txt' #sys.argv[1]

	with open(filename, 'r') as f:
		lines = f.readlines()



	base = r'./emacss -N%s -o1 -r%s -o1  -m%s  -g1 -M1E11 -o1 -d%s -o1   -z0.1 -s1  -u%s -l%s -f0  > %s &'
	mass_mean = 0.5739
	lower_mass=0.08
	upper_mass=100


	for line in lines:
		temp = line.replace('\n', '').split()
		r = float(temp[0])
		mass = float(temp[1])
		d = float(temp[2])
		N = int(mass/mass_mean)
		filename_two = './out/RH[%5.2E]_N[%5.2E]_RG[%5.2E].dat' % ( r, N, d)
		args = base % (N, r, mass_mean, d, upper_mass, lower_mass, filename_two)
		run(args)


	path = './out/'
	T_min = 12000
	T = 13000
	idx_RG = 2
	idx_M = 4
	idx_Rh = 5
	base = '%s\t\t%4.2E\t\t%4.2E\t\t%4.2E'
	


	# find all files in <path>
	all_files = [f for f in listdir(path) if isfile(join(path, f))]

	fog = open('out.txt', 'w')
	# extract the info from all files
	for filename in all_files:
	    
		data = np.loadtxt(path + filename)
		q = np.abs(data[:,0]-T)
		idx = np.where(np.min(q)==q)[0]
		temp = data[idx, :][0]
	
		if data[idx, 0] < T_min:
			continue
		else:
			output =  base % (filename, temp[idx_Rh-1], temp[idx_M-1],temp[idx_RG-1] )
	        fog.write("%s \n"% output)
	fog.close()

	return



def Finals():

	input_f=np.genfromtxt('out.txt')
	rh_f=(input_f[:,1])
	M_f=(input_f[:,2])
	RG_f=(input_f[:,3])/1000.

	line_number=input_f.shape[0]/1.

	logmass_f= np.log10(M_f)
	logRG_f=np.log10(RG_f)

	final_rh = np.histogram(rh_f, bins=bin_num, range=(0,35))
	final_mass = np.histogram(logmass_f, bins=bin_num, range=(2,7))
	final_logRG = np.histogram(logRG_f,  bins=bin_num, range=(-3,2.2))


	rh_f_bins = np.column_stack(156* final_rh[0]/line_number)
	logm_f_bins = np.column_stack( 156* final_mass[0]/line_number)
	logRG_f_bins = np.column_stack( 156* final_logRG[0]/line_number)

	return final_rh[0], final_mass[0], final_logRG[0], rh_f, M_f, RG_f, rh_f_bins, logm_f_bins, logRG_f_bins, line_number



def delete_files():

	filesdel = glob.glob('./out/*')
	for f in filesdel:
	    os.remove(f)

	return

