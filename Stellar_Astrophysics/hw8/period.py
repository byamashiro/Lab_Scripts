import datetime
import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import sigma_clip
from numpy import mean
from astropy.io import fits as fits
from astropy import units as u
from astropy.coordinates import SkyCoord
from matplotlib.patches import Rectangle
from astropy.coordinates import Angle
from scipy import ndimage
from astropy import units as u
import ccdproc
import pyfits
from matplotlib.colors import LogNorm
from astropy.stats import LombScargle
import astropy.units as u
from gatspy import periodic
'''
JD = []
V = []

JD = np.genfromtxt("rv2346.dat", usecols = 0)
V = np.genfromtxt("rv2346.dat", usecols = 1)

#period = np.arange(15, 17, 0.1)
#period = np.arange(16, 17, 0.0000000000001)

for i in period:
	plt.clf()
	phase_frac = (JD - JD[0])%i/i
	plt.plot(phase_frac, V, "o")
	plt.xlabel('Phase Fraction', fontname="Arial", fontsize = 16)
	plt.ylabel('Radial Velocity [km/s]', fontname="Arial", fontsize = 16)
	plt.title("Period: "+str(i)+" [days]")
	plt.show()

plt.clf()
model = periodic.LombScargleFast(fit_period=True)
model.optimizer.period_range = (3.0, 40.0)
model.fit(JD, V, None)
print(model.best_period)
'''

cepv5 = np.genfromtxt('hw8data/cepv5.dat',skip_header=3)
cepv7 = np.genfromtxt('hw8data/cepv7.dat',skip_header=3)
cepv13 = np.genfromtxt('hw8data/cepv13.dat',skip_header=3)
cepv16 = np.genfromtxt('hw8data/cepv16.dat',skip_header=3)
cepv17 = np.genfromtxt('hw8data/cepv17.dat',skip_header=3)
cepv19 = np.genfromtxt('hw8data/cepv19.dat',skip_header=3)
cepv20 = np.genfromtxt('hw8data/cepv20.dat',skip_header=3)
cepv22 = np.genfromtxt('hw8data/cepv22.dat',skip_header=3)
cepv25 = np.genfromtxt('hw8data/cepv25.dat',skip_header=3)
cepv31 = np.genfromtxt('hw8data/cepv31.dat',skip_header=3)


JD_cepv = 2449000 + np.concatenate((cepv5[:,0],cepv7[:,0],cepv13[:,0],cepv16[:,0],cepv17[:,0],cepv19[:,0],cepv20[:,0],cepv22[:,0],cepv25[:,0],cepv31[:,0]), axis=0)
vmag_cepv = np.concatenate((cepv5[:,1],cepv7[:,1],cepv13[:,1],cepv16[:,1],cepv17[:,1],cepv19[:,1],cepv20[:,1],cepv22[:,1],cepv25[:,1],cepv31[:,1]), axis=0)

#print JD_cepv, vmag_cepv

JD = []
V = []

JD = np.genfromtxt("rv2346.dat", usecols = 0)
V = np.genfromtxt("rv2346.dat", usecols = 1)
'''
period = np.arange(3.5, 57.0, 0.02)

for i in period:
	plt.clf()
	phase_frac = (JD_cepv - JD_cepv[0])%i/i
	plt.plot(phase_frac, vmag_cepv, "o")
	plt.xlabel('Phase Fraction', fontname="Arial", fontsize = 16)
	plt.ylabel('Radial Velocity [km/s]', fontname="Arial", fontsize = 16)
	plt.title("Period: "+str(i)+" [days]")
	plt.show()

'''
'''
plt.clf()
model = periodic.LombScargleFast(fit_period=True)
model.optimizer.period_range = (3.5, 49.0)
model.fit(JD_cepv, vmag_cepv, None)
print(model.best_period)
'''

#plt.clf()
model = periodic.LombScargleFast(fit_period=True)
model.optimizer.period_range = (3.5, 49.0)
model.fit(2449000+cepv31[:,0], cepv31[:,1], None)
print model.best_period, np.mean(cepv31[:,1])


