import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
import csv
import shutil 
import numpy as numpy
import time
import numpy.linalg as la
from mpl_toolkits.mplot3d import *
import scipy as sp
from scipy.interpolate import interp1d
from matplotlib.pyplot import * 
from pylab import *
import urllib
import cmath
import math as math 
from random import *
from scipy import optimize 
clf #clears plot
import itertools as itertools
import shlex
import pickle 
import os 
from scipy.integrate import quad
import scipy.special as sps
from pylab import figure, show, rand
from matplotlib.patches import Ellipse
import os.path
from heapq import nsmallest


import Functs as Functs
Functs=reload(Functs)


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
 
"""
********************
jack knife code
********************
"""
def jack(X):
	nn=len(X)
	JACK=zeros(nn)
	for kk in range(nn):
		JACK[kk]=(sum(X)-X[kk])/float(nn-1.)
	return JACK
 

###standard deviation and convariance matrix
	
def jack_sig(X):
	nn=float(len(X))
	ave=mean(X)
	return pow((((nn-1.)/nn)*sum((X-ave)**2.)),.5)

def inflate(X):
	NN=len(X)
	amp=float(sqrt(NN-1.0))
	mx=mean(X)
	return mx+((X-mx)*amp)


def deflate(X):
	NN=len(X)
	amp=1.0/float(sqrt(NN-1.0))
	mx=mean(X)
	return mx+((X-mx)*amp)


def loadjack(files):
	with open(files, 'r') as fin:
  		data = fin.read().splitlines(True)


	NG=int(data[0].split()[0])
	out=ones(NG)
	for ng in range(NG):
		out[ng]=data[ng+1].split()[1]
	return inflate(jack(out))



#########################################
####################Inputs###############
#########################################


def Couts(part_type,irrep,dname,Loas):
	"part_type= pipi or KKbar"
	filename="couts/"+part_type+"_d"+dname+"_"+irrep+"_L."+str(int(Loas))+".txt"
	cout=loadtxt(filename)
	
	return cout
	 
	 

"""
we need smart interpolating functions for the 
phase shift, QCs and LL factors...
"""
def S(Z):
	return (Z+I)/(Z-I)
	
def Z(S):
	return I*(S+1.0)/(S-1.0)
	
def clever_Z_interp(Eout,Vinp):
	S_VinpR,S_VinpI=real(S(Vinp)),imag(S(Vinp))
	fS_VinpR_tmp=interp1d(Ecm,S_VinpR)
	fS_VinpI_tmp=interp1d(Ecm,S_VinpI)
 

	return real(Z(fS_VinpR_tmp(Eout)+I*fS_VinpI_tmp(Eout)))					
 

def fLuscher_pcotdelta(Eout,part_type,irrep,dname,Loas): 
  EEcm=pow(Eout,2.0)
  
  if part_type=="pipi":
    qq=(EEcm/4.0)-pow(mpi,2.0)
    qout=sqrt(qq)	
  
  if part_type=="KKbar":
    qq=(EEcm/4.0)-pow(mK,2.0)
    qout=sqrt(qq)
  
  cout=Couts(part_type,irrep,dname,Loas)
  
  fcout=clever_Z_interp(Eout,cout)
  
  
  cotd=(4.0*pi*fcout)/qout

  delta=arctan(1.0/cotd)*180.0/pi
  
  for i0 in range(len(delta)):
      if mean(delta[i0])<0 and part_type=="pipi":
        delta[i0]=delta[i0]+180.0
  
  return delta
 
 
filename='../../spec_final_elastic.list'


with open(filename, 'r') as fin:
  	states = fin.read().splitlines(True)


print ""
print "**************************************"
print "pipi"

output=[]
for i0 in range(len(states)): 
  dname,irrep,L_label,jack_energy_file=states[i0].split()
  Ei=loadjack(jack_energy_file)
  
  d=array([float(dname[0]),float(dname[1]),float(dname[2])])
  print ""
  print "Loas",Loas
  P=d*2.0*pi/(Loas*aniso)
  PP=dot(P,P)
 
  print dname,d
  print "before",mean(Ei), std(Ei),dot(P,P)
  print mean(sqrt(pow(Ei,2.0)-PP))
  Eout=sqrt(pow(Ei,2.0)-PP)
  ps=fLuscher_pcotdelta(Eout,"pipi",irrep,dname,Loas) 
  print "after",mean(Eout), std(Eout)
  x,dx=mean(Eout),std(Eout)
  
  y,dy=mean(ps),std(ps)  
  print irrep,x,dx,y,dy 	
  #if irrep=="B1" and dname=="110": 
  output.append([0,x,dx,y,dy])
  """
  ps=Functs.Luscher_ps_no_interp_vec(Eout,mpi,irrep,d,L)
  
  errorbar(x,y,yerr=dy,xerr=dx,markersize=8,fmt='d',color='r',mfc='white',mec='r', elinewidth=2, capsize=4, mew=1.4)	
  """
	 
savetxt('phases.txt',array(output))

