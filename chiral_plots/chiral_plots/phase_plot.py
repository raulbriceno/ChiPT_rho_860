#!/usr/bin/env python
import matplotlib.pyplot as plt
from numpy import *
import math
from math import pi
import sys

from numpy import interp
####Inputs  
twopi=2.0*pi
hc=197.3269
I=(0+1j)
eps=0.00000000000000001



fname0="plot_output.J1.data"
fpidirs=["../SU3_op4/plots/","../SU3_op4/plots/chiral/","../SU3_op4_fpiChi/plots/chiral/","../SU2_op4/plots/chiral/","../SU2_op4_fpiChi/plots/chiral/"]

ats=[0.000164429429878,1.0,1.0,1.0,1.0]

colors=['orange','b','r','g','y']
Emax=1000

PSmax,PSmin=[],[]

for i0 in range(len(ats)):
  print i0
  at=ats[i0]
  colorf=colors[i0]
  fname=fpidirs[i0]+fname0
  data=loadtxt(fname)
  print "loading data from:",fname

  Ecm,psmax,psmin=[],[],[]


  for i in range(len(data)):
    Ecm.append(data[i][0]/at)
    psmin.append(data[i][1]-data[i][2])
    psmax.append(data[i][1]+data[i][2])

    
  """
  if i0==0:
    psmin0,psmax0,Ecm0=psmin,psmax,Ecm  
  if i0==2:
    psmin1,psmax1,Ecm1=psmin,psmax,Ecm  
  if i0==3:
    psmin2,psmax2,Ecm2=psmin,psmax,Ecm  
  if i0==5:
    psmin3,psmax3,Ecm3=psmin,psmax,Ecm  
  """

  Ecm=array(Ecm)
  psmax=array(psmax)
  psmin=array(psmin)
  if Emax > max(Ecm):
    Emax=max(Ecm)
  Emin=min(Ecm)
  plt.fill_between(Ecm,psmax*180.0/pi, psmin*180.0/pi,facecolor=colorf,alpha='.2')

"""
PSmax,PSmin=ones(len(Ecm0)),ones(len(Ecm0))

for i in range(len(Ecm0)):
  Ecm=Ecm0[i]
  PSmax[i]=max([interp(Ecm,Ecm0,psmax0),interp(Ecm,Ecm1,psmax1),interp(Ecm,Ecm2,psmax2),interp(Ecm,Ecm3,psmax3)])
  PSmin[i]=min([interp(Ecm,Ecm0,psmin0),interp(Ecm,Ecm1,psmin1),interp(Ecm,Ecm2,psmin2),interp(Ecm,Ecm3,psmin3)])
"""  

#plt.fill_between(Ecm0,PSmax*180.0/pi, PSmin*180.0/pi,facecolor='orange',alpha='.6')

mrho=775.26
wrho=147.8
x=mrho-(wrho/2.0)
#plt.axvline(x, color='k')
x=mrho+(wrho/2.0)
#plt.axvline(x, color='k')

colors=['k','g']
fmts=['o','s']
fnames=['rho_exp_Protopopescu.txt','rho_exp_Estabrooks.txt']
for i0 in range(2):
  fname=fnames[i0]
  fmtf=fmts[i0]
  colorf=colors[i0]
  data=loadtxt('./'+fname)
  Ecm,ps,dps=[],[],[]
  for i in range(len(data)):
    Ecm.append(data[i][0]*1000)
    ps.append(data[i][1])
    dps.append(data[i][2])
  plt.errorbar(Ecm,ps,yerr=dps,markersize=8,fmt=fmtf,color=colorf, elinewidth=2, capsize=4, mew=1.4)  

plt.xlim([Emin,Emax])
plt.yticks(arange(0,200,20),size=12)
plt.ylim([0,180])


#plt.ylabel(r'$\delta_1/{\circ}$',size=25)
#plt.xlabel(r'$\rm{E}_{\rm{cm}}$',size=25)
#gcf().subplots_adjust(left=0.15)
#gcf().subplots_adjust(bottom=0.15)
plt.show()



plt.savefig('phases',dpi=150)
