#
# Draw a graph with error bars and fit a function to it
#
from ROOT import gStyle , TCanvas , TGraphErrors, TMultiGraph
from array import array
import numpy as np
import matplotlib as plt


gStyle . SetOptFit (111) # superimpose fit results
c1=TCanvas("c1" ,"Data" ,200 ,10 ,900 ,700) #make nice
c1 . SetGrid ()

#TMultiGraph *mg = new TMultiGraph();
#mg = ROOT.TMultiGraph()

#ourgroup
anna_x = np.array([1, 2, 3, 4, 5, 6, 7, 8])

anna_y = np.array([0.045184519, 0.045066857, 0.045275523, 0.045169114, 0.045117404, 0.045045947, 0.045192347, 0.045218582])
anna_y_d = np.array([0.999950004, 0.999950004, 0.999950004, 0.999950004, 0.999950004, 0.999950004, 0.999950004, 0.999950004])
#anna_w_d = np.array([5.0,5.0,5.0,5.0,5.0,5.0])

x_ann = anna_x
y_ann = anna_y
#ex_ann = anna_w_d
ey_ann = anna_y_d
nPoints_ann = len ( x_ann )

#randy
randy_o = np.array([59.9 ,58.1 ,56.9 ,54.9 ,52.8 ,50.2 ,47.8 ,45.2])
randy_o_d = np.array([1.414284271 ,1.414284271 ,1.414284271 ,1.414284271 ,1.414284271 ,1.414284271 ,1.414284271 ,1.414284271])
randy_i = np.array([35.1 ,35.9 ,36.1 ,37.1 ,38.2 ,39.8 ,41.2 ,43.3])
randy_i_d = np.array([1.414284271 ,1.414284271 ,1.414284271 ,1.414284271 ,1.414284271 ,1.414284271 ,1.414284271 ,1.414284271])

x_ran = randy_o
y_ran = randy_i
ex_ran = randy_o_d
ey_ran = randy_i_d
nPoints_ran = len ( x_ran )

#focal point
focal = np.array([22.13147368 ,22.18925532 ,22.08698925 ,22.13902174 ,22.1643956 ,22.19955556 ,22.12764045 ,22.11480226])
focal_err = np.array([2.276602932 ,2.307429116 ,2.322947563 ,2.359838289 ,2.398195174 ,2.443852911 ,2.475886563 ,2.49785615])
focal_mean = np.mean(focal)
focal_mean_err = 0.000229577 / (2 * (8 ** (1/2)))

print focal_mean
print focal_mean_err

#predicted = (focal_mean**(-1) - randy_o**(-1))**(-1)
#
#fig = plt.figure()
#plt.errorbar(randy_o, randy_i, xerr=randy_o_d, yerr=randy_i_d, fmt='rs', ecolor='Grey')
#plt.plot(randy_o_d, predicted)
#
#plt.xlabel(r'$\mathrm{Object\ distance}\ [mm]$', fontsize = 20)
#plt.ylabel(r'$\mathrm{Image\ distance}\ [mm]$', fontsize = 20)
#plt.show()


#root equation
#TF1 *myfit = new TF1("myfit", "", 0, 62)


#equation model
#model_range = np.arange(1.0, 100.0, 1.0)
#print model_range

#d_img = ((1 / focal_mean) - (1 / d_obj)) ** (-1)



ran=TGraphErrors( nPoints_ran , x_ran , y_ran , ex_ran , ey_ran )
#gr.Fit("pol1")
ran.SetMarkerStyle(4)
ran.SetMarkerColor(4)






mg = TMultiGraph()
#mg.Add(bry)
#mg.Add(gab)
#mg.Add(jac)
#mg.Add(jam)
mg.Add(ran)
#mg.Add(ann)




mg.SetTitle(";Object Length [cm];Image Length [cm]")
mg . Draw ( "AP" ) ;
mg.GetXaxis().SetTitleSize(.04)
mg.GetYaxis().SetTitleSize(.04)


#mg.Fit("expo")
#gr.Fit("gaus")
c1 . Update ()
# request user action before ending (and deleting graphics window)
raw_input('Press <ret> to end -> ')