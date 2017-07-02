import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


from astropy.stats import sigma_clip
from numpy import mean


#=============Parallax Histogram


vizier = np.genfromtxt('vizier.tsv', skip_header = 65)# skip_footer = 1

parallax = vizier[:,3]
print parallax

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
#=============Parallax Histogram


vizier = np.genfromtxt('vizier.tsv', skip_header = 65)# skip_footer = 1
vizier_rej = np.genfromtxt('rejected.txt', skip_header = 3)# skip_footer = 1


magnitude = vizier[:,9]
magnitude_err = vizier[:,10]

magnitude_rej = vizier_rej[:,9]
magnitude_err_rej = vizier_rej[:,10]

color = vizier[:,11]
color_err = vizier[:,12]

color_rej = vizier_rej[:,11]
color_err_rej = vizier_rej[:,12]

#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
plt.xlim((min(color)-.25, max(color)+.25))

ax = fig.add_subplot(1, 1, 1)

#fig = plt.figure(figsize=(17,6))
#plt.subplot(121)

plt.errorbar(color, magnitude, xerr=color_err, yerr=magnitude_err, fmt='o', color='blue')
ax.errorbar(color_rej, magnitude_rej, xerr=color_err_rej, yerr=magnitude_err_rej, fmt='o', color='red')

plt.xlabel('(B-V)', fontname="Arial", fontsize = 14)
plt.ylabel('Hipparcos Magnitude', fontname="Arial", fontsize = 14)
plt.title('HIPPARCOS Magnitude of the Pleiades')
#plt.axvline(0, color='red', linestyle='dashed', linewidth=2)
#plt.axvline(16, color='red', linestyle='dashed', linewidth=2)

#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)
plt.savefig('magnitude.pdf', format='pdf', dpi=1000)

plt.show()


#=============Distance Histogram


vizier = np.genfromtxt('vizier.tsv', skip_header = 65)# skip_footer = 1

parallax = vizier[:,3]
distance = (1/parallax)*1000
#print x_quartz
#print x_quartz, y_quartz, quartz_multi

#fig = plt.figure()
#bx = fig.add_subplot(1, 1, 1)

fig = plt.figure(figsize=(17,6))

plt.subplot(121)

n, bins, patches = plt.hist(distance, 15, histtype='bar', stacked=False, fill=True, alpha=0.5) #range=(0, 15)

plt.xlabel('Distance [pc]', fontname="Arial", fontsize = 14)
plt.ylabel('Number', fontname="Arial", fontsize = 14)
plt.title('HIPPARCOS Distance of the Pleiades')
plt.axvline(0, color='red', linestyle='dashed', linewidth=2)
plt.axvline(400, color='red', linestyle='dashed', linewidth=2)

#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.subplot(122)
n, bins, patches = plt.hist(distance, 15, histtype='bar', stacked=False, range=(0,400), fill=True, alpha=0.5) #range=(0, 15)
plt.xlabel('Distance [pc]', fontname="Arial", fontsize = 14)
plt.ylabel('Number', fontname="Arial", fontsize = 14)
plt.title('HIPPARCOS Distance of the Pleiades')
#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)


plt.savefig('distancehist.pdf', format='pdf', dpi=1000)

plt.show()

#=============Distance velocity


vizier = np.genfromtxt('vizier_new.txt', skip_header = 65)# skip_footer = 
vizier_rej = np.genfromtxt('rejected.txt', skip_header = 3)# skip_footer = 1


parallax = vizier[:,3]
parallax_as = parallax*1000
distance = (1/parallax)*1000

parallax_rej = vizier_rej[:,3]
parallax_as_rej = parallax_rej*1000
distance_rej = (1/parallax_rej)*1000

pm_ra = (vizier[:,5])*1000
pm_dec = (vizier[:,7])*1000

pm_ra_rej = (vizier_rej[:,5])*1000
pm_dec_rej = (vizier_rej[:,7])*1000

pm_full = np.sqrt(pm_ra**2 + pm_dec**2)

pm_full_rej = np.sqrt(pm_ra_rej**2 + pm_dec_rej**2)


vel_t = (4.75 * pm_full)/parallax_as
vel_t_rej = (4.75 * pm_full_rej)/parallax_as_rej



#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#fig = plt.figure(figsize=(17,6))
#plt.subplot(121)

plt.plot(distance,vel_t, 'o', color='blue') #mfc='none',
ax.plot(distance_rej,vel_t_rej, 'o', color='red') #mfc='none',

plt.xlabel('Distance [pc]', fontname="Arial", fontsize = 14)
plt.ylabel('Tangential Velocity [km/s]', fontname="Arial", fontsize = 14)
plt.title('Galaxy Tangential Velocity vs. Distance')
#plt.axvline(0, color='red', linestyle='dashed', linewidth=2)
#plt.axvline(400, color='red', linestyle='dashed', linewidth=2)

#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.savefig('distancevel.pdf', format='pdf', dpi=1000)


plt.show()

#=============Distance modulous


vizier = np.genfromtxt('vizier.tsv', skip_header = 65)# skip_footer = 1

parallax = vizier[:,3]
parallax_as = parallax*1000
distance = (1/parallax)*1000

magnitude = vizier[:,9]
magnitude_err = vizier[:,10]

abs_mag = magnitude + 5 - np.log10(distance)
print abs_mag

dist_mod = magnitude - abs_mag


pm_ra = (vizier[:,5])*1000
pm_dec = (vizier[:,7])*1000

pm_full = np.sqrt(pm_ra**2 + pm_dec**2)

vel_t = (4.75 * pm_full)/parallax_as


#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
#bx = fig.add_subplot(1, 1, 1)

#fig = plt.figure(figsize=(17,6))
#plt.subplot(121)

plt.plot(parallax_as,dist_mod, 'o', mfc='none', color='blue')
plt.xlabel('Parallax [as]', fontname="Arial", fontsize = 14)
plt.ylabel('(m-M)', fontname="Arial", fontsize = 14)
plt.title('Distance Modulus vs. Parallax')
#plt.axvline(0, color='red', linestyle='dashed', linewidth=2)
#plt.axvline(400, color='red', linestyle='dashed', linewidth=2)

#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.savefig('distancemod.pdf', format='pdf', dpi=1000)


plt.show()

#=============Distance modulous


vizier = np.genfromtxt('vizier.tsv', skip_header = 65)# skip_footer = 1

parallax = vizier[:,3]
parallax_as = parallax*1000
distance = (1/parallax)*1000

magnitude = vizier[:,9]
magnitude_err = vizier[:,10]

abs_mag = magnitude + 5 - np.log10(distance)
print abs_mag

dist_mod = magnitude - abs_mag


pm_ra = (vizier[:,5])*1000
pm_dec = (vizier[:,7])*1000

pm_full = np.sqrt(pm_ra**2 + pm_dec**2)

vel_t = (4.75 * pm_full)/parallax_as


#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
#bx = fig.add_subplot(1, 1, 1)

#fig = plt.figure(figsize=(17,6))
#plt.subplot(121)

plt.plot(parallax_as,vel_t, 'o', mfc='none', color='blue')
plt.xlabel('Tangential Velocity [km/s]', fontname="Arial", fontsize = 14)
plt.ylabel('(m-M)', fontname="Arial", fontsize = 14)
plt.title('Distance Modulus vs. Tangential Velocity')
#plt.axvline(0, color='red', linestyle='dashed', linewidth=2)
#plt.axvline(400, color='red', linestyle='dashed', linewidth=2)

#plt.axis([40, 160, 0, 0.03])
plt.minorticks_on()
plt.grid(True)

plt.savefig('moddistance.pdf', format='pdf', dpi=1000)


plt.show()





