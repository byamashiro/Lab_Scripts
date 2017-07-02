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

JD = []
V = []

JD = np.genfromtxt("rv2346.dat", usecols = 0)
V = np.genfromtxt("rv2346.dat", usecols = 1)

#period = np.arange(15, 17, 0.1)
#period = np.arange(16, 17, 0.0000000000001)
'''
for i in period:
	plt.clf()
	phase_frac = (JD - JD[0])%i/i
	plt.plot(phase_frac, V, "o")
	plt.xlabel('Phase Fraction', fontname="Arial", fontsize = 16)
	plt.ylabel('Radial Velocity [km/s]', fontname="Arial", fontsize = 16)
	plt.title("Period: "+str(i)+" [days]")
	plt.show()
'''
plt.clf()
model = periodic.LombScargleFast(fit_period=True)
model.optimizer.period_range = (3.0, 40.0)
model.fit(JD, V, None)
print(model.best_period)

