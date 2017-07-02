from astropy import units as u
from astropy.units import imperial as imp
#import astropy.units as u
import numpy as np
from astropy import constants as const
import matplotlib.pyplot as plt
import scipy
from scipy import special

mu_e = 1.5
mu = 0.85
k_1 = 1.00*10.0**7.0
k_2 = 1.24*10.0**11.0

rho = np.arange(10**(-9),10**9,1000.)
rho_non = np.arange(10**(-9),2.89467*10**6,1000.)
rho_rel = np.arange(2.89467*10**6,10**9,1000.)
#temp = np.arange(3,12,0.01)

inner_rho = (rho / mu_e)
inner_rho_non = (rho_non / mu_e)
inner_rho_rel = (rho_rel / mu_e)


T_1 = (((3.0 * const.c * const.k_B * rho)/(4.0 * const.sigma_sb * mu * const.u))**(1./3.)).cgs

#using book approximation (proportionality so ignore this case)
#T_2 = ((mu/(rho * const.k_B))*((rho/mu_e)**(5.0/3.0))).cgs
#T_3 = ((mu/(rho * const.k_B))*((rho/mu_e)**(4.0/3.0))).cgs

#online constants used to derive
#T_2 = k_1 * (rho**(5./3.))
#T_3 = k_2 * (rho**(4./3.))

#online constants used to derive
#T_2 = k_1 * (rho**(5./3.))
#T_3 = k_2 * (rho**(4./3.))

#slide constants
#T_2 = (10.0**13.0)*((rho/mu_e)**(5.0/3.0))
#T_3 = (1.245*(10.0**15.0))*((rho/mu_e)**(4.0/3.0))

T_2 = ((mu * const.u * (10.0**13.0) * (inner_rho_non ** (5.0/3.0)) ) / (rho_non * const.k_B)).cgs
T_3 = ((mu * const.u * (1.245*(10.0**15.0)) * (inner_rho_rel ** (4.0/3.0)) ) / (rho_rel * const.k_B)).cgs


#idx = np.argwhere(np.diff(np.sign(T_3 - T_2)) != 0).reshape(-1) + 0



plt.plot(rho, T_1, color='blue', linewidth = 3)
plt.plot(rho_non, T_2,  color='red', linewidth = 3)
plt.plot(rho_rel, T_3, color='green', linewidth = 3)

#idx = np.argwhere(np.isclose(T_2, T_3, atol=0.1)).reshape(-1)
#plt.plot(rho[idx], T_3[idx], 'ro')
#ax1.axvline(goes_proton_time[max_index], color='black', linewidth=1)
plt.vlines(x=2.89467*10.0**6.0, ymin = 0, ymax = 1*10.0**9.0, color='purple', linewidth = 3)
plt.axvline(x=150, ymin=0, ymax=10., hold=None,linestyle = '-.', color='orange')
plt.axhline(y=15000000.0, hold=None,linestyle = '-.', color='orange')
plt.plot(150, 15000000.0, 'ob')


#plt.plot(lambda_queue, d_gaussian, color='red')
plt.xlabel(r'log($ \rho $)', fontname="Arial", fontsize = 14)
plt.ylabel('log(T)', fontname="Arial", fontsize = 14)
plt.minorticks_on()
plt.ylim([10**3,10**12])
plt.xlim([10**(-9),10**(9)])
plt.grid(True)
plt.yscale('log')
plt.xscale('log')

plt.savefig('plot.pdf', format='pdf', dpi=900)

plt.show()


