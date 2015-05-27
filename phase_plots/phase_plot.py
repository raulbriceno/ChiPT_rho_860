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
 


output=loadtxt('../SU3_op4/plots/plot_output.J1.data')

ps_pipi_max,ps_pipi_min=[],[]
Ecms=[]
for i0 in range(len(output)):
    [Ecm,ps_pipi,dps_pipi]=output[i0]

    ps_pipi_max.append(ps_pipi+dps_pipi)
    ps_pipi_min.append(ps_pipi-dps_pipi)
    Ecms.append(Ecm)

Ecms=array(Ecms)
ps_pipi_max,ps_pipi_min=array(ps_pipi_max),array(ps_pipi_min)

plt.fill_between(Ecms/mpi,ps_pipi_max*180.0/pi, ps_pipi_min*180.0/pi,facecolor='r',alpha='.5')

axhline(y=0,color='k',hold=None)

plt.subplot(211)
output=loadtxt('phase_shifts/phases.txt')
for i0 in range(len(output)):
  [part_type,x,dx,y,dy]=output[i0]
  print part_type,x,dx,y,dy
  if part_type==0.0:
    if dy>2.0*y:
      y=y+180
    if x<2.0*mK/mpi:
      plt.errorbar(x,y,yerr=dy,xerr=dx,markersize=8,fmt='o',color='r',mfc='white',mec='r', elinewidth=2, capsize=4, mew=1.4)
   



plt.subplot(212)
output=loadtxt('../../rho_860/rho_860_fit/phases.txt')
for i0 in range(len(output)):
  [part_type,x,dx,y,dy]=output[i0]
  print part_type,x,dx,y,dy
  if part_type==0.0:
    if dy>2.0*y:
      y=y+180
    if x<2.0*mK/mpi:
      plt.errorbar(x,y,yerr=dy,xerr=dx,markersize=8,fmt='o',color='r',mfc='white',mec='r', elinewidth=2, capsize=4, mew=1.4)
   
plt.xlim([2.0,2.0*mK/mpi])
#plt.ylabel(r'$\delta_1/{\circ}$',size=25)
plt.ylim([0,max(ps_pipi_max*180.0/pi)+10])

"""
plt.xlim([Emin,Emax])
plt.yticks(arange(0,200,20),size=12)
plt.ylim([0,180])
"""

#gcf().subplots_adjust(left=0.15)
#gcf().subplots_adjust(bottom=0.15)
plt.show()



plt.savefig('rel_BW_phase',dpi=150)

