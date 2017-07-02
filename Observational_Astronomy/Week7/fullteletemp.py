#
# Draw a graph with error bars and fit a function to it
#
from ROOT import gStyle , TCanvas , TGraph, TGraphErrors, TMultiGraph, TF1
from array import array
import numpy as np


#gStyle . SetOptFit (111) # superimpose fit results
gStyle . SetOptStat(0)
c1=TCanvas("c1" ,"Data" ,200 ,10 ,900 ,700) #make nice
c1 . SetGrid ()

#TMultiGraph *mg = new TMultiGraph();
#mg = ROOT.TMultiGraph()

#temperature(0)	darktime(1)	Meancounts(2)	telescope(3) temperature(4)	darktime(5)	Meancounts(6)	telescope(7)


data_ps1 = np.genfromtxt('data_ps1.dat')

temp_ps1 = np.array(data_ps1[:,0])
dtime_ps1 = np.array(data_ps1[:,1])
counts_ps1 = np.array(data_ps1[:,2])

data_isp1 = np.genfromtxt('data_isp1.dat')

temp_isp1 = np.array(data_isp1[:,0])
dtime_isp1 = np.array(data_isp1[:,1])
counts_isp1 = np.array(data_isp1[:,2])

nPoints = len(temp_isp1)
'''
mag = np.array(data[:,1])
mag_err = np.array(data[:,2])
old_mag_err = np.array(data[:,3])
null = np.empty((1,nPoints,))
null[:] = np.NAN
'''
zero = np.empty((1,nPoints,))
zero[:] = 0

#print null, zero
#print mag_err, old_mag_err

#full array
# . . . and hand over to TGraphErros object

#magnitude = TGraphErrors( nPoints , time , mag , mag_err,  mag_err )

magnitude = TGraph(nPoints, temp_ps1, counts_ps1)
#magnitude.Fit("pol4")
magnitude.SetMarkerStyle(4) #7
magnitude.SetMarkerColor(4)

#ran=TGraphErrors( nPoints_ran , x_ran , y_ran , ex_ran , ey_ran )
##gr.Fit("pol1")
#ran.SetMarkerStyle(4)
#ran.SetMarkerColor(2)



#mg.SetStats(0)

magnitude.SetTitle("PS-1 Temperature;Temperature [C];Mean Counts")
magnitude . Draw ( "AP" ) ;
magnitude.GetXaxis().SetTitleSize(.04)
magnitude.GetYaxis().SetTitleSize(.04)
magnitude.GetYaxis().SetTitleOffset(1.2)

'''
magnitude.GetXaxis().SetTimeDisplay(1);
magnitude.GetXaxis().SetNdivisions(-503);
magnitude.GetXaxis().SetTimeFormat("%m/%d/%Y");
magnitude.GetXaxis().SetTimeOffset(0,"gmt");
'''

#magnitude.Fit("pol1")
#gr.Fit("gaus")
#c1 . Update ()
#c1.Print("temp_ps1.pdf");

#------ISP1

magnitude_isp1 = TGraph(nPoints, temp_isp1, counts_isp1)
#magnitude_isp1.Fit("pol4")
magnitude_isp1.SetMarkerStyle(2) #7
magnitude_isp1.SetMarkerColor(2)

magnitude_isp1.SetTitle("ISP-1 Temperature;Temperature [C];Mean Counts")
magnitude_isp1 . Draw ( "AP" ) ;
magnitude_isp1.GetXaxis().SetTitleSize(.04)
magnitude_isp1.GetYaxis().SetTitleSize(.04)
magnitude_isp1.GetYaxis().SetTitleOffset(1.2)


mg = TMultiGraph()
mg.Add(magnitude)
mg.Add(magnitude_isp1)

mg.SetTitle("Full Temperature;Temperature [C];Mean Counts")
mg . Draw ( "AP" ) ;
mg.GetXaxis().SetTitleSize(.04)
mg.GetYaxis().SetTitleSize(.04)
mg.GetYaxis().SetTitleOffset(1.2)

'''
magnitude.GetXaxis().SetTimeDisplay(1);
magnitude.GetXaxis().SetNdivisions(-503);
magnitude.GetXaxis().SetTimeFormat("%m/%d/%Y");
magnitude.GetXaxis().SetTimeOffset(0,"gmt");
'''

#magnitude.Fit("pol1")
#gr.Fit("gaus")
c1 . Update ()
c1.Print("full_temp_v2.pdf");

# request user action before ending (and deleting graphics window)
raw_input('Press <ret> to end -> ')