from astropy.io import fits
import numpy as np

#hdulist = fits.open('ktwo211351816-c05_llc.fits')
#hdulist.info()
#hdu = hdulist[0]
#
##hdu.data.shape
#
#hdu.header
#plt.imshow(hdu.data[0,:,:], origin='lower')
#



from astropy.io import fits
from astropy.table import Table
data = fits.getdata('ktwo211351816-c05_llc.fits', 1)
t = Table(data)
print data.header
#print data
print t


