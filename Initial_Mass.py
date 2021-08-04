import numpy as np
from scipy.integrate import quad
import random
import globalz as glb




NCluster=glb.NCluster
bin_num=glb.bin_num
m_bin=glb.m_bin
mass=np.zeros(NCluster)




def integrand(m,Alpha,Ms):
	return pow(m,-1.0*Alpha)*pow(2.7182818,-1.0*(m/Ms))

def ini_m(Alpha,Ms):

	Ms=10.0**Ms

	q1=0
	Wm_tot= quad(integrand, pow(10.0,3.5), pow(10.0,7), args=(Alpha,Ms))

	schechter_range = m_bin
	q1=[None] * (len(schechter_range)-1)
	j=0

	for i in range(len(schechter_range)-1):
		LL=pow(10,schechter_range[i])
		UL=pow(10,schechter_range[i+1])
		Wm = quad(integrand, LL, UL, args=(Alpha,Ms))
		Nm=NCluster*(Wm[0]/Wm_tot[0])	
		q1[i]=int(Nm)

		for k in range(q1[i]):
			mass[j] = random.uniform(LL,UL)
			j=j+1

	for i in range(NCluster):
		if mass[i] <= 0: mass[i]=random.uniform(pow(10.0,3.5), pow(10.0,7))

	random.shuffle(mass)



	return mass
