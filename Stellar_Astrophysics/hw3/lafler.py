from astropy import units as u
import numpy as np
from astropy import constants as const
import matplotlib.pyplot as plt

time = np.genfromtxt("rv2346.dat", usecols=0)
data = np.genfromtxt("rv2346.dat", usecols=1)

print time, data