import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimized
import os

data = np.genfromtxt('reduced.dat')# skip_footer = 1

Mg_wavelengths = data[:,0]
Mg_intensity = data[:,1]

#a is height of curve, b is peak, d is where it starts in the y-axis
a = -0.23
b = 4481.89
c = 4481.228/(68000*2*np.sqrt(2*np.log(2)))
d = 0.96

def func_gaussian(x, b):
	y = a * np.exp((-(x-b)**2)/(2*c**2)) + d
	return y

param, covar = optimized.curve_fit(func_gaussian, Mg_wavelengths, Mg_intensity, p0 = [b])

plt.ticklabel_format(useOffset=False)
plt.plot(Mg_wavelengths, Mg_intensity, 'o', color = 'blue' ,markersize = 7.0, alpha = 0.4)
plt.plot(Mg_wavelengths, func_gaussian(Mg_wavelengths, param[0]), 'r', lw=2) #Mg_sort, param[0]
plt.xlim(4481.228-2,4481.228+2)
plt.ylim(0.7, 1.1)
plt.xlabel('Wavelength [$\AA$]', fontname="Arial", fontsize = 14)
plt.ylabel('Intensity', fontname="Arial", fontsize = 14)
#plt.title('Mg II Absorption')

plt.minorticks_on()
plt.grid(True)
plt.savefig('Mg_absorp.pdf', format='pdf', dpi=900)
plt.show()