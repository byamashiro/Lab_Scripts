# make a list of file names of .fits files
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

import os
files = os.listdir('.')
fitsFiles = []
for i in np.arange(0,len(files),1):
	if '.fits' in files[i]:
		fitsFiles.append(files[i])
#print fitsFiles
#exit(0)

#scale the image to nicely show a narow range of values

hdulist = fits.open('aug28_dark_001_03.chip01.fits')
#hdulist = fits.open('aug28_dark_001_05.chip01.fits')
#hdulist = fits.open('aug28_dark_001_07.chip01.fits')
#hdulist = fits.open('aug28_dark_001_08.chip01.fits')
#hdulist = fits.open('aug28_dark_001_09.chip01.fits')

#hdulist = fits.open('o6601g0218d.ota33.034.fits')

hdulist.info()
image = hdulist[0].data
header = hdulist[0].header
#print header
#exit(0)

showIm = np.log10(image - np.min(image)+1)
plt.imshow(showIm,'gray')

cbkg = plt.contourf(showIm,30)
plt.xlabel('Pixels', fontname="Arial", fontsize = 16)
plt.ylabel('Pixels', fontname="Arial", fontsize = 16)
#plt.colorbar(cbkg)
plt.colorbar(cbkg).set_label(label='Contour Levels',size=16) #,weight='bold')

plt.show()
exit(0)



'''
darkTimes = np.zeros(len(fitsFiles))
image = np.zeros(len(fitsFiles))
temp = np.zeros(len(fitsFiles))
exptime = np.zeros(len(fitsFiles))
darkMean = np.zeros(len(fitsFiles))

print darkTimes
darkTelescopes = [None]*len(fitsFiles)
for i in np.arange(0,len(fitsFiles),1):
    hdulist = fits.open(fitsFiles[i])
    dark = hdulist[0].data
    darkHeader = hdulist[0].header
    hdulist.close()
    darkMean[i] = np.mean(dark)
    darkTimes[i] = darkHeader['DARKTIME']
    darkTelescopes[i] = darkHeader['TELESCOP']
    temp[i] = darkHeader['CCDTEMP']
    exptime[i] = darkHeader['EXPTIME']

print "Mean counts:",darkMean
print "Temp.: ",temp
print "Dark Times: ",darkTimes
print "Telescope: ", darkTelescopes
'''

'''

#-------------Useless crap

	#seqid[i] = darkHeader['SEQID']    
    #gain[i] = darkHeader['GAIN']
    #readnoise[i] = darkHeader['RDNOISE']
    #print i,seqid[i],darkTimes[i],darkTelescopes[i],gain[i],readnoise[i]




# print a table of values from the images and headers
for i in np.arange(0,len(temps),1):

    print i,times[i],temps[i],means[i],stds[i],telescopes[i]


# examine signal vs. CCDTemp
fig = plt.figure()
plt.plot(temps[0:4],means[0:4],'bo',label='ISP-1')
plt.plot(temps[5:14],means[5:14],'kv',label='PS1')
plt.xlabel(r'CCD Temperature [C]', fontsize=20)
plt.ylabel(r'Mean Counts', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
plt.xlim(-75,-50)
plt.ylim(7790,7890)

'''

