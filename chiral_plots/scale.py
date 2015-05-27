import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
import csv
import numpy as numpy
import time
from mpl_toolkits.mplot3d import *
from matplotlib.pyplot import *
from pylab import *
import urllib
import cmath
import math as math
import random as random
clf #clears plot
import itertools as itertools
import shlex
import pickle
import os
from pylab import figure, show, rand
from matplotlib.patches import Ellipse

I=1j


mrho_HS=0.152
at_hS=0.2951/1672.0

atinv=6101.0
datinv=sqrt(pow(40,2.0)+pow(49,2.0))

at_and=1.0/atinv

mpi=0.06906
dmpi=0.00013
mK = 0.09698
dmK=0.00009
meta = 0.10406
dmeta=0.00041

mpiphys = 139.57
mKphys = 495.7
metaphys = 547.45
fpiphys = 92.4

print ""
print "#####################"
print "Using Andre's scale"
print "at",at_and
print "mpi=",mpi/at_and,'+/-',dmpi/at_and
print "mpi^2=",pow(mpi/(atinv*1000.0),2.0)
print "fpi=",103,"MeV"
print "fpi*at=",103.0*at_and
print "mK=",mK/at_and,'+/-', mK/at_and,'+/-',dmK/at_and
print "meta=",meta/at_and,'+/-', meta/at_and,'+/-',dmeta/at_and
print "renormalization scale=",mrho_HS*at_and/at_hS

"""
print ""
print "physical point values of masses"
print "mpi*at=",mpiphys*at_and
print "2.0*mpi*at=",2.0*mpiphys*at_and
print "fpi*at=",fpiphys*at_and
print "mK*at=",mKphys*at_and
print "meta*at=",metaphys*at_and
print "renormalization scale=",mrho_HS/at_hS
"""





print ""
print "#####################"
print "Using HadSpecs's scale"
print "at",at_hS
print "mpi=",mpi/at_hS,'+/-',dmpi/at_hS
print "mpi^2=",pow(mpi/(at_hS*1000.0),2.0)
print "fpi=",100,"MeV"
print "fpi*at=",100.0*at_hS
print "mK=",mK/at_hS,'+/-',dmK/at_hS
print "meta=",meta/at_hS,'+/-',dmeta/at_hS
print "renormalization scale=",mrho_HS

print ""
print "physical point values of masses"
print "mpi=",mpiphys
print "fpi=",fpiphys
print "mK=",mKphys
print "meta=",metaphys
print "renormalization scale=",mrho_HS/at_hS


"""
to generate a range of plots as a function of the pion mass, we use a simple quadratic fit for the masses
assume mK=mKphys+b*(mpiphys-mpi)^2
this implis b=(mK-mKphys)/(mpiphys-mpi)^2
"""
def masses(mpio,at):
  bfpi=((fpi/at)-fpiphys)/pow(mpiphys-mpi,2.)
  beta=((meta/at)-metaphys)/pow(mpiphys-mpi,2.)
  bK=((mK/at)-mKphys)/pow(mpiphys-mpi,2.)
  
  fpio=fpiphys+bfpi*pow(mpiphys-mpi,2.)
  metao=metaphys+beta*pow(mpiphys-mpi,2.)
  mKo=mKphys+bK*pow(mpiphys-mpi,2.)
  
  return (fpio,metao,mKo)


for mpi in range(mpiphy,mpi/at_hS,50):
  print mpi,masses(mpio,at_hS)


#Using Ref. arXiv:1302.2233 and http://arohatgi.info/WebPlotDigitizer/app/? to determine the decay constant


