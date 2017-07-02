import datetime
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


#local sidereal time Jan 18, midnight 07h34m05.33s
#Mauna kea locatio 19.8261 N, -155.4708 E

#ra_true_bk = Angle('16h41m14.057s').deg
#dec_true_bk = Angle('36d33m6.42s').deg

dtr = np.pi/180 #degree to radians

LST_at_midnight = Angle('07h34m05.33s').deg
azimuth = -155.4708 #horizontal position (0 to 360)
latitude = 19.8261 #vertical position (-90 to 90)
latitude_rad = latitude * dtr
delta_midnight = np.linspace(-6,6,1000)/24*360
LST = delta_midnight + LST_at_midnight


perseus_RA = Angle('03h18m36.0s').deg
perseus_DEC = Angle('+41d30m54.0s').deg
perseus_DEC_rad = perseus_DEC * dtr
perseus_HA = LST - perseus_RA
perseus_HA_rad = perseus_HA * dtr
perseus_elevation_rad = np.arcsin((np.sin(perseus_DEC_rad)*np.sin(latitude_rad)) + (np.cos(perseus_DEC_rad)*np.cos(latitude_rad)*np.cos(perseus_HA_rad)))
perseus_elevation_deg = (perseus_elevation_rad * (180/np.pi))
#a = np.array([delta_midnight])
#b = np.array([perseus_elevation_deg])
#np.set_printoptions(threshold='nan')
#c = np.row_stack((a,b))
#print c


trainwreck_RA = Angle('04h54m19.0s').deg
trainwreck_DEC = Angle('+02d56m49.0s').deg
trainwreck_DEC_rad = trainwreck_DEC * dtr
trainwreck_HA = LST - trainwreck_RA
trainwreck_HA_rad = trainwreck_HA * dtr
trainwreck_elevation_rad = np.arcsin((np.sin(trainwreck_DEC_rad)*np.sin(latitude_rad)) + (np.cos(trainwreck_DEC_rad)*np.cos(latitude_rad)*np.cos(trainwreck_HA_rad)))
trainwreck_elevation_deg = (trainwreck_elevation_rad * (180/np.pi))

abel569_RA = Angle('07h09m10.0s').deg
abel569_DEC = Angle('+48d37m10.0s').deg
abel569_DEC_rad = abel569_DEC * dtr
abel569_HA = LST - abel569_RA
abel569_HA_rad = abel569_HA * dtr
abel569_elevation_rad = np.arcsin((np.sin(abel569_DEC_rad)*np.sin(latitude_rad)) + (np.cos(abel569_DEC_rad)*np.cos(latitude_rad)*np.cos(abel569_HA_rad)))
abel569_elevation_deg = (abel569_elevation_rad * (180/np.pi))

hydra_RA = Angle('10h36m51.0s').deg
hydra_DEC = Angle('-27d31m35.0s').deg
hydra_DEC_rad = hydra_DEC * dtr
hydra_HA = LST - hydra_RA
hydra_HA_rad = hydra_HA * dtr
hydra_elevation_rad = np.arcsin((np.sin(hydra_DEC_rad)*np.sin(latitude_rad)) + (np.cos(hydra_DEC_rad)*np.cos(latitude_rad)*np.cos(hydra_HA_rad)))
hydra_elevation_deg = (hydra_elevation_rad * (180/np.pi))

coma_RA = Angle('12h59m49.0s').deg
coma_DEC = Angle('+27d58m50.0s').deg
coma_DEC_rad = coma_DEC * dtr
coma_HA = LST - coma_RA
coma_HA_rad = coma_HA * dtr
coma_elevation_rad = np.arcsin((np.sin(coma_DEC_rad)*np.sin(latitude_rad)) + (np.cos(coma_DEC_rad)*np.cos(latitude_rad)*np.cos(coma_HA_rad)))
coma_elevation_deg = (coma_elevation_rad * (180/np.pi))

A1689_RA = Angle('13h11m30.0s').deg
A1689_DEC = Angle('-01d20m17.0s').deg
A1689_DEC_rad = A1689_DEC * dtr
A1689_HA = LST - A1689_RA
A1689_HA_rad = A1689_HA * dtr
A1689_elevation_rad = np.arcsin((np.sin(A1689_DEC_rad)*np.sin(latitude_rad)) + (np.cos(A1689_DEC_rad)*np.cos(latitude_rad)*np.cos(A1689_HA_rad)))
A1689_elevation_deg = (A1689_elevation_rad * (180/np.pi))



#elevation_rad = np.arccos(-(np.cos(declination*dtr)*np.sin(HA*dtr))/np.sin(azimuth*dtr))


#print elevation_rad, elevation_deg
plt.ylim(30,90)
plt.plot(delta_midnight*24/360, perseus_elevation_deg, color='black', label='Perseus')
plt.plot(delta_midnight*24/360, trainwreck_elevation_deg, color='purple', label='Train Wreck')
plt.plot(delta_midnight*24/360, abel569_elevation_deg, color='blue', label='Abell 569')
plt.plot(delta_midnight*24/360, hydra_elevation_deg, color='green', label='Hydra')
plt.plot(delta_midnight*24/360, coma_elevation_deg, color='yellow', label='Coma')
plt.plot(delta_midnight*24/360, A1689_elevation_deg, color='red', label='Abell 1689')
plt.xlabel('midnight [hours]', fontsize=14)
plt.ylabel('elevation [deg]', fontsize=14)
#plt.legend(loc="best", ncol=1, shadow=False, fancybox=True)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
#plt.savefig('azimuth.pdf', format='pdf', dpi=900)
plt.savefig('azimuth.pdf', bbox_inches='tight', dpi=900)



plt.show()





