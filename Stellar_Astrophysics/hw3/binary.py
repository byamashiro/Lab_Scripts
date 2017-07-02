from astropy import units as u
import numpy as np
from astropy import constants as const



#=====orbital size and stellar masses

v_1 = 32.65 * u.km/u.second
v_2 = 33.67 * u.km/u.second

p = 214.37 * u.day
p_1 = p.to(u.second)
p_2 = p.to(u.year)

a_1 = (v_1 * p_1)/(2 * np.pi)
a_2 = (v_2 * p_1)/(2 * np.pi)

orb_size = a_1 + a_2
orb_size_AU = orb_size.to(u.AU)
print orb_size_AU



st_mass = ((orb_size_AU**3) / (p_2**2))
print st_mass




#=====mass ratios

m_ratio = v_2/v_1
print m_ratio

st_b = st_mass.value / (1.0 + m_ratio)
print st_b

st_a = st_b * m_ratio
print st_a

#===ang sizes


rhs = 2.76 + 0.252*(1.843 - 1.749)
K = 14.895
K_2 = 15.446
log = (rhs - K)/5
log_2 = (rhs - K_2)/5

phi = np.exp(log) * u.deg
phi_2 = np.exp(log_2) *u.deg

print "phi(14.895): ",phi
print "phi(15.446): ",phi_2

st_rad_1 = 26.06
st_rad_2 = 19.76

dist_1 = st_rad_1/np.tan(phi)
dist_2 = st_rad_2/np.tan(phi_2)

print "dist1:",dist_1
print "dist2:",dist_2





