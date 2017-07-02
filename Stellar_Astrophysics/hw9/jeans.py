from astropy import units as u
import numpy as np
from astropy import constants as const
import matplotlib.pyplot as plt
import scipy
from scipy import special

T = 10. * u.K
rho = 10.**(-22.) * u.g/u.cm**3
mu = 1.
print rho.unit

M_j = (((5.*const.k_B*T)/(2.*const.G*mu*(const.u)))**(3./2.)) * ((3./(4.*np.pi*rho))**(1./2.))
print M_j.cgs

print (M_j/const.M_sun).cgs