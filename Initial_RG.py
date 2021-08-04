import numpy as np
import globalz as glb
from scipy.integrate import quad
import random

NCluster=glb.NCluster
rg=np.zeros(NCluster)
r_bin=glb.r_bin

def integrand(Rg1,Beta,Rs):
	return (4*3.141578*(Rg1**2.0))/(1+((Rg1/Rs)**Beta))

def ini_rg(Beta,Rs):

	WRg_tot= quad(integrand, 0.0, 100, args=(Beta,Rs))

	radii_range = r_bin

	qr1=[None] * (len(radii_range)-1)
	j=0
	for i in range(len(radii_range)-1):
		LLr=radii_range[i]
		ULr=radii_range[i+1]
		Wr = quad(integrand, LLr, ULr, args=(Beta,Rs))
		Nr=NCluster*(Wr[0]/WRg_tot[0])	
		qr1[i]=int(Nr)

		for k in range(int(round(Nr))):
			rg[j] = random.uniform(LLr,ULr)
			j=j+1
		
	for i in range(NCluster):
		if rg[i] <= 0: rg[i]=random.uniform(0.0, 100)
	#	rg[i]=rg[i]*1000.0    

	random.shuffle(rg)

	return rg
