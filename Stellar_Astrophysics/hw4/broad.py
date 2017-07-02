from astropy import units as u
import numpy as np
from astropy import constants as const
import matplotlib.pyplot as plt
import scipy
from scipy import special

#====problem 1 in hertz
d_lamb = ([])
d_gamma = ([])
t_0 = 10**(-8) * u.second
gam = 2/t_0
print gam.unit
#lam_0 = 5000 * u.angstrom
lam_0 = 4481 * u.angstrom

v_0 = (const.c / lam_0).si

#np.linspace
#freq = (const.c / (np.arange(5000-50,5000+50) *u.angstrom)).si
#freq = (const.c / (np.linspace(5000-(10**-3),5000+(10**-3),num=1000) *u.angstrom)).si
freq = (const.c / (np.linspace(4481-(10**-0),4481+(10**-0),num=1000) *u.angstrom)).si

for i in freq:
	#lamb = ((i**2)/(2*np.pi*const.c))*((1/t_0) + (1/t_0))
	lamb = (gam/(4*np.pi**2))/((i - v_0)**2 + (gam/(4*np.pi))**2)
	#print lamb.unit
	d_lamb = np.append(d_lamb, lamb)

#wave = (const.c / d_lamb).to('AA')
wave = (const.c / freq).to('AA')

#print wave.unit



norm_lamb = d_lamb / np.amax(d_lamb)
#print norm_lamb

'''
#plt.plot(wave, d_lamb)
plt.plot(wave, norm_lamb)
plt.xlabel('Wavelength [$\AA$]', fontname="Arial", fontsize = 14)
plt.ylabel('Normalized Intensity', fontname="Arial", fontsize = 14)
plt.axhline(y=np.amax(norm_lamb)/2, xmin=0, xmax=1, hold=None, color='g')
plt.minorticks_on()
plt.grid(True)
#plt.savefig('nat1.pdf', format='pdf', dpi=900)
plt.show()
'''
#======problem 2

T = 10000 * u.K
mg_lam = 4481 * u.AA
A = 24.0
#m_u = 1.67*10**-24 u.g


v_th = (np.sqrt((2.0*const.k_B * T)/(A * const.u))).to('km/s')
print v_th


lambda_d = (((2.0 * mg_lam)/const.c)*v_th).to('AA')

print lambda_d
d_gaussian = ([])
lambda_queue = np.linspace(4481-1,4481+1,num=1000) * u.AA

for i in lambda_queue:
	gaussian = np.exp(-((i - mg_lam)**2)/(lambda_d**2))
	#gaussian = np.exp(-(((mg_lam+lambda_d) - mg_lam)**2)/(lambda_d**2))
	d_gaussian = np.append(d_gaussian,gaussian)

plt.plot(wave, norm_lamb, color='blue')
#plt.axvline(x=4481, ymin=0, ymax=1, hold=None, color='purple')
plt.plot(lambda_queue, d_gaussian, color='red')
plt.xlabel('Wavelength [$\AA$]', fontname="Arial", fontsize = 14)
plt.ylabel('Normalized Intensity', fontname="Arial", fontsize = 14)
plt.minorticks_on()
plt.ylim([10**-6,1])
plt.grid(True)
plt.yscale('log')
#plt.savefig('dopper.pdf', format='pdf', dpi=900)

plt.show()



