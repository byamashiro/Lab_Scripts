from ROOT import gStyle , TCanvas , TGraphErrors, TMultiGraph
from array import array
import numpy as np
import matplotlib.pyplot as plt

objectDistances = np.array([71.0, 90.0, 110.0, 131.0, 150.0])
d_Objects = np.array([2.0, 2.0, 2.0, 2.0, 2.0])
imageDistances = np.array([173.0, 113.0, 91.0, 81.0, 74.0])
d_Image = np.array([2.0, 2.0, 2.0, 2.0, 2.0])

for focalLength in np.arange(48, 52.01, 0.1):
	print focalLength

focalLengths = np.arange(48,52.01,0.1)
chiSquares = np.array([])
for focalLength in focalLengths:
	predicted = (focalLength**(-1) - objectDistances**(-1))**(-1)
	difference = predicted - imageDistances
	chiSquare = np.sum(difference**2 / d_Image**2)
	chiSquares = np.append(chiSquares, chiSquare)
	print focalLength, chiSquare