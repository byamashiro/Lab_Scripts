import numpy as np
import matplotlib.pyplot as plt

fname = hotdog-100V.spec
data = np.genfromtxt(
	fname,
	names = True,
	comments = '#',
	delimiter = '\t',
	dtype = None)
	print(data)