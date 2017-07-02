import numpy as np
import matplotlib.pyplot as plt

from astropy.stats import sigma_clip
from numpy import mean


#=============halogen gasses
wavelengths_argon = []
counts_argon = []
with open('gas/element-argon.spec','r') as f:
    for line in f:
        try:
            x, y = line.strip(' \t\r\n\0').split('\t')
            wavelengths_argon.append(float(x))
            counts_argon.append(float(y))
        except:
			pass

wavelengths_argon_2 = np.array(wavelengths_argon)
counts_argon_2 = np.array(counts_argon)

wavelengths_helium = []
counts_helium = []
with open('gas/element-helium.spec','r') as f:
    for line in f:
        try:
            x, y = line.strip(' \t\r\n\0').split('\t')
            wavelengths_helium.append(float(x))
            counts_helium.append(float(y))
        except:
			pass

wavelengths_helium_2 = np.array(wavelengths_helium)
counts_helium_2 = np.array(counts_helium)

wavelengths_hydrogen = []
counts_hydrogen = []
with open('gas/element-hydrogen.spec','r') as f:
    for line in f:
        try:
            x, y = line.strip(' \t\r\n\0').split('\t')
            wavelengths_hydrogen.append(float(x))
            counts_hydrogen.append(float(y))
        except:
			pass

wavelengths_hydrogen_2 = np.array(wavelengths_hydrogen)
counts_hydrogen_2 = np.array(counts_hydrogen)

wavelengths_mercury = []
counts_mercury = []
with open('gas/element-mercury.spec','r') as f:
    for line in f:
        try:
            x, y = line.strip(' \t\r\n\0').split('\t')
            wavelengths_mercury.append(float(x))
            counts_mercury.append(float(y))
        except:
			pass

wavelengths_mercury_2 = np.array(wavelengths_mercury)
counts_mercury_2 = np.array(counts_mercury)

wavelengths_neon = []
counts_neon = []
with open('gas/element-neon.spec','r') as f:
    for line in f:
        try:
            x, y = line.strip(' \t\r\n\0').split('\t')
            wavelengths_neon.append(float(x))
            counts_neon.append(float(y))
        except:
			pass

wavelengths_neon_2 = np.array(wavelengths_neon)
counts_neon_2 = np.array(counts_neon)

fig = plt.figure()
dx = fig.add_subplot(1, 1, 1)

dx.plot(wavelengths_argon_2, counts_argon_2, color = 'red')
dx.plot(wavelengths_helium_2, counts_helium_2, color = 'orange')
dx.plot(wavelengths_hydrogen_2, counts_hydrogen_2, color = 'yellow')
dx.plot(wavelengths_mercury_2, counts_mercury_2, color = 'green')
dx.plot(wavelengths_neon_2, counts_neon_2, color = 'blue')


plt.xlabel('Wavelength [$\lambda$]', fontname="Arial", fontsize = 18)
plt.ylabel('Counts', fontname="Arial", fontsize = 18)
plt.legend()

plt.minorticks_on()
plt.grid()


#plt.show()

#=============Hotdog
wavelengths_1 = []
counts_1 = []
with open('hotdog/hotdog-100V.spec','r') as f:
    for line in f:
        try:
            x, y = line.strip(' \t\r\n\0').split('\t')
            wavelengths_1.append(float(x))
            counts_1.append(float(y))
        except:
			pass
#            print(line)

hotdog_100_wavelength = np.array(wavelengths_1)
hotdog_100_counts = np.array(counts_1)

wavelengths_2 = []
counts_2 = []
with open('hotdog/hotdog-140V.spec','r') as f:
    for line in f:
        try:
            x, y = line.strip(' \t\r\n\0').split('\t')
            wavelengths_2.append(float(x))
            counts_2.append(float(y))
        except:
			pass
#            print(line)

hotdog_140_wavelength = np.array(wavelengths_2)
hotdog_140_counts = np.array(counts_2)

#print hotdog_100_wavelength

fig = plt.figure()
cx = fig.add_subplot(1, 1, 1)

cx.plot(hotdog_100_wavelength, hotdog_100_counts, color = 'blue')
cx.plot(hotdog_140_wavelength, hotdog_140_counts, color = 'red')
#plt.show()

#=============Condenser

quartz = np.genfromtxt('quartz/quartz_no_condenser.txt', skip_header = 17)# skip_footer = 1
quartz_multiplier = np.genfromtxt('quartz/quartz_condenser.txt', skip_header = 1)

#print quartz,quartz_multiplier


x_quartz = quartz[:,0]
y_quartz = quartz[:,1]
quartz_multi = (quartz[:,1] * quartz_multiplier[:,1])

#print x_quartz
#print x_quartz, y_quartz, quartz_multi

fig = plt.figure()
bx = fig.add_subplot(1, 1, 1)

bx.plot(x_quartz, y_quartz, color = 'blue')
bx.plot(x_quartz, quartz_multi, color = 'red')

#plt.show()

#=================1 second

bk_1s_1 = np.genfromtxt('background/bk_1_1s.txt')
bk_1s_2 = np.genfromtxt('background/bk_2_1s.txt')
bk_1s_3 = np.genfromtxt('background/bk_3_1s.txt')

bk_1s_all = (np.array(bk_1s_1) + np.array(bk_1s_2) + np.array(bk_1s_3)) / 3


dark_1s_1 = np.genfromtxt('dark/dark_1_1s.txt')
dark_1s_2 = np.genfromtxt('dark/dark_2_1s.txt')
dark_1s_3 = np.genfromtxt('dark/dark_3_1s.txt')

dark_1s_all = (np.array(dark_1s_1) + np.array(dark_1s_2) + np.array(dark_1s_3)) / 3



spectra_1s_1 = np.genfromtxt('xdata/x_1_1s.txt')
spectra_1s_2 = np.genfromtxt('xdata/x_2_1s.txt')
spectra_1s_3 = np.genfromtxt('xdata/x_3_1s.txt')

spectra_1s_all = (np.array(spectra_1s_1) + np.array(spectra_1s_2) + np.array(spectra_1s_3)) / 3

#print spectra_1s_all,bk_1s_all,dark_1s_all


x1 = bk_1s_all[:,0]
y1 = bk_1s_all[:,1]

x2 = dark_1s_all[:,0]
y2 = dark_1s_all[:,1]

x3 = spectra_1s_all[:,0]
y3 = spectra_1s_all[:,1]

diff = (spectra_1s_all[:,1] - (bk_1s_all[:,1] - dark_1s_all[:,1]) - dark_1s_all[:,1]) #y axis array

h1 = bk_1s_1[:,0]
k1 = bk_1s_1[:,1]

h2 = dark_1s_1[:,0]
k2 = dark_1s_1[:,1]

h3 = spectra_1s_1[:,0]
k3 = spectra_1s_1[:,1]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(x3, y3, color = 'blue')
ax.plot(x2, y2, color = 'red')
ax.plot(x1, y1, color = 'green')

ax.plot(x1, diff, color = 'black')



plt.xlabel('Wavelength [$\lambda$]', fontname="Arial", fontsize = 18)
plt.ylabel('Counts', fontname="Arial", fontsize = 18)
plt.legend()

plt.minorticks_on()
plt.grid()


#plt.show()

#=================4 second
bk_4s_1 = np.genfromtxt('background/bk_1_4s.txt')
bk_4s_2 = np.genfromtxt('background/bk_2_4s.txt')
bk_4s_3 = np.genfromtxt('background/bk_3_4s.txt')

bk_4s_all = (np.array(bk_4s_1) + np.array(bk_4s_2) + np.array(bk_4s_3)) / 3


dark_4s_1 = np.genfromtxt('dark/dark_1_4s.txt')
dark_4s_2 = np.genfromtxt('dark/dark_2_4s.txt')
dark_4s_3 = np.genfromtxt('dark/dark_3_4s.txt')

dark_4s_all = (np.array(dark_4s_1) + np.array(dark_4s_2) + np.array(dark_4s_3)) / 3

spectra_4s_1 = np.genfromtxt('xdata/x_1_4s.txt')
spectra_4s_2 = np.genfromtxt('xdata/x_2_4s.txt')
spectra_4s_3 = np.genfromtxt('xdata/x_3_4s.txt')

spectra_4s_all = (np.array(spectra_4s_1) + np.array(spectra_4s_2) + np.array(spectra_4s_3)) / 3


x1_4s = bk_4s_all[:,0]
y1_4s = bk_4s_all[:,1]

x2_4s = dark_4s_all[:,0]
y2_4s = dark_4s_all[:,1]

x3_4s = spectra_4s_all[:,0]
y3_4s = spectra_4s_all[:,1]

diff_4s = (spectra_4s_all[:,1] - (bk_4s_all[:,1] - dark_4s_all[:,1]) - dark_4s_all[:,1]) #y axis array

h1_4s = bk_4s_1[:,0]
k1_4s = bk_4s_1[:,1]

h2_4s = dark_4s_1[:,0]
k2_4s = dark_4s_1[:,1]

h3_4s = spectra_4s_1[:,0]
k3_4s = spectra_4s_1[:,1]

fig = plt.figure()
ax_4s = fig.add_subplot(1, 1, 1)

ax_4s.plot(x3_4s, y3_4s, color = 'blue')
ax_4s.plot(x2_4s, y2_4s, color = 'red')
ax_4s.plot(x1_4s, y1_4s, color = 'green')

ax_4s.plot(x1_4s, diff_4s, color = 'black')

#============interpolated hotdog

flux_q_lamp_matched = np.interp(quartz[:,0], quartz_multiplier[:,0], quartz_multiplier[:,1])
sensitivity = flux_q_lamp_matched / quartz[:,1]


hotdog_100_sensitivity = np.interp(hotdog_100_wavelength, quartz[:,0], sensitivity)
hotdog_140_sensitivity = np.interp(hotdog_140_wavelength, quartz[:,0], sensitivity)

fig = plt.figure(figsize=(12,6))

plt.subplot(121)
plt.plot(quartz[:,0], quartz[:,1], label='100 V')
plt.plot(hotdog_100_wavelength, hotdog_100_counts, label='100 V')
plt.plot(hotdog_140_wavelength, hotdog_140_counts, label='140 V')

plt.xlabel('Wavelength [$\lambda$]', fontsize = 20)
plt.ylabel('Counts', fontsize = 20)
plt.legend()

plt.subplot(122)
plt.plot(quartz[:,0], quartz[:,1]*hotdog_100_sensitivity)
plt.plot(hotdog_100_wavelength, hotdog_100_counts*hotdog_100_sensitivity)
plt.plot(hotdog_140_wavelength, hotdog_140_counts*hotdog_140_sensitivity)

plt.tight_layout()


#=============interpolated X_1s
#flux_q_lamp_matched = np.interp(quartz[:,0], quartz_multiplier[:,0], quartz_multiplier[:,1])
#sensitivity = flux_q_lamp_matched / quartz[:,1]

#projectx_sensitivity = np.interp(x1, quartz[:,0], sensitivity) #working set
projectx_sensitivity = np.interp(x1, quartz[:,0], sensitivity)


fig = plt.figure(figsize=(17,6))

plt.subplot(121)
#plt.plot(quartz[:,0], quartz[:,1], label='Quartz')
plt.plot(x1, diff, color='red')
plt.plot(x1_4s, diff_4s, color='blue')


plt.xlabel('Wavelength [$\lambda$]', fontname="Arial", fontsize = 18)
plt.ylabel('Counts', fontname="Arial", fontsize = 18)
plt.legend()

plt.minorticks_on()
plt.grid()


plt.subplot(122)


#plt.plot(wavelengths_hydrogen_2, counts_hydrogen_2*projectx_sensitivity, color = 'blue')
#plt.plot(wavelengths_mercury_2, counts_mercury_2*projectx_sensitivity, color = 'blue') #pretty good but lacks center emission line

#plt.plot(wavelengths_argon_2, counts_argon_2*projectx_sensitivity, color = 'blue')

#plt.plot(wavelengths_helium_2, counts_helium_2*projectx_sensitivity, color = 'blue')
#plt.plot(wavelengths_neon_2, counts_neon_2*projectx_sensitivity, color = 'blue') #not this
#plt.plot(wavelengths_mercury_2, counts_mercury_2*projectx_sensitivity, color = 'blue')

#==========
np.set_printoptions(formatter={'float_kind':'{:f}'.format}, threshold=np.inf)
combined_diff_1s = np.column_stack((x1,diff))


#print combined_diff_1s[:,0]
sec_array = np.column_stack([x1, diff*projectx_sensitivity])
max_sec_array = np.amax(sec_array[:,1])

reduced_sec_array = np.copy(sec_array[:,1])
toReplace = []
j=0
#print len(sec_array)
for i in range(len(reduced_sec_array)):
    if np.abs(reduced_sec_array[i] - reduced_sec_array[j]) > .088 :
        toReplace.append(i)
        print toReplace
    else:
        reduced_sec_array[toReplace] = (reduced_sec_array[j] + reduced_sec_array[i])/2
        toReplace = []
        j=i

combined_reduced_sec_array = np.column_stack([x1, reduced_sec_array])
#print combined_reduced_sec_array



#print combined_diff_1s[:,0]
sec_array_4s = np.column_stack([x1, diff_4s*projectx_sensitivity])
max_sec_array_4s = np.amax(sec_array_4s[:,1])

reduced_sec_array_4s = np.copy(sec_array_4s[:,1])
toReplace = []
j=0
#print len(sec_array)
for i in range(len(reduced_sec_array_4s)):
    if np.abs(reduced_sec_array_4s[i] - reduced_sec_array_4s[j]) > .062 :
        toReplace.append(i)
        print toReplace
    else:
        reduced_sec_array_4s[toReplace] = (reduced_sec_array_4s[j] + reduced_sec_array_4s[i])/2
        toReplace = []
        j=i

combined_reduced_sec_array_4s = np.column_stack([x1, reduced_sec_array_4s])

#==========


#plt.plot(quartz[:,0], quartz[:,1]*projectx_sensitivity)
plt.plot(x1, diff*projectx_sensitivity, color='red')
#plt.plot(x1, diff*projectx_sensitivity, color='red')

plt.plot(x1_4s, diff_4s*projectx_sensitivity, color='blue')
plt.plot(x1, reduced_sec_array, color='green')
plt.plot(x1, reduced_sec_array_4s, color='green')




plt.axvline(600, linestyle = '--', color = 'black')
plt.axvline(700, linestyle = '--', color = 'black')
plt.xlabel('Wavelength [$\lambda$]', fontname="Arial", fontsize = 18)
plt.ylabel('Normalized Counts', fontname="Arial", fontsize = 18)
plt.legend()

plt.minorticks_on()
plt.grid()

plt.tight_layout()
plt.savefig('counts.eps', format='eps', dpi=1000)

#=====================
fig = plt.figure(figsize=(18,6))
plt.subplot(121)

plt.xlabel('Wavelength [$\lambda$]', fontname="Arial", fontsize = 18)
plt.ylabel('Normalized Counts', fontname="Arial", fontsize = 18)

difference_cont_1s = abs((diff*projectx_sensitivity) - reduced_sec_array)
plt.plot(wavelengths_argon_2, counts_hydrogen_2/4500, color='green')
plt.plot(wavelengths_argon_2, counts_mercury_2/4500, color='purple')
plt.plot(wavelengths_argon_2, counts_argon_2/4500, color='orange')

plt.plot(x1, difference_cont_1s, color='red')
plt.minorticks_on()
plt.grid()
plt.legend()

plt.subplot(122)

plt.xlabel('Wavelength [$\lambda$]', fontname="Arial", fontsize = 18)
plt.ylabel('Normalized Counts', fontname="Arial", fontsize = 18)

plt.axvline(436.0, linestyle = '-', color = 'goldenrod')
plt.axvline(486.0, linestyle = '-', color = 'goldenrod')
plt.axvline(546.5, linestyle = '-', color = 'goldenrod')
plt.axvline(657.0, linestyle = '-', color = 'goldenrod')
#plt.axvline(664.0, linestyle = '-', color = 'yellow')
plt.axvline(763.5, linestyle = '-', color = 'goldenrod')
plt.axvline(801.0, linestyle = '-', color = 'goldenrod')
plt.axvline(811.5, linestyle = '-', color = 'goldenrod')
plt.axvline(842.5, linestyle = '-', color = 'goldenrod')
plt.axvline(912.5, linestyle = '-', color = 'goldenrod')

difference_cont_4s = abs((diff_4s*projectx_sensitivity) - reduced_sec_array_4s)
plt.plot(wavelengths_argon_2, counts_hydrogen_2/4500, color='green')
plt.plot(wavelengths_argon_2, counts_mercury_2/4500, color='purple')
plt.plot(wavelengths_argon_2, counts_argon_2/4500, color='orange')



plt.minorticks_on()
plt.grid()

plt.plot(x1, difference_cont_4s, color='blue')


plt.legend()
plt.savefig('emission.eps', format='eps', dpi=1000)


#plt.show()

#===============combining



#print sec_array
#print "The Initial Max is: ",max_sec_array
#print "Peak Wavelength: ",peak_region_wavelength





#================flux of centroid

#peak_region_wavelength = np.where((x1 >= 600) & (x1 <= 700))
#print peak_region_wavelength

'''
con_1s = np.column_stack([x1,reduced_sec_array])
#peak_region_wavelength = np.where((con_1s >= 600) & (con_1s <= 700))
#print peak_region_wavelength
#print con_1s

con_4s = np.column_stack([x1,reduced_sec_array_4s])
#print con_4s

diff_full = np.column_stack([x1, difference_cont_4s])

reduced_difference_cont_4s = np.copy(difference_cont_4s)
dCont_4s = []
j=0
#print len(sec_array)
for i in range(len(reduced_difference_cont_4s)):
    if np.abs(reduced_difference_cont_4s[i]) > .25 :
        dCont_4s.append(i)
        print dCont_4s
    else:
        pass
        #reduced_difference_cont_4s[dCont_4s] = (reduced_sec_array_4s[j] + reduced_sec_array_4s[i])/2
        #dCont_4s = []
        #j=i

#combined_reduced_sec_array_4s = np.column_stack([x1, reduced_sec_array_4s])


print "\n"
print x1[86]
print x1[136]
print x1[196]
print x1[197]
print x1[306]
print x1[307]
print x1[308]
print x1[314]
print x1[413]
print x1[414]
print x1[451]
print x1[461]
print x1[462]
print x1[492]
print x1[493]
print x1[562]
print x1[563]
'''



















#print len(x1)
#print len(diff)
#peak_region_flux = np.sum()




