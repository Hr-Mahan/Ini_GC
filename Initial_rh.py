import numpy as np
import globalz as glb
import random


NCluster=glb.NCluster
rh=np.zeros(NCluster)


def ini_rh(rhc,sigma):

	for i in range(NCluster):

		rh[i] = -1.0
		while (rh[i] <= 0.0):
			rh[i] = np.random.normal(rhc, sigma, 1)
		rh[i] = rh[i] 	

	random.shuffle(rh)

	return rh
