from astropy import units as u
import numpy as np
from astropy import constants as const
import matplotlib.pyplot as plt



e = 0.7
K = 50.0



w_arr = np.array(range(0, 360, 5)) * u.deg
i_arr = np.array(range(0, 360, 20)) * u.deg


for i in i_arr:
	V_arr = np.array([])
	w_ph_arr = np.array([])
	for w in w_arr:
		V = K*(e*np.cos(w) + np.cos(i+w))
		V_arr = np.append(V_arr, V)
		E = 2.0 * np.arctan(np.tan(w/2.0) * np.sqrt((1.0-e)/(1.0+e)))
		M = E.value - e*np.sin(E)

		w_ph = M/(2*np.pi)
		w_ph_arr = np.append(w_ph_arr, w_ph)
	plt.plot(w_ph_arr, V_arr, 'o')
	plt.xlabel('$\omega$/2', fontname="Arial", fontsize = 14)
	plt.ylabel('Radial Velocity [km/s]', fontname="Arial", fontsize = 14)
	plt.minorticks_on()
	plt.grid(True)
	plt.savefig('ellip{:03}.pdf'.format(i), format='pdf', dpi=900)
	plt.show()


