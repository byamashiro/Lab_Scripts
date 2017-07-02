from astropy import units as u
from astropy.units import imperial as imp
#import astropy.units as u
import numpy as np
from astropy import constants as const
import matplotlib.pyplot as plt
import scipy
from scipy import special


#===========You may find this surprising
e_rate = const.L_sun.cgs / const.M_sun.cgs
print "Sun: ", e_rate


m_human = (80.0 * u.kg).cgs
e_human = (2000.0 *imp.kcal).cgs
day_human = (1.0 *u.day).cgs

#print m_human, e_human, day_human
print "Human: ", e_human / (day_human * m_human)

m_lexus = (4222.0 * imp.lb).cgs
e_lexus = (295.0 * imp.hp).cgs
#t_lexus = (7.7 * u.second)

print "Lexus (car): ", e_lexus / ( m_lexus)


#============Energy production
H_1 = 7.28899 * u.MeV
He_4 = 2.42475 * u.MeV
C_12 = 0.0 * u.MeV
rxn_gen = (4. * H_1) - He_4

#print H_1, He_4
print "Energy generated: ", rxn_gen
del_m = (4. * 1.6725*10**(-27) * u.kg) - (6.644*10**(-27)*u.kg)
#print del_m.cgs

#m_rxn = (rxn_gen / const.c**2).cgs
e_rxn = (del_m * const.c**2).to(u.J)

#print e_rxn.to(u.J)

m_He = (He_4 / const.c**2).cgs
m_newrxn = (rxn_gen / const.c**2).cgs
print m_newrxn
e_sun = (const.L_sun).to(u.J/u.second)

n_rxns = e_sun / e_rxn
print n_rxns
#rxn_rate = 9.29*10**37 * 1/u.second

#print m_He, rxn_rate
print "Mass of He generation: " ,(m_newrxn * n_rxns).to(u.kg/u.second)

#======Procedure 2
print rxn_gen.to(u.erg)
print "Ratio L: ", (const.L_sun / rxn_gen.to(u.erg)).cgs
print "Final mass He rate: ",((const.L_sun / rxn_gen.to(u.erg)).cgs)*(6.633*10**(-27) * u.kg)


print "Carbon: ", (3. * He_4) - C_12