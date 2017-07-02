from ROOT import gStyle , TCanvas , TGraphErrors, TMultiGraph, TF1
from array import array
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline




null_points = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
objectDistances = np.array([58.4, 56.6, 55.4, 53.4, 51.3, 48.7, 46.3, 43.7])
d_Objects = np.array([0.193649167, 0.193649167, 0.193649167, 0.193649167, 0.193649167, 0.193649167, 0.193649167, 0.193649167])
imageDistances = np.array([34.9, 35.7, 35.9, 36.9, 38.0, 39.6, 41.0, 43.1])
d_Image = np.array([0.193649167, 0.193649167, 0.193649167, 0.193649167, 0.193649167, 0.193649167, 0.193649167, 0.193649167])
Distance_len = len ( objectDistances )

focal = np.array([21.84523044, 21.89187432, 21.7837897, 21.82126246, 21.82978723, 21.8405436, 21.74455899, 21.69896313])
focal_mean = np.mean(focal)
max_value = np.amax(focal)
min_value = np.amin(focal)

print 'Focal Mean: ',focal_mean
print 'Focal Max Value: ',max_value
print 'Focal Min Value: ',min_value
#Used to find interval and max and minimum values for the arange
print "=============================================="

focalLength = focal_mean
predicted = (focalLength**(-1) - objectDistances**(-1))**(-1)
calculated = (21.7925**(-1) - objectDistances**(-1))**(-1)
best_left = (21.7885**(-1) - objectDistances**(-1))**(-1)
best_right = (21.796**(-1) - objectDistances**(-1))**(-1)
mean_best = (21.8070012338**(-1) - objectDistances**(-1))**(-1)

difference = predicted - imageDistances
chiSquare = np.sum(difference**2 / d_Image**2)
print 'Focal Mean and Chi Squared Value'
print focalLength, chiSquare

print "=============================================="

#For following, focal is the array of 8 measurements
focalLengths = np.arange(21.69896313, 21.89187432, 0.0005) #original
#focalLengths = np.arange(21.785, 21.80, 0.0005)
#focalLengths = np.arange(21.69, 21.90, 0.01)
#change 0.005 for larger/smaller intervals
chiSquares = np.array([])
for focal in focalLengths:
	predicted = (focal**(-1) - objectDistances**(-1))**(-1)
	difference = predicted - imageDistances
	chiSquare = np.sum(difference**2 / d_Image**2)
	chiSquares = np.append(chiSquares, chiSquare)
	print focal, chiSquare


fig = plt.figure()
plt.errorbar(objectDistances, imageDistances, xerr=d_Objects, yerr=d_Image, fmt='o', ecolor='blue', mfc='none')
plt.plot(objectDistances,predicted,linewidth=2,color='green') #predicted
plt.plot(objectDistances,calculated,linewidth=2,color='red') #low fit
plt.plot(objectDistances,best_left,linewidth=2,color='blue') #best fit
plt.plot(objectDistances,best_right,linewidth=2,color='blue') #best fit
plt.plot(objectDistances,mean_best,linewidth=2,color='purple') #mean


plt.xlabel('Object Distance [cm]', fontname="Arial", fontsize = 18)
plt.ylabel('Image Distance [cm]', fontname="Arial", fontsize = 18)
plt.minorticks_on()
plt.grid()

fig.savefig('fitter.eps')
plt.show()


#============ROOT
#gStyle . SetOptFit (111) # superimpose fit results
#gStyle . SetOptStat(0)
gStyle.SetOptStat(0)

c1=TCanvas("c1" ,"Data" ,200 ,10 ,900 ,700) #make nice
c1 . SetGrid ()

papaya = TGraphErrors( Distance_len , objectDistances , imageDistances , d_Objects , d_Image )
#gr.Fit("pol1")
papaya.SetMarkerStyle(4)
papaya.SetMarkerColor(4)
papaya.SetLineStyle(2)
papaya.SetLineColor(1)

banana = TGraphErrors( Distance_len , objectDistances , predicted , null_points , null_points )
#gr.Fit("pol1")
banana.SetMarkerStyle(0)
banana.SetMarkerColor(6)
banana.SetLineColor(4)
banana.SetLineWidth(2)

mg = TMultiGraph()
mg.Add(papaya)
mg.Add(banana)

mg.SetTitle(";Object Length [cm];Image Length [cm]")
mg . Draw ( "ALP" ) ;
mg.GetXaxis().SetTitleSize(.04)
mg.GetYaxis().SetTitleSize(.04)

fit1 = TF1("func1", "(21.79**(-1) - x[0]**(-1))**(-1)", 40.0, 60.0 )
#fit1 = TF1("func", "(focal**(-1) - objectDistances**(-1))**(-1)", 40.0, 60.0 )
fit1.SetLineStyle(1)
fit1.SetLineColor(2)
#c1 . Update ()

#mean value
fit2 = TF1("func2", "(21.8070012338**(-1) - x[0]**(-1))**(-1)", 40.0, 60.0 )
#fit1 = TF1("func", "(focal**(-1) - objectDistances**(-1))**(-1)", 40.0, 60.0 )
fit2.SetLineStyle(1)
fit2.SetLineColor(3)
mg.Fit(fit1,"R+")
mg.Fit(fit2,"R+")


c1 . Update ()
c1.Print("flup.eps")
# request user action before ending (and deleting graphics window)
raw_input('Press <ret> to end -> ')
