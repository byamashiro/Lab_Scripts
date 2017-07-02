import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.optimize import curve_fit

from astropy.modeling import models, fitting
from astropy.modeling.models import GaussianAbsorption1D
from astropy.stats import sigma_clip
from numpy import mean

'''
#=============Parallax Histogram


data = np.genfromtxt('1753905in.s', skip_header = 2)# skip_footer = 1

wavelength = data[:,0]
intensity = data[:,1]
#print x_quartz
#print x_quartz, y_quartz, quartz_multi

#fig = plt.figure()
#bx = fig.add_subplot(1, 1, 1)

fig = plt.figure(figsize=(17,6))

plt.subplot(121)

n, bins, patches = plt.hist(parallax, 15, histtype='bar', stacked=False, fill=True, alpha=0.5) #range=(0, 15)

plt.xlabel('Parallax [mas]', fontname="Arial", fontsize = 14)
plt.ylabel('Number', fontname="Arial", fontsize = 14)
plt.title('HIPPARCOS Parallax of the Pleiades')
plt.axvline(0, color='red', linestyle='dashed', linewidth=2)
plt.axvline(16, color='red', linestyle='dashed', linewidth=2)

#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.subplot(122)
n, bins, patches = plt.hist(parallax, 15, histtype='bar', stacked=False, range=(0,15), fill=True, alpha=0.5) #range=(0, 15)
plt.xlabel('Parallax [mas]', fontname="Arial", fontsize = 14)
plt.ylabel('Number', fontname="Arial", fontsize = 14)
plt.title('HIPPARCOS Parallax of the Pleiades')
#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.savefig('parallax.pdf', format='pdf', dpi=1000)

plt.show()
'''

#========Boltzmann Equation

k = 8.617*(10**(-5)) #eV/K
T = 3000.0
g_1 = 2.0
g_2 = 8.0
g_frac = g_1 / g_2

E_1 = 0.0
E_2 = 13.6 * (1-(1/4))


boltz = g_frac * np.exp(-(E_1 - E_2)/(k * T))
print "Temp: ",T, "   ", "Population: ", 1/boltz


#==================number density
rho = 3.5*(10**(-7))
rho_2 = 3.5*(10**(-8))
m_H_g = 1.6737236 * (10**(-24))
n_a = 6.02214179 * (10**(23))
nd = (n_a/(m_H_g))*rho
nd_2 = (n_a/(m_H_g))*rho_2


h = 6.62607004 * (10**(-34))

print "Number Density [n_H]: " , nd

#===== Saha Equation

m_H_kg = 1.6737236 * (10**(-27))

n_hydrogen = (1/nd)*(((2*np.pi*m_H_kg*k*T)/(h**2))**(3/2))*np.exp(-13.6/(k*T))
n_hydrogen_2 = (1/nd_2)*(((2*np.pi*m_H_kg*k*T)/(h**2))**(3/2))*np.exp(-13.6/(k*T))

print "Population (Saha): ", n_hydrogen, "    ", "Updated Saha: ", n_hydrogen_2

#=============Absorptions


data = np.genfromtxt('1753905in.s', skip_header = 2)# skip_footer = 1

wavelength = data[:,0]
angstrom = wavelength * 10

intensity = data[:,1]

#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#fig = plt.figure(figsize=(17,6))
#plt.subplot(121)

#ax.plot(distance_rej,vel_t_rej, 'o', color='red') #mfc='none',
plt.xlim([4200,6700])
plt.ylim([0,1.5])


plt.xlabel('Wavelength [A]', fontname="Arial", fontsize = 14)
plt.ylabel('Normalized Intensity', fontname="Arial", fontsize = 14)
#plt.title('Galaxy Tangential Velocity vs. Distance')
plt.axvline(6562.81, color='red', linestyle='dashed', linewidth=2) #Halpha
plt.axvline(6276.61, color='red', linestyle='dashed', linewidth=2) #O2
plt.axvline(5895.618, color='red', linestyle='dashed', linewidth=2) #Na
plt.axvline(4861.34, color='red', linestyle='dashed', linewidth=2) #hbeta
plt.axvline(4340.47, color='red', linestyle='dashed', linewidth=2) #hgamma
plt.axvline(4307.74, color='red', linestyle='dashed', linewidth=2)
plt.plot(angstrom,intensity, 'o', color='blue') #mfc='none',


#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.savefig('absorption.pdf', format='pdf', dpi=1000)


plt.show()

#=============Mg II

data = np.genfromtxt('1753905in.s', skip_header = 2)# skip_footer = 1

wavelength = data[:,0]
angstrom = wavelength * 10

intensity = data[:,1]

#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#def func(x, a, x0, sigma):
#    return a*np.exp(-(x-x0)**2/(2*sigma**2))


#x = angstrom
#y = intensity

#popt, pcov = curve_fit(func, x, y)
#print popt
#ym = func(x, popt[0], popt[1], popt[2])

#popt, pcov = curve_fit(func, angstrom, intensity)
#print popt
#ym = func(angstrom, popt[0], popt[1], popt[2])



#fig = plt.figure(figsize=(17,6))
#plt.subplot(121)


#g_init = models.Gaussian1D(amplitude=0.3, mean=4481.228, stddev=.5)
#fit_g = fitting.LevMarLSQFitter()
#g = fit_g(g_init, angstrom, intensity)

#s1 = GaussianAbsorption1D(amplitude=2., mean=4481.91, stddev=0.4)
#r = np.arange((4481.228-2),(4481.228+2), .01)
#for factor in range(1, 2):
#    s1.amplitude = factor
#    plt.plot(angstrom, s1(angstrom), color=str(0.25 * factor), lw=2)

plt.plot(angstrom,intensity, 'o', color='red') #mfc='none',
#ax.plot(x,ym, c='blue', label ='Best Fit')
#plt.plot(angstrom,g(angstrom), 'o', color='blue', label = 'Gaussian') #mfc='none',
#ax.plot(distance_rej,vel_t_rej, 'o', color='red') #mfc='none',
plt.xlim([(4481.228-2),(4481.228+2)])
plt.ylim([(0.7),(1.2)])


plt.xlabel('Wavelength [A]', fontname="Arial", fontsize = 14)
plt.ylabel('Normalized Intensity', fontname="Arial", fontsize = 14)
#plt.title('Galaxy Tangential Velocity vs. Distance')


#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)
plt.legend(loc=2)

plt.savefig('mgII.pdf', format='pdf', dpi=1000)


plt.show()

#=============Fe II

data = np.genfromtxt('1753905in.s', skip_header = 2)# skip_footer = 1

wavelength = data[:,0]
angstrom = wavelength * 10

intensity = data[:,1]

#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#fig = plt.figure(figsize=(17,6))
#plt.subplot(121)

plt.plot(angstrom,intensity, 'o', color='orange') #mfc='none',
#ax.plot(distance_rej,vel_t_rej, 'o', color='red') #mfc='none',
plt.xlim([(4508.27-2),(4508.27+2)])
plt.ylim([(0.7),(1.2)])

plt.xlabel('Wavelength [A]', fontname="Arial", fontsize = 14)
plt.ylabel('Normalized Intensity', fontname="Arial", fontsize = 14)
#plt.title('Galaxy Tangential Velocity vs. Distance')


#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.savefig('feII.pdf', format='pdf', dpi=1000)


plt.show()

#=============N V

data = np.genfromtxt('1753905in.s', skip_header = 2)# skip_footer = 1

wavelength = data[:,0]
angstrom = wavelength * 10

intensity = data[:,1]

#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#fig = plt.figure(figsize=(17,6))
#plt.subplot(121)

plt.plot(angstrom,intensity, 'o', color='yellow') #mfc='none',
#ax.plot(distance_rej,vel_t_rej, 'o', color='red') #mfc='none',
plt.xlim([(4603.73-2),(4603.73+2)])
plt.ylim([(0.7),(1.2)])

plt.xlabel('Wavelength [A]', fontname="Arial", fontsize = 14)
plt.ylabel('Normalized Intensity', fontname="Arial", fontsize = 14)
#plt.title('Galaxy Tangential Velocity vs. Distance')


#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.savefig('nV.pdf', format='pdf', dpi=1000)


plt.show()

#=============O V

data = np.genfromtxt('1753905in.s', skip_header = 2)# skip_footer = 1

wavelength = data[:,0]
angstrom = wavelength * 10

intensity = data[:,1]

#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#fig = plt.figure(figsize=(17,6))
#plt.subplot(121)

plt.plot(angstrom,intensity, 'o', color='green') #mfc='none',
#ax.plot(distance_rej,vel_t_rej, 'o', color='red') #mfc='none',
plt.xlim([(5114.07-2),(5114.07+2)])
plt.ylim([(0.7),(1.2)])

plt.xlabel('Wavelength [A]', fontname="Arial", fontsize = 14)
plt.ylabel('Normalized Intensity', fontname="Arial", fontsize = 14)
#plt.title('Galaxy Tangential Velocity vs. Distance')


#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.savefig('oV.pdf', format='pdf', dpi=1000)


plt.show()

#=============C IV

data = np.genfromtxt('1753905in.s', skip_header = 2)# skip_footer = 1

wavelength = data[:,0]
angstrom = wavelength * 10

intensity = data[:,1]

#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#fig = plt.figure(figsize=(17,6))
#plt.subplot(121)

plt.plot(angstrom,intensity, 'o', color='blue') #mfc='none',
#ax.plot(distance_rej,vel_t_rej, 'o', color='red') #mfc='none',
plt.xlim([(5801.33-2),(5801.33+2)])
plt.ylim([(0.7),(1.2)])

plt.xlabel('Wavelength [A]', fontname="Arial", fontsize = 14)
plt.ylabel('Normalized Intensity', fontname="Arial", fontsize = 14)
#plt.title('Galaxy Tangential Velocity vs. Distance')


#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.savefig('cIV.pdf', format='pdf', dpi=1000)


plt.show()

#=============C IV_2

data = np.genfromtxt('1753905in.s', skip_header = 2)# skip_footer = 1

wavelength = data[:,0]
angstrom = wavelength * 10

intensity = data[:,1]

#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#fig = plt.figure(figsize=(17,6))
#plt.subplot(121)

plt.plot(angstrom,intensity, 'o', color='purple') #mfc='none',
#ax.plot(distance_rej,vel_t_rej, 'o', color='red') #mfc='none',
plt.xlim([(5811.98-2),(5811.98+2)])
plt.ylim([(0.7),(1.2)])

plt.xlabel('Wavelength [A]', fontname="Arial", fontsize = 14)
plt.ylabel('Normalized Intensity', fontname="Arial", fontsize = 14)
#plt.title('Galaxy Tangential Velocity vs. Distance')


#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.savefig('cIV_2.pdf', format='pdf', dpi=1000)


plt.show()
'''
#===velocities
c = 299792458.0

l_mg = 4481.228
l_fe = 4508.27
l_v = 4603.73
l_o = 5114.07
l_ci = 5801.33
l_cii = 5811.98

n_mg = 4481.91
n_fe = 4509.08
n_v = 4604.62
n_o = 5115.08
n_ci = 5802.42
n_cii = 5813.08

v_mg = (c - n_mg)/l_mg
v_fe = (c - n_fe)/l_fe
n_v = (c - n_v)/l_v
v_o = (c - n_o)/l_o
v_ci = (c - n_ci)/l_ci
v_cii = (c - n_cii)/l_cii

print v_mg 
print v_fe 
print n_v 
print v_o 
print v_ci 
print v_cii
'''


