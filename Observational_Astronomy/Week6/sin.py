import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi

from astropy.stats import sigma_clip
from numpy import mean


#data = np.genfromtxt('212173112.dat')
#function = sin(x)
'''
time = np.array(data[:,0])
flux = np.array(data[:,1])

fft_flux = fft(flux)

#N = len(flux)
#df = 1. / (N * dt)
#PSD = abs(dt * fftpack.fft(flux)[:N / 2]) ** 2
#f = df * np.arange(N / 2) 

>>> signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)
>>> fourier = np.fft.fft(signal)
>>> n = signal.size
>>> timestep = 0.1
>>> freq = np.fft.fftfreq(n, d=timestep)
>>> freq


#signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)
fourier = np.fft.fft(time)
n = time.size
timestep = 0.02043198
freq = np.fft.fftfreq(n, d=timestep)
#freq

max_flux = np.max(abs(fft_flux))
print "Max Flux: ",max_flux
print fft_flux



print time, flux

#fig = plt.figure()
#dx = fig.add_subplot(1, 1, 1)

fig = plt.figure(figsize=(18,6))

plt.subplot(121)
ax2.plot(t, sin(2*2*pi*t))

plt.plot(time, flux, color = 'blue')
plt.xlabel('Time [days]', fontname="Arial", fontsize = 14)
plt.ylabel('Flux', fontname="Arial", fontsize = 14)
#plt.legend()

plt.minorticks_on()
plt.grid()

plt.subplot(122)

plt.plot(abs(freq), abs(fft_flux), color = 'blue')
plt.xlabel('Frequency [1/days]', fontname="Arial", fontsize = 14)
plt.ylabel('Power', fontname="Arial", fontsize = 14)
#plt.legend()

plt.minorticks_on()
plt.grid()
plt.xscale('log')

plt.show()

'''
'''
t = arange(0.0, 1.0, 0.01)

fig = figure(1)

ax1 = fig.add_subplot(211)
ax1.plot(t, sin(2*pi*t))
ax1.grid(True)
ax1.set_ylim((-2, 2))
ax1.set_ylabel('1 Hz')
ax1.set_title('A sine wave or two')

for label in ax1.get_xticklabels():
    label.set_color('r')


ax2 = fig.add_subplot(212)
ax2.plot(t, sin(2*2*pi*t))
ax2.grid(True)
ax2.set_ylim((-2, 2))
l = ax2.set_xlabel('Hi mom')
l.set_color('g')
l.set_fontsize('large')

'''
Fs = 150.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = np.arange(0,2*np.pi,Ts) # time vector

#ff = (38/20)*np.pi;   # frequency of the signal
ff = np.pi
y = np.sin(((2*np.pi)*ff*t)) / t

#y = np.sin(((2*np.pi)*ff*t)) + np.sin((2*(2*np.pi)*ff*t))
#y = np.sin((4*(2*np.pi)*ff*t) + np.pi)
#y = 2*np.sin((2*(2*np.pi)*ff*t)) + 4*np.sin((4*(2*np.pi)*ff*t)) + 3*np.cos((5*(2*np.pi)*ff*t) + np.pi)
#y = 1 + np.sin(((2*np.pi)*ff*t)) +2*np.cos(((2*np.pi)*ff*t)) + np.cos((2*(2*np.pi)*ff*t) + np.pi/4)

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(n/2)] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(n/2)]

fig, ax = plt.subplots(2, 1)
ax[0].set_title('1+sin($\omega_1$t)+2cos($\omega_1$t)+cos(2$\omega_1$t + $\pi$/4)')
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('Amplitude')


show()

