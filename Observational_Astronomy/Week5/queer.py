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


#from matplotlib import cm

#==============Full Image
fig = plt.figure(figsize=(18,6))
plt.subplot(121)

hdulist = fits.open('coj1m011-kb05-20140607-0113-e90.fits')

#hdulist = fits.open('coj1m003-kb71-20140607-0056-e90.fits')
#hdulist = fits.open('coj1m003-kb71-20140607-0059-e90.fits')
#hdulist = fits.open('cpt1m012-kb75-20140606-0200-e90.fits')
#hdulist = fits.open('cpt1m013-kb76-20140525-0146-e90.fits')
#hdulist = fits.open('cpt1m013-kb76-20140525-0176-e90.fits')
#hdulist = fits.open('elp1m008-kb74-20140606-0082-e90.fits')
#hdulist = fits.open('lsc1m004-fl04-20140622-0136-e90.fits')
#hdulist = fits.open('lsc1m004-fl04-20140624-0138-e90.fits')

hdulist.info()

image = hdulist[0].data
rotate_image = ndimage.rotate(image, 90)
inverted_image = rotate_image.T
header = hdulist[0].header

image
print header
exit(0)
#===========header data
x0 = header['CRPIX1'] - 1
y0 = header['CRPIX2'] - 1
ra0 = header['CRVAL1']
dec0 = header['CRVAL2']
rnoise = header['RDNOISE']

CD1_1 = header['CD1_1']
CD2_2 = header['CD2_2']


#========================

n_imrows = np.shape(inverted_image)[0]
n_imcols = np.shape(inverted_image)[1]



plt.imshow(inverted_image)
np.min(inverted_image), np.mean(inverted_image), np.max(inverted_image)

showIm = np.log10(inverted_image)
#showIm = image
plt.imshow(showIm,'gray')
np.min(showIm), np.mean(showIm), np.max(showIm)

showIm = np.log10(inverted_image - np.mean(inverted_image))
#showIm = (image - np.mean(image))
plt.imshow(showIm,'gray')
print "total: ", np.mean(inverted_image)

fi = plt.contourf(showIm,5)
plt.colorbar(fi)

print "=================Total Image================"
print "Photons: ",np.max(inverted_image)
print "Mean Photons: ",np.mean(inverted_image)
print "Median: ",np.median(inverted_image)
print "Standard Dev: ",np.std(inverted_image)
plt.minorticks_on()
plt.grid()
#plt.show()

#==============Background
plt.subplot(122)

indices = np.indices((n_imrows, n_imcols))
xs_bk = indices[1,:]
ys_bk = indices[0,:]

#background = image[850:1000, 1040:1100] #y, x OLD BACKGROUND

#RA/Dec coords: 16h14m17.0692s -19d05m50.3571s

ra_true_bk = Angle('16h14m17.0692s').deg
dec_true_bk = Angle('-19d05m50.3571s').deg

ra_conv_bk = (ra_true_bk - ra0)/CD1_1 + x0
dec_conv_bk = (dec_true_bk - dec0)/CD2_2 + y0

background = inverted_image[dec_conv_bk-30:dec_conv_bk+30, ra_conv_bk-30:ra_conv_bk+30]


#target_bk_xs = xs_bk[850:1000, 1040:1100]
#target_bk_ys = ys_bk[850:1000, 1040:1100]
#target_bk_xs, target_bk_ys

#target_x = np.sum(region_app * target_xs) / np.sum(region_app)
#target_y = np.sum(region_app * target_ys) / np.sum(region_app)

#ra_bk = CD1_1 * (1070 - x0) + ra0
#dec_bk = CD2_2 * (925 - y0) + dec0
#print ra_bk, dec_bk

#==============Degree to sexagesimal

#c_bk = SkyCoord(ra=ra_bk*u.degree, dec=dec_bk*u.degree, frame='icrs')
#c_bk.to_string('hmsdms')
#print "BG RA/Dec: ",c_bk.to_string('hmsdms')








showIm = np.log10(background)
plt.imshow(showIm,'gray')

dims_bk = np.shape(background)
n_bk = dims_bk[0] * dims_bk[1]
mean_bk = np.mean(background)
sigma_bk = np.std(background)
sigma_mean_bk = np.std([mean_bk])

print "=================Background================"
print "Number of Pixels", n_bk
print "Mean", mean_bk
print "Standard Deviation", sigma_bk


cbkg = plt.contourf(showIm,10)
plt.colorbar(cbkg)
plt.minorticks_on()
plt.grid()
plt.show()

#exit(0)
#==============Target Region
'''
fig = plt.figure(figsize=(18,6))
plt.subplot(121)


target = image[1030:1070, 945:985]
showIm = np.log10(target)
showIm = np.log10(target/mean_bk)
plt.imshow(showIm,'gray')
dims_tg = np.shape(target)
n_tg = dims_tg[0] * dims_tg[1]
sum_tg = np.sum(target)

cp = plt.contourf(showIm,900)
plt.colorbar(cp)

#plt.show()
'''

#==============Centroid

ra_true = Angle('16h14m20.3s').deg
dec_true = Angle('-19d06m48.1s').deg

ra_standard_true = Angle('16h14m20.912s').deg
dec_standard_true = Angle('-19d06m04.70s').deg

ra_conv = (ra_true - ra0)/CD1_1 + x0
dec_conv = (dec_true - dec0)/CD2_2 + y0

ra_standard_conv = (ra_standard_true - ra0)/CD1_1 + x0
dec_standard_conv = (dec_standard_true - dec0)/CD2_2 + y0

r_app = 20
#region_app = image[target_y-r_app:target_y+r_app, target_x-r_app:target_x+r_app]
region_app = inverted_image[dec_conv-r_app:dec_conv+r_app, ra_conv-r_app:ra_conv+r_app]
region_standard_app = inverted_image[dec_standard_conv-r_app:dec_standard_conv+r_app, ra_standard_conv-r_app:ra_standard_conv+r_app]

indices = np.indices((n_imrows, n_imcols))
xs = indices[1,:]
ys = indices[0,:]

target_xs = xs[1030:1070, 945:985]
target_ys = ys[1030:1070, 945:985]
target_xs, target_ys

target_x = np.sum(region_app * target_xs) / np.sum(region_app)
target_y = np.sum(region_app * target_ys) / np.sum(region_app)

ra = CD1_1 * (target_x - x0) + ra0
dec = CD2_2 * (target_y - y0) + dec0
#print ra, dec

#==============Degree to sexagesimal

c = SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='icrs')
c.to_string('hmsdms')
print "initial: ",c.to_string('hmsdms')



#print "True ra: ",ra_conv
#print "Ture dec: ",dec_conv

fig = plt.figure(figsize=(18,6))
plt.subplot(121)

showIm = np.log10(region_app)
plt.imshow(showIm,'gray')
dims_tg = np.shape(region_app)
n_tg = dims_tg[0] * dims_tg[1]
sum_tg = np.sum(region_app)

r_a = plt.contourf(showIm,10) #900
plt.colorbar(r_a)
plt.minorticks_on()
plt.grid()
#plt.show() #ucomment later
#==============gain


gain = header['GAIN']

sum_gain = sum_tg * gain
back_gain = mean_bk * gain
std_gain = sigma_bk * gain
back = n_tg * back_gain
sigma_mean_bk_gain = sigma_mean_bk * gain

#jamesphoton = (region_app - mean_bk)*gain
#jamesphoton2 = np.sum(jamesphoton)



nPhotons = sum_gain - back
errPhotons = np.sqrt(nPhotons)
uncertPhotons = np.sqrt(np.sum((region_app.size/gain) + ((rnoise**2)/(gain**2))) + ((region_app.size**2)*(std_gain**2)))
#u_target = np.sqrt(np.nansum(region_app)/gain + (region_app.size*std_gain)**2)
true_uncertPhotons = np.sqrt((nPhotons/gain) + (region_app.size*(back_gain+rnoise**2)) + ((region_app.size**2)*(sigma_mean_bk_gain**2)))

print "=================Centroid================"
centroid_xs = xs[dec_conv-r_app:dec_conv+r_app, ra_conv-r_app:ra_conv+r_app]
centroid_ys = ys[dec_conv-r_app:dec_conv+r_app, ra_conv-r_app:ra_conv+r_app]

centroid_x = np.sum(region_app * centroid_xs) / np.sum(region_app)
centroid_y = np.sum(region_app * centroid_ys) / np.sum(region_app)

ra_centroid = CD1_1 * (centroid_x - x0) + ra0
dec_centroid = CD2_2 * (centroid_y - y0) + dec0

ra_dec_centroid = SkyCoord(ra=ra_centroid*u.degree, dec=dec_centroid*u.degree, frame='icrs')
ra_dec_centroid.to_string('hmsdms')
#print "RA/Dec: ",ra_dec_centroid.to_string('hmsdms')
print "Number of Photons: ",nPhotons ,"+/-", true_uncertPhotons,"+/-", uncertPhotons
#print "James Flux: ",jamesphoton2
#print "RN Uncert: ",uncertPhotons
#print "James Uncert: ",u_target
print "Final Minimum: ", np.min(showIm)
print "Final Mean: ", np.mean(showIm)
print "Final Maximum: ", np.max(showIm)



#exit(0)
#================standard

plt.subplot(122)

showIm = np.log10(region_standard_app)
plt.imshow(showIm,'gray')
dims_tg_st = np.shape(region_standard_app)
n_tg_st = dims_tg_st[0] * dims_tg_st[1]
sum_tg_st = np.sum(region_standard_app)

r_a_standard = plt.contourf(showIm,10) #900
plt.colorbar(r_a_standard)

plt.minorticks_on()
plt.grid()
plt.show()
#==============gain


gain = header['GAIN']

sum_gain_st = sum_tg_st * gain
back_gain_st = mean_bk * gain
std_gain_st = sigma_bk * gain

back_st = n_tg_st * back_gain_st
nPhotons_st = sum_gain_st - back_st
errPhotons_st = np.sqrt(nPhotons_st)
uncertPhotons_st = np.sqrt(np.sum((region_standard_app.size/gain) + ((rnoise**2)/(gain**2))) + ((region_standard_app.size**2)*(std_gain_st**2)))
true_uncertPhotons_st = np.sqrt((nPhotons_st/gain) + (region_standard_app.size*(back_gain+rnoise**2)) + ((region_standard_app.size**2)*(sigma_mean_bk_gain**2)))


print "=================Standard================"
standard_xs = xs[dec_standard_conv-r_app:dec_standard_conv+r_app, ra_standard_conv-r_app:ra_standard_conv+r_app]
standard_ys = ys[dec_standard_conv-r_app:dec_standard_conv+r_app, ra_standard_conv-r_app:ra_standard_conv+r_app]

standard_x = np.sum(region_standard_app * standard_xs) / np.sum(region_standard_app)
standard_y = np.sum(region_standard_app * standard_ys) / np.sum(region_standard_app)

ra_standard = CD1_1 * (standard_x - x0) + ra0
dec_standard = CD2_2 * (standard_y - y0) + dec0

ra_dec_standard = SkyCoord(ra=ra_standard*u.degree, dec=dec_standard*u.degree, frame='icrs')
ra_dec_standard.to_string('hmsdms')
print "RA/Dec: ",ra_dec_standard.to_string('hmsdms')

print "Number of Photons: ",nPhotons_st ,"+/-", uncertPhotons_st ,"+/-", true_uncertPhotons_st
print "Final Minimum: ", np.min(showIm)
print "Final Mean: ", np.mean(showIm)
print "Final Maximum: ", np.max(showIm)

#========================Magnitude calculations

print "=================Final Values==============="
Mag = (-2.5 * np.log10(nPhotons/nPhotons_st)) + 13.5
Mag_err = np.sqrt( ((-2.5*uncertPhotons)/nPhotons)**2 + ((2.5*uncertPhotons_st)/nPhotons_st)**2 )

print "Flux (Star): ",nPhotons ,"+/-", uncertPhotons,"+/-", true_uncertPhotons
print "RA/Dec (Star): ",ra_dec_centroid.to_string('hmsdms')
print "------------------------------------"
print "Flux (Standard): ",nPhotons_st ,"+/-", uncertPhotons_st ,"+/-", true_uncertPhotons_st
print "RA/Dec (Standard): ",ra_dec_standard.to_string('hmsdms')
print "------------------------------------"
print "Magnitude (Star): ",Mag,"+/-",Mag_err
