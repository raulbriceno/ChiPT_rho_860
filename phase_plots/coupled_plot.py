import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
import csv
import shutil 
import numpy as numpy
import time
import numpy.linalg as la
from mpl_toolkits.mplot3d import *
from matplotlib.pyplot import * 
from pylab import *
import urllib
import cmath
import math as math 
from random import *
import itertools as itertools
import shlex
import os 
from pylab import figure, show, rand
from matplotlib.patches import Ellipse
import os.path
from heapq import nsmallest


####Inputs  
twopi=2.0*pi
hc=197.3269
I=(0+1j)
eps=0.00000000000000001

mpi=0.03928
mK=0.08344 
aniso=3.4534 
Loas=32
L=Loas*aniso

Ecm=arange(0.07,0.24,.0001)
 


output=loadtxt('../coupled/plots/plot_output.J1.data')

ps_pipi_max,ps_pipi_min=[],[]
ps_kkbar_max,ps_kkbar_min=[],[]
eta_max,eta_min=[],[]
Ecms=[]
for i0 in range(len(output)):
    [Ecm,ps_pipi,dps_pipi,ps_kkbar,dps_kkbar,eta,deta]=output[i0]

    ps_pipi_max.append(ps_pipi+dps_pipi)
    ps_pipi_min.append(ps_pipi-dps_pipi)
    ps_kkbar_max.append(ps_kkbar+dps_kkbar)
    ps_kkbar_min.append(ps_kkbar-dps_kkbar)
    eta_max.append(eta+deta)
    eta_min.append(eta-deta)
    Ecms.append(Ecm)

Ecms=array(Ecms)
ps_pipi_max,ps_pipi_min=array(ps_pipi_max),array(ps_pipi_min)
ps_kkbar_max,ps_kkbar_min=array(ps_kkbar_max),array(ps_kkbar_min)
eta_max,eta_min=array(eta_max),array(eta_min)

subplot(2,1,1)


plt.fill_between(Ecms/mpi,ps_pipi_max*180.0/pi, ps_pipi_min*180.0/pi,facecolor='r',alpha='.5')
plt.fill_between(Ecms/mpi,ps_kkbar_max*180.0/pi, ps_kkbar_min*180.0/pi,facecolor='b',alpha='.5')
axhline(y=0,color='k',hold=None)


output=loadtxt('../rho_860_fit/phases.txt')
for i0 in range(len(output)):
  [part_type,x,dx,y,dy]=output[i0]
  print part_type,x,dx,y,dy
  if part_type==0.0:
    if dy>2.0*y:
      y=y+180
    if x<2.0*mK/mpi:
      plt.errorbar(x,y,yerr=dy,xerr=dx,markersize=8,fmt='o',color='r',mfc='white',mec='r', elinewidth=2, capsize=4, mew=1.4)
    else:
      plt.errorbar(x,y,yerr=dy,xerr=dx,markersize=8,fmt='d',color='0.75',mfc='white',mec='0.75', elinewidth=2, capsize=4, mew=1.4,alpha=1)
  if part_type==1.0:
    if x<2.0*mK/mpi:
      plt.errorbar(x,y,yerr=dy,xerr=dx,markersize=8,fmt='s',color='b',mfc='white',mec='b', elinewidth=2, capsize=4, mew=1.4)
    else:
      plt.errorbar(x,y,yerr=dy,xerr=dx,markersize=8,fmt='d',color='0.75',mfc='white',mec='0.75', elinewidth=2, capsize=4, mew=1.4,alpha=1)

plt.errorbar(2.0*mK/mpi,0,yerr=0,xerr=0,markersize=8,fmt='o',color='k',mfc='white',mec='k', elinewidth=2, capsize=4, mew=1.4)

plt.xlim([2.0,max(Ecms)/mpi])
#plt.ylabel(r'$\delta_1/{\circ}$',size=25)
plt.ylim([min(ps_kkbar_min)*180.0/pi-10,max(ps_pipi_max*180.0/pi)+10])


subplot(3,1,3)

plt.fill_between(Ecms/mpi,eta_max, eta_min,facecolor='orange',alpha='.5')

axhline(y=1,color='k',hold=None)

plt.errorbar(2.0*mK/mpi,1,yerr=0,xerr=0,markersize=8,fmt='o',color='k',mfc='white',mec='k', elinewidth=2, capsize=4, mew=1.4)

#plt.ylabel(r'$\eta$',size=25)
#plt.xlabel(r'$\rm{E}_{\rm{cm}}$',size=25)
plt.ylim([.8,1.05])
plt.xlim([2.0,max(Ecms)/mpi])
"""
plt.xlim([Emin,Emax])
plt.yticks(arange(0,200,20),size=12)
plt.ylim([0,180])
"""

#gcf().subplots_adjust(left=0.15)
#gcf().subplots_adjust(bottom=0.15)
plt.show()



plt.savefig('coupled_phases_eta',dpi=150)

