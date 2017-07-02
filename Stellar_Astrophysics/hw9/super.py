from astropy import units as u
import numpy as np
from astropy import constants as const
from scipy import constants as sciconst

import matplotlib.pyplot as plt
import scipy
from scipy import special
from scipy.optimize import curve_fit

#===========Problem 1
ns_rad = 13.0 * u.km
ns_mass = 1.5 * const.M_sun
gravity = (const.G * ns_mass)/(ns_rad**2.0)
#print gravity
#pot_e_1 = ns_mass * gravity * ns_rad
pot_e_2 = (const.G * (ns_mass**2.0))/ns_rad
print 'Total Energy: ',pot_e_2.to(u.erg)

e_lum = (35000.0*const.L_sun) * (6000000.0 * u.year)
print e_lum.to(u.erg)

e_rel = (1.0/2.0)*(12.0*const.M_sun)*((10000.0*(u.km/u.second))**2.0)

print e_rel.to(u.erg)

#===========Problem 2

v_esc_a = np.sqrt((2.0*const.G*const.M_sun)/const.R_earth).to(u.km/u.second)
v_esc_b = np.sqrt((2.0*const.G*(1.5*const.M_sun))/(13.0 * u.km)).to(u.km/u.second)

print v_esc_a, v_esc_b

v_wd = (2.0 * np.pi * (2.0/(1.0*u.second))) * const.R_earth

print v_wd.to(u.km/u.s)

v_ns =  (2.0 * np.pi * (100.0/(1.0*u.second))) * (13.0 * u.km)
print 'velocity: ', v_ns.to(u.km/u.s)

#v_ns = (2.0 * np.pi * (2142.8014/(1.0*u.second))) * (13.0 * u.km)
print 'tester (175027.042816): ',v_ns.to(u.km/u.s)

freq = (v_ns/(13.0 * u.km))/(2.0 * np.pi)
print freq.to(1.0/u.second)


#===========Problem 3
M_wd = 1.4 * const.M_sun
m_nuc = const.u
m_C = 12.011 * u.gram
m_Ni = 58.6934 * u.gram
m_C_nuc = 8.0 * (10.0**(-23.0)) * u.gram
m_C_tot = m_C_nuc * (12.0 * m_nuc)
e_nuc = 9.0 * 10.0**(-5.0) * u.erg


chains = const.M_sun/m_C_nuc
energy_wd = (chains * e_nuc)/100.0

t_nuc = energy_wd/((10.0**10.0)*const.L_sun)
print "energy wd: ", energy_wd.to(u.erg)
print t_nuc.to(u.day)
#print energy_wd

N_nuc = M_wd/m_nuc
#N_nuc = (1.0*const.M_sun)/m_C_tot


#e_nuc = (((m_nuc/12.0) - (m_nuc/59.0))*const.c**2.0).to(u.erg)

print N_nuc, e_nuc

E_tot = N_nuc * e_nuc

print E_tot.to(u.erg)

time_e = (E_tot/((10.0**10.0)*const.L_sun)).to(u.year)
print time_e/100.0
