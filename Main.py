import numpy as np
from scipy.integrate import quad
import globalz as glb
import Initial_Mass as m0
import Initial_rh as rh0
import Initial_RG as rg0
import Plotz
import Bestz
import Emacss_Evolution
from datetime import datetime

start_time = datetime.now()


NCluster=glb.NCluster
chi2_m0=glb.chi2_m0
chi2_rh0=glb.chi2_rh0
chi2_RG0=glb.chi2_RG0
chi2_tot0=chi2_m0+chi2_rh0+chi2_RG0

data0 = np.loadtxt("Obsevations.txt")



for i1 in range(1,2):
	for i2 in range(1,2):
		I_mass= m0.ini_m(glb.ALPHA0+(i1/100.0),glb.MS0+(2.0*i2/10.0))
		for i3 in range(1,2):
			for i4 in range(1,2):
				I_rh=rh0.ini_rh(glb.RHC0+i3,glb.SIGMA0+(5.0*i4/10.0))
				for i5 in range(1,2):
					for i6 in range(1,2):
						I_RG=rg0.ini_rg(glb.BETA0+(5.0*i5/10.0),glb.RS0+(2.0*i6/10.0))
						f0 = open('Initial.txt', 'w')
						for i in range(NCluster):
							f0.write(  "%8.3f"%rh0.rh[i] +'\t'+'\t'+ "%8.3f"%m0.mass[i]+'\t'+'\t'+ "%8.3f"%rg0.rg[i] + '\n')
						f0.close()
						A1=glb.ALPHA0+(i1/100.0)
						A2=glb.MS0+(2.0*i2/10.0)
						A3=glb.RHC0+i3
						A4=glb.SIGMA0+(5.0*i4/10.0)
						A5=glb.BETA0+(5.0*i5/10.0)
						A6=glb.RS0+(2.0*i6/10.0)
						evolve=Emacss_Evolution.Emacss()
						finals=Emacss_Evolution.Finals()
						M_fnl=finals[4]
						weights_p = [156.0/finals[-1]] * len(finals[4])	
						rh_fnl=finals[3]
						RG_fnl=finals[5] 	
#						CHI2_m=Plotz.Histo_plot(np.log10(data0[:,0]),np.log10(M_fnl),2,7,weights_p,"Log_{30}\ m_{i}\ [M_{\odot}]","mass")
						CHI2_m=Plotz.Histo_CHI2(np.log10(data0[:,0]),np.log10(M_fnl),2,7,weights_p)
						CHI2_rh=Plotz.Histo_CHI2(data0[:,2],rh_fnl,0,35,weights_p)
						CHI2_RG=Plotz.Histo_CHI2(np.log10(data0[:,1]),np.log10(RG_fnl),-1,2.2,weights_p)
						CHI2_tot=CHI2_m+CHI2_rh+CHI2_RG
						BEST_m=Bestz.best_chi2(chi2_m0,CHI2_m,A1,A2,A3,A4,A5,A6,M_fnl,"Best_M_Results")
						chi2_m0=BEST_m
						BEST_rh=Bestz.best_chi2(chi2_rh0,CHI2_rh,A1,A2,A3,A4,A5,A6,rh_fnl,"Best_rh_Results")
						chi2_rh0=BEST_rh
						BEST_RG=Bestz.best_chi2(chi2_RG0,CHI2_RG,A1,A2,A3,A4,A5,A6,RG_fnl,"Best_RG_Results")
						chi2_RG0=BEST_RG
						BEST_TOTAL=Bestz.best_chi2_tot(chi2_tot0,CHI2_tot,A1,A2,A3,A4,A5,A6,M_fnl,rh_fnl,RG_fnl)
						chi2_tot0=BEST_TOTAL

						DEL_OUT=Emacss_Evolution.delete_files()
						

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
