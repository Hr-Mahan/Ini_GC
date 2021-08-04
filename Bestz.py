import numpy as np



def best_chi2(chi0,chi1,A1,A2,A3,A4,A5,A6,Arr_in,name_f):
	N=len(Arr_in)
	if chi1 < chi0:
		f1 = open(name_f+ ".txt", 'w')
		f1.write(  "%8.3f"%chi1 +'\t'+ "%8.3f"%A1+'\t'+ "%8.3f"%A2+'\t'+ "%8.3f"%A3+'\t'+ "%8.3f"%A4+'\t'+ "%8.3f"%A5+'\t'+ "%8.3f"%A6+ '\n')
		for i in range(N):
			f1.write(  "%8.3f"%Arr_in[i]+ '\n')
		f1.close()
		NEW_chi2=chi1
	else:
		NEW_chi2=chi0

	return NEW_chi2



def best_chi2_tot(chi0,chi1,A1,A2,A3,A4,A5,A6,Arr_in1,Arr_in2,Arr_in3):
	N=len(Arr_in1)
	if chi1 < chi0:
		f2 = open( 'Best_Results_total.txt', 'w')
		f2.write(  "%8.3f"%chi1 +'\t'+ "%8.3f"%A1+'\t'+ "%8.3f"%A2+'\t'+ "%8.3f"%A3+'\t'+ "%8.3f"%A4+'\t'+ "%8.3f"%A5+'\t'+ "%8.3f"%A6+ '\n')
		for i in range(N):
			f2.write(  "%8.3f"%Arr_in1[i] +'\t'+'\t'+ "%8.3f"%Arr_in2[i]+'\t'+'\t'+ "%8.3f"%Arr_in3[i] + '\n')
		f2.close()
		NEW_chi2=chi1
	else:
		NEW_chi2=chi0

	return NEW_chi2
