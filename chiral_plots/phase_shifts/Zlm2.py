from scipy import *
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

####Inputs  
twopi=2.0*pi
hc=197.3269
I=(0+1j)
eps=0.00000000000000001

 

			
###############################################################
##########################Create sums###########################
###############################################################
def S2(x,N):
	NN=N**2.0
	XX1=[]
	XX2=[]
	XX3=[]
	X1=range(-N,N+1) 
	for x1 in X1:
		for x2 in X1:
			for x3 in X1:
				xx1=x1**2.0
				xx2=x2**2.0
				xx3=x3**2.0
				if (xx1+xx2+xx3)<=NN:
					XX1.append(x1)
					XX2.append(x2)
					XX3.append(x3)
	
	(XX1,XX2,XX3)=(array(XX1),array(XX2),array(XX3))
	print XX1
	print XX2
	print XX3
	lam=str(N)  
	return (array(XX1),array(XX2),array(XX3))	
 
def S3(x,N):
	NN=N**2
	XX1=[]
	XX2=[]
	XX3=[]
	X1=range(-N,N+1) 
	for x1 in X1:
		for x2 in X1:
			for x3 in X1:
				xx1=x1**2.0
				xx2=x2**2.0
				xx3=x3**2.0
				if (xx1+xx2+xx3)<=NN:
					if (xx1+xx2+xx3) not in [0]:
						XX1.append(x1)
						XX2.append(x2)
						XX3.append(x3)
	
	(XX1,XX2,XX3)=(array(XX1),array(XX2),array(XX3))
	print XX1
	print XX2
	print XX3
	lam=str(N) 

	return (array(XX1),array(XX2),array(XX3))	





 
###################################################################
####################Inverse of Scattering Amplitudes###############
###################################################################

 
def ScatA(Ecm,ere):
	if ere=='cubA1':  
		mat0=[[1.0]]
		T2=fixT(T2rJ0f(Ecm),mat0)
		T4=fixT(T4rJ0f(Ecm),mat0)
	return (T2,T4)
	
#############################################################################
#############################################################################
####################### Spherical Harmonics #################################
#############################################################################
#############################################################################
def Ylmr(x,y,z,l,m):
	#this prints out Ylm*r^l
	r=sqrt(pow(x,2.0)+pow(y,2.0)+pow(z,2.0))+eps
	if l==0:
		if m==0:
			rYlm=sqrt(1.0/(4.0*pi))
	elif l==1:
		if m==-1:
			rYlm=(1.0/2.0)*sqrt(3.0/(2.0*pi))*(x-I*y) 
		elif m==0:
			rYlm=(1.0/2.0)*sqrt(3.0/(pi))*(z) 
		elif m==1:
			rYlm=-(1.0/2.0)*sqrt(3.0/(2.0*pi))*(x+I*y) 
	elif l==2:
		if m==-2:
			rYlm=(1.0/4.0)*sqrt(15.0/(2.0*pi))*pow(x-I*y,2.0) 
		elif m==-1:
			rYlm=(1.0/2.0)*sqrt(15.0/(2.0*pi))*z*(x-I*y) 
		elif m==0:	
			rYlm=(1.0/4.0)*sqrt(5.0/pi)*(2.0*pow(z,2.0)-pow(x,2.0)-pow(y,2.0)) 
		elif m==1:
			rYlm=(-1.0/2.0)*sqrt(15.0/(2.0*pi))*z*(x+I*y) 
		elif m==2:
			rYlm=(1.0/4.0)*sqrt(15.0/(2.0*pi))*pow(x+I*y,2.0) 
	elif l==3:
		if m==-3:
			rYlm=sqrt(35.0/pi)*(1.0/8.0)*pow(x-I*y,3.0) 
		elif m==-2:
			rYlm=sqrt(105.0/(2.0*pi))*(1.0/4.0)*pow(x-I*y,2.0)*z
		elif m==-1:
			rYlm=sqrt(21.0/pi)*(1.0/8.0)*pow(x-I*y,1.0)*(4.0*pow(z,2.0)-pow(x,2.0)-pow(y,2.0))
		elif m==0:
			rYlm=sqrt(7.0/pi)*(1.0/4.0)*z*(2.0*pow(z,2.0)-3.0*pow(x,2.0)-3.0*pow(y,2.0))
		elif m==1:
			rYlm=sqrt(21.0/pi)*(-1.0/8.0)*pow(x+I*y,1.0)*(4.0*pow(z,2.0)-pow(x,2.0)-pow(y,2.0))
		elif m==2:
			rYlm=sqrt(105.0/(2.0*pi))*(1.0/4.0)*pow(x+I*y,2.0)*z
		elif m==3:
			rYlm=sqrt(35.0/pi)*(-1.0/8.0)*pow(x+I*y,3.0) 
		
			
		
	elif l==4:
		if m==-4:	
			rYlm=sqrt(35.0/(2*pi))*(3.0/16.0)*pow(x-I*y,4.0)	
		elif m==-3:	
			rYlm=sqrt(35.0/pi)*(3.0/8.0)*pow(x-I*y,3.0)*z
		elif m==-2:	
			rYlm=sqrt(5.0/(2*pi))*(3.0/8.0)*pow(x-I*y,2.0)*(7*pow(z,2.0)-pow(r,2.0))
		elif m==-1:	
			rYlm=sqrt(5.0/pi)*(3.0/8.0)*pow(x-I*y,1.0)*z*(7*pow(z,2.0)-3.0*pow(r,2.0))
		elif m==0:	
			rYlm=sqrt(1.0/pi)*(3.0/16.0)*(35.0*pow(z,4.0)-30.0*pow(z,2.0)*pow(r,2.0)+3.0*pow(r,4.0))
		elif m==1:	
			rYlm=sqrt(5.0/pi)*(-3.0/8.0)*pow(x+I*y,1.0)*z*(7*pow(z,2.0)-3.0*pow(r,2.0))
		
		elif m==2:	
			rYlm=sqrt(5.0/(2*pi))*(3.0/8.0)*pow(x+I*y,2.0)*(7*(z**2.0)-(r**2))

		elif m==3:	
			rYlm=sqrt(35.0/pi)*(-3.0/8.0)*pow(x+I*y,3.0)*z
		elif m==4:	
			rYlm=sqrt(35.0/(2*pi))*(3.0/16.0)*pow(x+I*y,4.0)
				
	return rYlm


##########################################################################################
##########################################################################################
####################### Zeta Functions #################################
##########################################################################################
##########################################################################################

 

lam=10
(x1,x2,x3)=S2(0,lam)
(x01,x02,x03)=S3(0,10)
def Zboost(x,d,l,m,alpha,gg): 
	dd=float(dot(d,d))
	#From references http://arxiv.org/pdf/1202.2145v3.pdf
	#Vector of catersian coordinates
	N=(x1,x2,x3)

	if dot(d,d) not in [0]:
		amppar=(N[0]*d[0]+N[1]*d[1]+N[2]*d[2])/dd
	else:
		amppar=0
	Npar1=amppar*d[0]
	Npar2=amppar*d[1]
	Npar3=amppar*d[2]
	Nper1=N[0]-Npar1
	Nper2=N[1]-Npar2
	Nper3=N[2]-Npar3
	rr=((pow(Npar1-(d[0]*alpha),2.0)+pow(Npar2-(d[1]*alpha),2.0)+pow(Npar3-(d[2]*alpha),2.0))/pow(gg,2.0))+pow(Nper1,2.0)+pow(Nper2,2.0)+pow(Nper3,2.0)-x 
	#print rr
	#rr=rr+pow(Nper1,2.0)+pow(Nper2,2.0)+pow(Nper3,2.0)-x 

	#define spherical coordinate 
	x0=((Npar1-(d[0]*alpha))/gg)+Nper1
	y0=((Npar2-(d[1]*alpha))/gg)+Nper2
	z0=((Npar3-(d[2]*alpha))/gg)+Nper3

	###Define spherical harmonic 
	rylm=Ylmr(x0,y0,z0,l,m)

	##First term
	Lam=1.0
	c1= sum(exp(-Lam*rr)*rylm/rr) 

	#Second term
	def integrand1(t):return 2.0*x*exp(t*x)/sqrt(t)
	y=gg*(1.0/sqrt(4.0*pi))*(pow(pi,3.0/2.0))
	if l==0:
		c2=y*(quad(integrand1, 0, Lam)[0]-2.0*exp(Lam*x)/sqrt(Lam))
	else:
		c2=0 
	#third term
	
	wd=(x01*d[0])+(x02*d[1])+(x03*d[2])

	N=[x01,x02,x03]    
	if dot(d,d) not in [0]:
		amppar=(N[0]*d[0]+N[1]*d[1]+N[2]*d[2])/dd
	else:
		amppar=0
	Npar1=amppar*d[0]
	Npar2=amppar*d[1]
	Npar3=amppar*d[2]
	Nper1=N[0]-Npar1
	Nper2=N[1]-Npar2
	Nper3=N[2]-Npar3 
	ww=(pow(Npar1*gg,2.0)+pow(Npar2*gg,2.0)+pow(Npar3*gg,2.0))+pow(Nper1,2.0)+pow(Nper2,2.0)+pow(Nper3,2.0)


	#define spherical coordinate 
	x0=(Npar1*gg)+Nper1
	y0=(Npar2*gg)+Nper2
	z0=(Npar3*gg)+Nper3
	###Define spherical harmonic 
	rylm=Ylmr(x0,y0,z0,l,m)

	#print 'rylm',rylm
	def integrand2(t):
		a1=gg*exp(I*2.0*alpha*pi*wd)*pow(I,l)
		a2=rylm
		a3=pow((pi/t),(3.0/2.0)+l)
		a4=exp(t*x)*exp(-(pow(pi,2.0))*ww/t)
		return real(sum(a1*a2*a3*a4))
	c3r=quad(integrand2, 0, Lam)[0]
	def integrand2(t):
		a1=gg*exp(I*2.0*alpha*pi*wd)*pow(I,l)
		a2=rylm
		a3=pow((pi/t),(3.0/2.0)+l)
		a4=exp(t*x)*exp(-(pow(pi,2.0))*ww/t)
		return imag(sum(a1*a2*a3*a4))
	c3i=quad(integrand2, 0, Lam)[0]
	c3=c3r+c3i*I
	 
	C=c1+c2+c3
	#print c1,c2,c3
	#return (c1,c2,c3,C)
	return C

def ZVect(xRange,d,l,m,alpha,Gs):
	ZoutR=zeros(len(xRange))
	ZoutI=zeros(len(xRange))
	clmoutR=zeros(len(xRange))
	clmoutI=zeros(len(xRange))
	
	for i in range(len(xRange)):
		x=xRange[i]
		gg=Gs[i]
		Z0=Zboost(x,d,l,m,alpha,gg)
		ZoutR[i]=real(Z0)
		ZoutI[i]=imag(Z0)
		clmoutR[i]=real(Z0)
		clmoutI[i]=imag(Z0)
		amp=sqrt(4.0*pi)*pow(twopi/L,l-2)/(gg*pow(L,3.0))
		clmoutR[i]=amp*ZoutR[i]
		clmoutI[i]=amp*ZoutI[i]
	return (ZoutR,ZoutI,clmoutR,clmoutI)


def gamma(Ecm,d,L):
	P=d*twopi/(L)
	PP=dot(P,P)
	EE=pow(Ecm,2.0)
	#print PP,sqrt(EE+PP),Ecm
	return sqrt(EE+PP)/Ecm
	
