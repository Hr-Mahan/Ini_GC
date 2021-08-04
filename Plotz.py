import numpy as np
import matplotlib.pyplot as plt
import globalz as glb
import Emacss_Evolution


NCluster=glb.NCluster
bin_num=glb.bin_num
m_bin=glb.m_bin
r_bin=glb.r_bin


heights=2.0*9.5/2
widths=2.0*6.8/2.0
titlefntsize=28
xfntsize=21
yfntsize=21
xpad=2
ypad=1.4
ticfntsize=17
lgndfntsize=10
lgndloc=2
mew1=0
ms1=0
lw1=3

fig, ax1 = plt.subplots()                   
fig.set_size_inches(heights, widths)




#def Histo_plot(Arr_obs,Arr_final,Ra,Rb,weights0,xlabel,name_p):
def Histo_CHI2(Arr_obs,Arr_final,Ra,Rb,weights0):

	fd=2
	chi2= 0.0

#	entries, edges, _ = plt.hist(Arr_obs,bins=bin_num,range=[Ra,Rb], histtype="stepfilled", edgecolor='g', facecolor='palegreen', label='Observation') 
#	bin_centers = 0.5 * (edges[:-1] + edges[1:])
#	plt.errorbar(bin_centers, entries, yerr=np.sqrt(entries), fmt='r.')
#	sigma_tmp = np.sqrt(entries)
#	HB_tmp=entries

#	entriesp, edgesp, _ = plt.hist(Arr_final,bins=bin_num,weights=weights0,range=[Ra,Rb],histtype="stepfilled", hatch='/', edgecolor='b', facecolor='none' , label='Simulation')
#	expt_tmp=entriesp


	entries, bin_edges = np.histogram(Arr_obs,bins=bin_num,range=[Ra,Rb]) 
	sigma_tmp = np.sqrt(entries)
	HB_tmp=entries

	entriesp, bin_edges = np.histogram(Arr_final,bins=bin_num,weights=weights0,range=[Ra,Rb])
	expt_tmp=entriesp


	for i in range(0,bin_num):
		if sigma_tmp[i] == 0.0: sigma_tmp[i]=1.0


	for i in range(0,bin_num):
	    chi2=chi2+((HB_tmp[i]-expt_tmp[i] )**2)/(sigma_tmp[i]**2)
	chi2=chi2/(bin_num-fd-1)

#	plt.xlabel(r'$\mathregular{str(xlabel)}$',fontsize = xfntsize, labelpad=xpad)
#	plt.ylabel(r'$\mathregular{Number}$',fontsize = yfntsize, labelpad=ypad)

#	plt.xticks(fontsize = ticfntsize)
#	plt.yticks(fontsize = ticfntsize)
#	plt.legend(frameon=False,loc=lgndloc, fontsize = lgndfntsize)

#	plt.savefig(name_p+ ".eps")

#	plt.clf()

	return chi2
