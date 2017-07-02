import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from tempfile import TemporaryFile



from astropy.stats import sigma_clip
from numpy import mean

data = np.genfromtxt('212173112.dat')
'''
hdulist.info()

#image = hdulist[0].data
#rotate_image = ndimage.rotate(image, 90)
#inverted_image = image.T
header = hdulist[0].header
image
print header
exit(0)
'''
time = np.array(data[:,0])
flux = np.array(data[:,1])

fft_flux = fft(flux)

#N = len(flux)
#df = 1. / (N * dt)
#PSD = abs(dt * fftpack.fft(flux)[:N / 2]) ** 2
#f = df * np.arange(N / 2) 
'''
>>> signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)
>>> fourier = np.fft.fft(signal)
>>> n = signal.size
>>> timestep = 0.1
>>> freq = np.fft.fftfreq(n, d=timestep)
>>> freq
'''

#signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)
fourier = np.fft.fft(time)
n = time.size
timestep = 0.02043198
freq = np.fft.fftfreq(n, d=timestep)
#freq

max_flux = np.max(abs(fft_flux))
#print "Max Flux: ",max_flux
#print fft_flux



#print time, flux

#fig = plt.figure()
#dx = fig.add_subplot(1, 1, 1)

fig = plt.figure(figsize=(18,6))

plt.subplot(121)

plt.plot(time, flux, color = 'blue')
plt.xlabel('Time [days]', fontname="Arial", fontsize = 14)
plt.ylabel('Flux', fontname="Arial", fontsize = 14)
#plt.legend()

plt.minorticks_on()
plt.grid()


#fig = plt.figure(figsize=(18,6))

plt.subplot(122)

plt.plot(abs(freq), abs(fft_flux), color = 'blue')
plt.xlabel('Frequency [1/days]', fontname="Arial", fontsize = 14)
plt.ylabel('Power', fontname="Arial", fontsize = 14)
#plt.legend()

plt.minorticks_on()
plt.grid()
plt.xscale('log')

plt.show()






a = np.array([abs(freq)])
b = np.array([abs(fft_flux)])

totaldata = np.concatenate((a,b))
print totaldata

#np.savetxt('test.out', (a,b), delimiter='	')
'''
outfile = TemporaryFile()
np.savez(final.dat, x=a, y=b)
outfile.seek(0)
npzfile = np.load(outfile)
npzfile.files
['y', 'x']
'''


