#
# Draw a graph with error bars and fit a function to it
#
from ROOT import gStyle , TCanvas , TGraphErrors, TMultiGraph, TF1
from array import array
import numpy as np


#gStyle . SetOptFit (111) # superimpose fit results
gStyle . SetOptStat(0)
c1=TCanvas("c1" ,"Data" ,200 ,10 ,900 ,700) #make nice
c1 . SetGrid ()

#TMultiGraph *mg = new TMultiGraph();
#mg = ROOT.TMultiGraph()


data = np.genfromtxt('magnitude.dat')

time = np.array(data[:,0])
nPoints = len(time)

mag = np.array(data[:,1])
mag_err = np.array(data[:,2])
old_mag_err = np.array(data[:,3])
null = np.empty((1,nPoints,))
null[:] = np.NAN

zero = np.empty((1,nPoints,))
zero[:] = 0

print null, zero


print mag_err, old_mag_err




#full array


# . . . and hand over to TGraphErros object

magnitude = TGraphErrors( nPoints , time , mag , mag_err,  mag_err )
magnitude.Fit("pol4")
magnitude.SetMarkerStyle(4) #7
magnitude.SetMarkerColor(4)

#ran=TGraphErrors( nPoints_ran , x_ran , y_ran , ex_ran , ey_ran )
##gr.Fit("pol1")
#ran.SetMarkerStyle(4)
#ran.SetMarkerColor(2)

#mg = TMultiGraph()
#mg.Add(magnitude)
#mg.SetStats(0)

magnitude.SetTitle(";Time;Magnitude")
magnitude . Draw ( "AP" ) ;
magnitude.GetXaxis().SetTitleSize(.04)
magnitude.GetYaxis().SetTitleSize(.04)

magnitude.GetXaxis().SetTimeDisplay(1);
magnitude.GetXaxis().SetNdivisions(-508); #-503

magnitude.GetXaxis().SetTimeFormat("%m/%d");
magnitude.GetXaxis().SetTimeOffset(0,"gmt");



#magnitude.Fit("pol1")
#gr.Fit("gaus")
c1 . Update ()
c1.Print("magnitude.pdf");

# request user action before ending (and deleting graphics window)
raw_input('Press <ret> to end -> ')