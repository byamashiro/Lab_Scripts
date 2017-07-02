from astropy import units as u
import numpy as np
from astropy import constants as const
import matplotlib.pyplot as plt
import scipy
from scipy import special

e_d = (4.5 * u.eV).cgs 
e_i = (13.6 * u.eV).cgs
mu = 1.0
omega = 3.0e39 * u.J

e_tot = ((const.M_sun/(2*const.m_p))*e_d) +((const.M_sun/(const.m_p))*e_i)
print "Total Energy: ", e_tot, e_tot.to(u.J)
#print e_d, e_i
#r_1 = 10.0**15 * u.meter
r_grav = (const.G * (const.M_sun**2))/e_tot


r_1 = const.R_sun

r_ps = (const.m_p * const.G * const.M_sun) * ((2./e_d) + (1./e_i)) + r_1
print "Method 1 Radius: ",(r_ps).si
print "M1 Radius Rsun: ",(r_ps/const.R_sun).si

print "Method 2 Radius: ",r_grav.si
print "M2 Radius Rsun: ",(r_grav/const.R_sun).si
print "M2 Approx Rsun: ",((3./5.)*(r_grav/const.R_sun)).si



T = ((mu * const.m_p)/(3.0 * const.k_B))*((const.G * const.M_sun)/r_ps)
print "Method 1 Temp: ",T.si

T_grav = ((mu * const.m_p)/(3.0 * const.k_B))*((const.G * const.M_sun)/r_grav)
print "Method 2 Temp:", T_grav.si

