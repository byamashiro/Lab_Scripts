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

hdulist = fits.open('J1614-1906_obs/science1.fits') #coj1m011-kb05-20140607-0113-e00.fits')
#sciimg = hdulist[].data
header = hdulist[1].header

#print header
#exit(0)


hdulist = fits.open('J1614-1906_obs/bias1.fits')
bias_1 = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/bias2.fits')
bias_2 = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/bias3.fits')
bias_3 = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/bias4.fits')
bias_4 = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/bias5.fits')
bias_5 = hdulist[1].data



hdulist = fits.open('J1614-1906_obs/dark_20s_1.fits')
hdulist.info()
dark1_20s = hdulist[1].data
darkHeader_20s = hdulist[1].data
#plt.imshow(dark1_20s)
#plt.show()
#print darkHeader
#print np.mean(dark1), np.nanmean(dark1)
#print np.std(dark1), np.nanstd(dark1)
#print np.max(dark1), np.nanmax(dark1)
#print np.min(dark1), np.nanmin(dark1)
#print np.shape(dark1)


#Calculating the median image from a set of images:
#  Load each image separately

hdulist = fits.open('J1614-1906_obs/dark_20s_1.fits')
dark1_20s = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/dark_20s_2.fits')
dark2_20s = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/dark_20s_3.fits')
dark3_20s = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/dark_20s_4.fits')
dark4_20s = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/dark_20s_5.fits')
dark5_20s = hdulist[1].data


#  Stack the images together
darkStack_20s = np.dstack([dark1_20s, dark2_20s, dark3_20s, dark4_20s, dark5_20s])
sciDarkImage_20s = np.median(darkStack_20s,axis=2)

#Save your images as .fits files so you don't have to re-calculate every step:

#newHDU = fits.CompImageHDU(sciDarkImage_20s, darkHeader_20s)
#newHDU.writeto('science_dark.fits', clobber=True)


#Sum the counts for the target within an aperture (box) around a central pixel
#targetColumn, targetRow = 977, 1058 
#targCounts = np.nansum(sciFlattened[targetRow-aperture:targetRow+aperture,targetColumn-aperture:targetColumn+aperture]) - aperture**2 * backgroundMean



#Flat image

hdulist = fits.open('J1614-1906_obs/flat_1.fits')
flat1 = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/flat_2.fits')
flat2 = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/flat_3.fits')
flat3 = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/flat_4.fits')
flat4 = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/flat_5.fits')
flat5 = hdulist[1].data

flatStack = np.dstack([flat1, flat2, flat3, flat4, flat5])
sciFlatImage = np.median(flatStack,axis=2)

hdulist = fits.open('J1614-1906_obs/dark_09s_1.fits')
dark1_9s = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/dark_09s_2.fits')
dark2_9s = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/dark_09s_3.fits')
dark3_9s = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/dark_09s_4.fits')
dark4_9s = hdulist[1].data
hdulist = fits.open('J1614-1906_obs/dark_09s_5.fits')
dark5_9s = hdulist[1].data

darkStack_9s = np.dstack([dark1_9s, dark2_9s, dark3_9s, dark4_9s, dark5_9s])
sciDarkImage_9s = np.median(darkStack_9s,axis=2)

norm_flat = (sciFlatImage - sciDarkImage_9s)/(np.mean(sciFlatImage - sciDarkImage_9s)) # 9s integration time
#print norm_flat

#newHDU = fits.CompImageHDU(sciFlatImage, darkHeader)
#newHDU.writeto('science_flat.fits', clobber=True)



#Science image


#======================old image begin
fig = plt.figure(figsize=(18,6))
plt.subplot(121)


hdulist = fits.open('old/coj1m011-kb05-20140607-0113-e90.fits')
hdulist.info()

image = hdulist[0].data


n_imrows = np.shape(image)[0]
n_imcols = np.shape(image)[1]



plt.imshow(image)
np.min(image), np.mean(image), np.max(image)

showIm = np.log10(image)
#showIm = image
plt.imshow(showIm,'gray')
np.min(showIm), np.mean(showIm), np.max(showIm)

showIm = np.log10(image - np.mean(image))
#showIm = (image - np.mean(image))
plt.imshow(showIm,'gray')
print "total: ", np.mean(image)

fi = plt.contourf(showIm,256)
plt.xlabel('Pixels', fontname="Arial", fontsize = 16)
plt.ylabel('Pixels', fontname="Arial", fontsize = 16)

#plt.colorbar(fi)
plt.colorbar(fi).set_label(label='Contour Levels',size=16)


print "=================Total Image================"
print "Photons: ",np.max(image)
print "Mean Photons: ",np.mean(image)
print "Median: ",np.median(image)
print "Standard Dev: ",np.std(image)
plt.minorticks_on()
plt.grid()


#=======================Old image end
plt.subplot(122)

hdulist = fits.open('J1614-1906_obs/science1.fits') #coj1m011-kb05-20140607-0113-e00.fits')
sciimg = hdulist[1].data

sciimg_nd = (sciimg) - sciDarkImage_20s
pure_sciimg = sciimg_nd / norm_flat

print np.min(pure_sciimg), np.max(pure_sciimg), np.mean(pure_sciimg), np.std(pure_sciimg)


#showIm = np.log10(pure_sciimg - np.mean(pure_sciimg))
showIm=(pure_sciimg)
plt.imshow(showIm,'gray', clim=(10, 500))

#showIm = (image - np.mean(image))

#fi = plt.contourf(showIm,6, clim=(10, 500))
plt.xlabel('Pixels', fontname="Arial", fontsize = 16)
plt.ylabel('Pixels', fontname="Arial", fontsize = 16)
#plt.colorbar(fi).set_label(label='Contour Levels',size=16)

plt.minorticks_on()

plt.grid()



plt.show()
#exit(0)
#==========aperture


background = pure_sciimg[850:1000, 1040:1100]
showIm = background
cbkg = plt.contourf(showIm,256)
plt.xlabel('Pixels', fontname="Arial", fontsize = 16)
plt.ylabel('Pixels', fontname="Arial", fontsize = 16)
#plt.colorbar(cbkg)
plt.colorbar(cbkg).set_label(label='Contour Levels',size=16) #,weight='bold')
plt.show()


fig = plt.figure(figsize=(18,6))
plt.subplot(121)

aperture = 20
targetColumn, targetRow = 977, 1058
targCounts = np.nansum(pure_sciimg[targetRow-aperture:targetRow+aperture,targetColumn-aperture:targetColumn+aperture]) - (aperture**2 * np.mean(background))

target = pure_sciimg[targetRow-aperture:targetRow+aperture,targetColumn-aperture:targetColumn+aperture] 

showIm = np.log10(target)
#plt.imshow(showIm,'gray')
cbkg = plt.contourf(showIm,256)
plt.xlabel('Pixels', fontname="Arial", fontsize = 16)
plt.ylabel('Pixels', fontname="Arial", fontsize = 16)
#plt.colorbar(cbkg)
plt.colorbar(cbkg).set_label(label='Contour Levels',size=16) #,weight='bold')

plt.minorticks_on()

plt.grid()
#plt.show()

#========standard
plt.subplot(122)

hdulist = fits.open('J1614-1906_obs/science1.fits') #coj1m011-kb05-20140607-0113-e00.fits')
#sciimg = hdulist[].data
header = hdulist[1].header
x0 = header['CRPIX1'] - 1
y0 = header['CRPIX2'] - 1
ra0 = header['CRVAL1']
dec0 = header['CRVAL2']
#rnoise = header['RDNOISE']
CD1_1 = header['CD1_1']
CD2_2 = header['CD2_2']


ra_standard_true = Angle('16h14m20.912s').deg
dec_standard_true = Angle('-19d06m04.70s').deg
ra_standard_conv = (ra_standard_true - ra0)/CD1_1 + x0
dec_standard_conv = (dec_standard_true - dec0)/CD2_2 + y0
r_app = 20
region_standard_app = image[dec_standard_conv-r_app+25:dec_standard_conv+r_app+25, ra_standard_conv-r_app-58:ra_standard_conv+r_app-58]

targCounts_standard = np.nansum(region_standard_app ) - (aperture**2 * np.mean(background))
#true_uncertPhotons_st = np.sqrt((region_standard_app) + (region_standard_app.size) + ((region_standard_app.size**2)*(background**2)))


showIm = np.log10(region_standard_app)
#plt.imshow(showIm,'gray')
cbkg_1 = plt.contourf(showIm,256)
sum_tg_st = np.sum(region_standard_app)
r_a_standard = plt.contourf(showIm,256) #900
plt.xlabel('Pixels', fontname="Arial", fontsize = 16)
plt.ylabel('Pixels', fontname="Arial", fontsize = 16)
#plt.colorbar(r_a_standard)
plt.colorbar(cbkg_1).set_label(label='Contour Levels',size=16)

plt.minorticks_on()
plt.grid()

plt.show()

#=======Data
hdulist = fits.open('J1614-1906_obs/science1.fits') #coj1m011-kb05-20140607-0113-e00.fits')
#sciimg = hdulist[].data
header = hdulist[1].header
star = hdulist[1].header['GROUPID']
date = hdulist[1].header['DATE-OBS']

print "============Final Values=============="

print "Object: ", star
print "Date: ",date
print "Target Counts: ", targCounts
print "Standard Counts", targCounts_standard#, "+/-", true_uncertPhotons_st

print "============Background=============="

print "BKG Mean: ",np.mean(background)
print "BKG Counts", np.nansum(background)
print "BKG Standard Deviation: ",np.std(background)

print "============Magnitude=============="
Mag = (-2.5 * np.log10(targCounts/targCounts_standard)) + 13.5
print "Magnitude (Star): ",Mag#,"+/-",Mag_err_new












