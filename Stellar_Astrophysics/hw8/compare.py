from astropy import units as u
import numpy as np
from astropy import constants as const
import matplotlib.pyplot as plt
import scipy
from scipy import special
from scipy.optimize import curve_fit


pleiades = np.genfromtxt('hw8data/cluple.dat',skip_header=3) # usecols=0 , delimiter=' ', dtype=None
clu6087 = np.genfromtxt('hw8data/clu6087.dat',skip_header=3) # usecols=0 , delimiter=' ', dtype=None



def func(x, a, b, c):
	return a * np.exp(-b * x) + c

popt, pcov = curve_fit(func, clu6087[:,1], clu6087[:,2])
qopt, qcov = curve_fit(func, pleiades[:,1], pleiades[:,2])



#=========attempt for polynomial fit
'''
poly_ple = np.polyfit(pleiades[:,1], pleiades[:,2], 3)
poly_clu = np.polyfit(clu6087[:,1]-0.1, clu6087[:,2], 3)

p_ple = np.poly1d(poly_ple)
p_clu = np.poly1d(poly_clu)

x_ple = np.linspace(-0.1, 0.2, 100)
x_clu = np.linspace(0.0, 0.35, 100)
'''

'''
fig = plt.figure(figsize=(18,6))
plt.subplot(121)

plt.plot(pleiades[:,1], pleiades[:,0], 'o', color='blue')
plt.plot(clu6087[:,1], clu6087[:,0],'o', color='red')
plt.xlabel('(B-V)', fontname="Arial", fontsize = 14)
plt.ylabel('(V-B)', fontname="Arial", fontsize = 14)
plt.minorticks_on()
#plt.ylim([10**-6,1])
plt.grid(True)
#plt.yscale('log')
#plt.savefig('dopper.pdf', format='pdf', dpi=900)
#plt.axvline(x=4481, ymin=0, ymax=1, hold=None, color='purple')


plt.subplot(122)
plt.plot(pleiades[:,1], pleiades[:,0], 'o', color='blue')
plt.plot(clu6087[:,1], corrected_V,'o', color='red')
plt.xlabel('(B-V)', fontname="Arial", fontsize = 14)
plt.ylabel('(V-B)', fontname="Arial", fontsize = 14)
plt.minorticks_on()
#plt.ylim([10**-6,1])
plt.grid(True)


plt.show()

'''
'''
fig = plt.figure(figsize=(18,6))
plt.subplot(121)
plt.plot(pleiades[:,1], pleiades[:,2], 'o', color='blue')
#plt.plot(x_ple,p_ple(x_ple),'-', color='blue')


plt.plot(clu6087[:,1], clu6087[:,2],'o', color='red')

#plt.plot(x_clu,p_clu(x_clu),'-', color='red')

plt.xlabel('(B-V)', fontname="Arial", fontsize = 14)
plt.ylabel('(V-B)', fontname="Arial", fontsize = 14)
plt.minorticks_on()
#plt.ylim([10**-6,1])
plt.grid(True)
#plt.yscale('log')
#plt.savefig('dopper.pdf', format='pdf', dpi=900)
#plt.axvline(x=4481, ymin=0, ymax=1, hold=None, color='purple')

plt.subplot(122)
plt.plot(pleiades[:,1], pleiades[:,2], 'o', color='blue')


#plt.axvline(x=4481, ymin=0, ymax=1, hold=None, color='purple')
plt.plot(clu6087[:,1]-0.15, clu6087[:,2]-0.12,'o', color='red')

plt.xlabel('(B-V)', fontname="Arial", fontsize = 14)
plt.ylabel('(V-B)', fontname="Arial", fontsize = 14)
plt.minorticks_on()
#plt.ylim([10**-6,1])
plt.grid(True)
#plt.yscale('log')
#plt.savefig('dopper.pdf', format='pdf', dpi=900)

plt.show()
'''

#========Step 1
print "====Step 1"

#0 = V
#1 = B-V
#2 = U-B

#pleiades
#clu6087 

EBV = 0.18
A_V = 3.1 * EBV
V_0 = pleiades[:,0] - A_V

diff = 4.7

print "Average Visual Magnitude: ", np.mean(V_0)
print "Color Excess E(B-V): ", EBV


#print A_V
#new plots
fig = plt.figure(figsize=(18,6))
plt.subplot(121)
plt.plot(pleiades[:,1], pleiades[:,0], 'o', color='blue')
#plt.axvline(x=4481, ymin=0, ymax=1, hold=None, color='purple')
plt.plot(clu6087[:,1], clu6087[:,0],'o', color='red')
plt.xlabel('(B-V)', fontname="Arial", fontsize = 14)
plt.ylabel('V', fontname="Arial", fontsize = 14)
plt.gca().invert_yaxis()
plt.minorticks_on()
#plt.ylim([10**-6,1])
plt.grid(True)

plt.subplot(122)
plt.plot(pleiades[:,1], pleiades[:,0], 'o', color='blue')
#plt.axvline(x=4481, ymin=0, ymax=1, hold=None, color='purple')
plt.plot(clu6087[:,1]-0.15, clu6087[:,0]-A_V-diff,'o', color='red')
plt.xlabel('(B-V)', fontname="Arial", fontsize = 14)
plt.ylabel('V', fontname="Arial", fontsize = 14)
plt.gca().invert_yaxis()
plt.minorticks_on()
#plt.ylim([10**-6,1])
plt.grid(True)
#plt.show()

#np.log10(distance) = (5.0*np.log(120.0) - 5.0)/5.0
distance = 10.0**((5.0*np.log10(120.0) + diff)/5.0)
print "Distance Modulus: ", diff
print "Distance to Cluster NGC 6087: ",distance*u.parsec

app_mag = 6.42
abs_mag = app_mag + 5.0 - np.log10(distance)

print "Average Absolute Visual Magnitude: ", abs_mag


lum = 10.0**((4.8-abs_mag)/2.5)
print "Luminosity in solar lum: ", lum


app_mod = abs_mag - 5.0 + np.log10(25000000.0)
print "Apparent V-mag at 25 Mpc: ", app_mod

app_dist = 10.0**(app_mod - 4.8 +5.0)
print "Distance Sun same app V-mag: ", app_dist


#====Step 2
print "====Step 2"

cepgal = np.genfromtxt('hw8data/cepgal.dat',skip_header=2)
plr = np.genfromtxt('hw8data/plr.dat',skip_header=2)
spc = np.genfromtxt('hw8data/spc.dat',skip_header=2)

EBmV = 0.12
AvLMC = 3.1 * EBmV
plr_mag = plr[:,1] - AvLMC
spc_mag = spc[:,1] - AvLMC

distmod = 18.5


print "Distance modulus (LMC): ", distmod
fig = plt.figure(figsize=(18,6))

plt.plot(np.log10(cepgal[:,0]), cepgal[:,1], 'o', color='blue')
plt.plot(np.log10(plr[:,0])+1.0, plr_mag-distmod,'o', color='red')
plt.plot(np.log10(spc[:,0])+1.0, spc_mag-distmod,'o', color='green')

plt.xlabel('log(Period)', fontname="Arial", fontsize = 14)
plt.ylabel('log(V)', fontname="Arial", fontsize = 14)
plt.gca().invert_yaxis()
plt.minorticks_on()
#plt.ylim([10**-6,1])
plt.grid(True)
plt.show()


#abs_cepgal = np.mean(cepgal[:,1])
#print abs_cepgal
#distance_lmc = 10.0**((5.0*np.log10(abs_mag) + distmod)/5.0)
distance_lmc = 10.0**((distmod+5.0)/5.0)

#distance_lmc = 10.0**(distmod + 5.0) #needs to be changed
print "Distance to the LMC: ", distance_lmc



#====Step 3
print "====Step 3"
n1365_v = np.genfromtxt('hw8data/n1365.dat',skip_header=2)
n1365_i = np.genfromtxt('hw8data/imag.dat')

plr = np.genfromtxt('hw8data/plr.dat',skip_header=2)


#distance to the lmc

v_cep_distmod = 12.7
i_cep_distmod = 12.5



#12.8 in the modulus between lmc and cepheid
fig = plt.figure(figsize=(18,6))
plt.subplot(121)
plt.plot(np.log10(n1365_v[:,0]), n1365_v[:,1]-v_cep_distmod, 'o', color='blue')
plt.plot(np.log10(plr[:,0])+1.0, plr_mag,'o', color='red')
plt.xlabel('log(Period)', fontname="Arial", fontsize = 14)
plt.ylabel('log(V)', fontname="Arial", fontsize = 14)
plt.gca().invert_yaxis()
plt.minorticks_on()
#plt.ylim([10**-6,1])
plt.grid(True)

plt.subplot(122)
plt.plot(np.log10(n1365_i[:,1]), n1365_i[:,2]-i_cep_distmod, 'o', color='green')
plt.plot(np.log10(plr[:,0])+1.3, (plr[:,1]-plr[:,2])-(0.48*AvLMC),'o', color='red')
plt.xlabel('log(Period)', fontname="Arial", fontsize = 14)
plt.ylabel('log(V)', fontname="Arial", fontsize = 14)
plt.gca().invert_yaxis()
plt.minorticks_on()
#plt.ylim([10**-6,1])
plt.grid(True)
plt.show()


print "Distance Modulus LMC Cephid: ", v_cep_distmod

avg_abs_vmag = np.mean(n1365_v[:,1])
#print avg_abs_vmag

distance_1365_v = 10.0**((5.0*np.log10(distance_lmc) + (v_cep_distmod))/5.0)
distance_1365_i = 10.0**((5.0*np.log10(distance_lmc) + (i_cep_distmod))/5.0)

print "Distance to the NGC 1365 Vmag (pc): ", distance_1365_v
print "Distance to the NGC 1365 Imag (pc): ", distance_1365_i

Hubble = (7185.0 * (u.kilometer/u.second))/(((distance_1365_v*u.parsec) * 5.7) )
print "Hubble Constant: ", Hubble.to(u.km/u.second/u.megaparsec)

inversehubble = 1.0/Hubble
print "Inverse Hubble: ", inversehubble.to(u.year)

exit(0)



#d_gaussian = ([])
#lambda_queue = np.linspace(4481-1,4481+1,num=1000) * u.AA

#for i in lambda_queue:
#	gaussian = np.exp(-((i - mg_lam)**2)/(lambda_d**2))
#	#gaussian = np.exp(-(((mg_lam+lambda_d) - mg_lam)**2)/(lambda_d**2))
#	d_gaussian = np.append(d_gaussian,gaussian)

