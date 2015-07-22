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
fpidirs=["../SU2_op4_A_Robert/plots/","../SU3_op4_B_Robert/plots/","../SU2_op4_C/plots/","../SU3_op4_D/plots/","../SU2_op4_E/plots/","../SU3_op4_F/plots/","../SU2_op4_G/plots/","../SU2_op4_R1/plots/","../SU3_op4_H/plots/","../SU2_op4_A_Robert/plots/chiral/","../SU3_op4_B_Robert/plots/chiral/","../SU2_op4_C/plots/chiral/","../SU3_op4_D/plots/chiral/","../SU2_op4_E/plots/chiral/","../SU3_op4_F/plots/chiral/","../SU2_op4_G/plots/chiral/","../SU2_op4_R1/plots/chiral/","../SU3_op4_H/plots/chiral/"]

ats=[0.000166761338157,0.000166761338157,0.00016576643127,0.00016576643127,0.00016576643127,0.00016576643127,0.00016576643127,0.00016576643127,0.00016576643127,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]

fpidirs=["../SU2_op4_A_Robert/plots/","../SU3_op4_B_Robert/plots/","../SU2_op4_C/plots/","../SU2_op4_E/plots/","../SU2_op4_G/plots/","../SU2_op4_R1/plots/","../SU2_op4_A_Robert/plots/chiral/","../SU3_op4_B_Robert/plots/chiral/","../SU2_op4_C/plots/chiral/","../SU2_op4_E/plots/chiral/","../SU2_op4_G/plots/chiral/","../SU2_op4_R1/plots/chiral/"]


ats=[0.000166761338157,0.000166761338157,0.000166761338157,0.000166761338157,0.000166761338157,0.000166761338157,1.0,1.0,1.0,1.0,1.0,1.0]

colors=['b','r','g','y','k','magenta','orange','cyan','b','r','g','y','k','magenta','orange','cyan']


Emax=1000

PSmax,PSmin=[],[]

fpidirs=["../SU2_op4_A_Robert/plots/mpi400_chiral/","../SU2_op4_Pelaez_Rioz/plots/chiral/"]
ats=[1.0,1.0]
for i0 in [0,1]:#,11]:#range(len(ats)):
  print ""
  print "*************************************"
  print i0
  at=ats[i0]
  colorf=colors[i0]
  fname=fpidirs[i0]+fname0
  data=loadtxt(fname)
  print "loading data from:",fname
  print colorf
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
  if i0 in [0,2,3,4,5]:
    plt.subplot(211)
  else:
    plt.subplot(212)
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


plt.subplot(211)
output=loadtxt('phase_shifts/phases.txt')
for i0 in range(len(output)):
  [part_type,x,dx,y,dy]=output[i0]
  print part_type,x,dx,y,dy
  if part_type==0.0:
    #if dy>2.0*y:
    #y=y+180
    if dy <20: 
      plt.errorbar(x/ats[0],y,yerr=dy,xerr=dx/ats[0],markersize=8,fmt='o',color='r',mfc='white',mec='r', elinewidth=2, capsize=6, mew=1.4)
                             
plt.subplot(211)
at_hs=0.00017649521531100477
at_hs=0.00016680000000000002
output=loadtxt('phase_shifts/phases_m400.txt')
for i0 in range(len(output)):
  [part_type,x,dx,y,dy]=output[i0]
  print part_type,x,dx,y,dy
  if dy <20:
    plt.errorbar(x/at_hs,y,yerr=dy,xerr=dx/at_hs,markersize=8,fmt='o',color='r',mfc='white',mec='r', elinewidth=2, capsize=6, mew=1.4)



plt.subplot(212)
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
  plt.errorbar(Ecm,ps,yerr=dps,markersize=8,fmt=fmtf,color=colorf,mfc='white',mec=colorf, elinewidth=2, capsize=6, mew=1.4)
 

plt.xlim([Emin,Emax])
plt.yticks(arange(0,200,20),size=12)

plt.yticks(arange(0,200,20),size=12)
plt.ylim([0,180])


plt.subplot(211)
plt.yticks(arange(0,200,20),size=12)
plt.ylim([0,180])
plt.xlim([Emin,Emax])


plt.show()


plt.savefig('phases',dpi=150)
