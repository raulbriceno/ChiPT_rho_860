#!/usr/bin/env python
import matplotlib.pyplot as plt
from numpy import *
import math
from math import pi
import sys

####Inputs  
twopi=2.0*pi
hc=197.3269
I=(0+1j)
eps=0.00000000000000001

at=0.000163907556138 

fname=sys.argv[1]

data=loadtxt(fname)

Ecm,psmax,psmin=[],[],[]


for i in range(len(data)):
  Ecm.append(data[i][0]/at)
  psmin.append(data[i][1]-data[i][2])
  psmax.append(data[i][1]+data[i][2])

Ecm=array(Ecm)
psmax=array(psmax)
psmin=array(psmin)
 
#plt.plot(Ecm,psmax*180.0/pi,color='b')
#plt.plot(Ecm,psmin*180.0/pi,color='b')
plt.fill_between(Ecm,psmax*180.0/pi, psmin*180.0/pi,facecolor='orange',alpha='.5')

mrho=775.26
wrho=147.8
x=mrho-(wrho/2.0)
#plt.axvline(x, color='k')
x=mrho+(wrho/2.0)
#plt.axvline(x, color='k')

Emin=min(Ecm)
Emax=max(Ecm)
mpi = 139.57

data=loadtxt('/u/home/rbriceno/analysis/ChiPT_rho/rho_exp.txt')

Ecm,ps,dps=[],[],[]


for i in range(len(data)):
    Ecm.append(data[i][0]*1000)
    ps.append(data[i][1])
    dps.append(data[i][2])


plt.errorbar(Ecm,ps,yerr=dps,markersize=8,fmt='o',color='k', elinewidth=2, capsize=4, mew=1.4)  

plt.xlim([Emin,Emax])
plt.yticks(arange(0,200,20),size=12)
plt.ylim([0,180])


#plt.ylabel(r'$\delta_1/{\circ}$',size=25)
#plt.xlabel(r'$\rm{E}_{\rm{cm}}$',size=25)
#gcf().subplots_adjust(left=0.15)
#gcf().subplots_adjust(bottom=0.15)
plt.show()



#plt.savefig('figures/phases',dpi=150)
