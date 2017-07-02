'''
Compares brightness of a target star to a reference star within the same FITS image. Written for Lab 5, UHM ASTR300L Fall 2016.

v1.0: Oct 19, 2016
  *initial release
v1.1: Oct 30, 2016
  *fixed region plots
  *fixed flux uncertainties
  *modified output format for easier parsing

@author: devNull
'''
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits as fits
from astropy.coordinates import Angle,SkyCoord
from astropy import units as u
from astropy.wcs import WCS

# Constants
APERTURE = 20
APERTURE_BG = 30
TARGET_RA = Angle('16h14m20.3s').deg
TARGET_DEC = Angle('-19d06m48.1s').deg
REFERENCE_RA = Angle('16h14m20.912s').deg
REFERENCE_DEC = Angle('-19d06m04.70s').deg
REFERENCE_MAG = 13.5

# Parameters; if using published coordinates, xt, yt, xr, yr are ignored
#fileName = 'lsc1m004-fl04-20140622-0136-e90.fits'
fileName = 'lsc1m004-fl04-20140624-0138-e90.fits'


#fileName = 'cpt1m013-kb76-20140525-0146-e90.fits'
#fileName = 'coj1m003-kb71-20140607-0056-e90.fits'
#fileName = 'coj1m011-kb05-20140607-0113-e90.fits'

usePublished = False
#xt,yt = 1040,980
#xr,yr = 1065,870
#xb,yb = 900,560

xt,yt = 1060,975 #for second lsc file
#xt,yt = 1020,975
xr,yr = 1085,865
xb,yb = 920,555

# Function definitions
def centroid(arr):
    return np.nansum(arr*np.array(range(len(arr))))/np.nansum(arr)

def centroid2d(matrix):
    x = centroid(np.nansum(matrix,axis=0))
    y = centroid(np.nansum(matrix,axis=1))
    return x,y

# Read file
with fits.open(fileName) as hdulist:
    image = hdulist[0].data
    wcs = WCS(hdulist[0].header)
    gain = hdulist[0].header['GAIN']
    rdnoise = hdulist[0].header['RDNOISE']/gain     #digital
    julian = hdulist[0].header['MJD-OBS']

# Transform published RA/Dec to integer pixel coordinates
if usePublished:
    xt,yt = wcs.all_world2pix(TARGET_RA,TARGET_DEC,1)
    xt,yt = int(np.round(xt)), int(np.round(yt))
    xr,yr = wcs.all_world2pix(REFERENCE_RA,REFERENCE_DEC,1)
    xr,yr = int(np.round(xr)), int(np.round(yr))    

# Select regions
target = image[yt-APERTURE:yt+APERTURE, xt-APERTURE:xt+APERTURE]
reference = image[yr-APERTURE:yr+APERTURE, xr-APERTURE:xr+APERTURE]
background = image[yb-APERTURE_BG:yb+APERTURE_BG, xb-APERTURE_BG:xb+APERTURE_BG]

# Background; mean, uncertainty
m_bg = np.nanmean(background)
u_bg = np.nanstd(background)
um_bg = u_bg/np.sqrt(background.size)

# Target; corrected region, flux total, uncertainty
c_target = target - m_bg
f_target = np.nansum(c_target)
u_target = np.sqrt(np.nansum(target)/gain + target.size*(m_bg+rdnoise**2) + (target.size*um_bg)**2)

# Reference; corrected region, flux total, uncertainty
c_reference = reference - m_bg
f_reference = np.nansum(c_reference)
u_reference = np.sqrt(np.nansum(reference)/gain + reference.size*(m_bg+rdnoise**2) + (reference.size*um_bg)**2)

# Centroid; offset to original image pixels, then transformed to RA/Dec
xtc, ytc = centroid2d(c_target)
xtc += xt-APERTURE
ytc += yt-APERTURE
ra,dec = wcs.all_pix2world(xtc,ytc,1)

# Magnitude; relative to reference mag, uncertainty
mag = REFERENCE_MAG - 2.5*np.log10(f_target/f_reference)
u_mag = 2.5/np.log(10)*np.sqrt((u_target/f_target)**2+(u_reference/f_reference)**2)
#u_mag = np.sqrt( ((-2.5*u_target)/f_target)**2 + ((2.5*u_reference)/f_reference)**2 )


# Plots
fig = plt.figure()
plt.imshow(np.log10(image),'gray')
plt.show()

for region in [target,reference,background]:
    plt.contourf(np.log10(region))
    plt.gca().invert_yaxis()
    plt.grid(True)
    plt.show()

# Results; in units of instrument flux, need to multiply by gain for electrons
s_target = SkyCoord(ra=ra*u.deg, dec=dec*u.deg, frame='icrs').to_string('hmsdms')
date = hdulist[0].header['DATE']
print "Date: ",date

time = np.datetime64(date,'s')
unix = (time.astype(np.int64)).astype(np.int64)

print "UNIX Time: ",unix
print("Julian_date: {} Centroid: {}".format(julian, s_target))
print("Background_mean: {} +/- {}".format(m_bg, u_bg))
print("Target_flux: {} +/- {}".format(f_target, u_target))
print("Reference_flux: {} +/- {}".format(f_reference, u_reference))
print("Target_magnitude: {} +/- {}".format(mag,u_mag))