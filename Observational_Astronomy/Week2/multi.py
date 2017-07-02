#
# Draw a graph with error bars and fit a function to it
#
from ROOT import gStyle , TCanvas , TGraphErrors, TMultiGraph, TF1
from array import array
import numpy as np


gStyle . SetOptFit (111) # superimpose fit results
c1=TCanvas("c1" ,"Data" ,200 ,10 ,900 ,700) #make nice
c1 . SetGrid ()

#TMultiGraph *mg = new TMultiGraph();
#mg = ROOT.TMultiGraph()

#anna
anna_h = np.array([161.0,165.0,163.0,174.0,171.0,169.0])
anna_h_d = np.array([5.0,5.0,5.0,5.0,5.0,5.0])
anna_w = np.array([165.0,177.0,157.0,173.0,175.0,183.0])
anna_w_d = np.array([5.0,5.0,5.0,5.0,5.0,5.0])

x_ann = anna_w
y_ann = anna_h
ex_ann = anna_w_d
ey_ann = anna_h_d
nPoints_ann = len ( x_ann )

#randy
randy_h = np.array([176.0,172.5,172.1,161.3,174.0,162.5,171.2,161.5])
randy_h_d = np.array([0.1,0.2,0.2,0.1,0.2,0.1,0.2,0.1])
randy_w = np.array([179.2,184.0,175.7,160.5,174.0,158.0,169.8,164.0])
randy_w_d = np.array([0.2,0.1,0.2,0.1,0.2,0.2,0.2,0.2])

x_ran = randy_w
y_ran = randy_h
ex_ran = randy_w_d
ey_ran = randy_h_d
nPoints_ran = len ( x_ran )

#james
james_h = np.array([171.6,176.0,176.7,161.3])
james_h_d = np.array([0.2,0.2,0.2,0.2])
james_w = np.array([174.7,177.8,174.1,166.1])
james_w_d = np.array([3.5,3.5,3.5,3.3])

x_jam = james_w
y_jam = james_h
ex_jam = james_w_d
ey_jam = james_h_d
nPoints_jam = len ( x_jam )

#bryan
bryan_h = np.array([161.0,172.0,163.0])
bryan_h_d = np.array([1.0,1.0,1.0])
bryan_w = np.array([167.0,185.0,161.0])
bryan_w_d = np.array([1.0,1.0,1.0])

x_bry = bryan_w
y_bry = bryan_h
ex_bry = bryan_w_d
ey_bry = bryan_h_d
nPoints_bry = len ( x_bry )

#jacob
jacob_h = np.array([171.9,163.7,176.3,162.4,177.8,161.2])
jacob_h_d = np.array([0.1,0.1,0.1,0.1,0.1,0.1])
jacob_w = np.array([183.6,160.3,178.6,161.3,172.9,165.2])
jacob_w_d = np.array([0.1,0.1,0.1,0.1,0.1,0.1])

x_jac = jacob_w
y_jac = jacob_h
ex_jac = jacob_w_d
ey_jac = jacob_h_d
nPoints_jac = len ( x_jac )

#gabster
gabster_h = np.array([175.5,173.1,163.5])
gabster_h_d = np.array([0.1,0.1,0.1])
gabster_w = np.array([171.6,183.9,162.1])
gabster_w_d = np.array([0.2,0.2,0.2])

x_gab = gabster_w
y_gab = gabster_h
ex_gab = gabster_w_d
ey_gab = gabster_h_d
nPoints_gab = len ( x_gab )

#full array
full_h = np.concatenate((anna_h, randy_h, james_h, bryan_h, jacob_h, gabster_h))
full_h_d = np.concatenate((anna_h_d, randy_h_d, james_h_d, bryan_h_d, jacob_h_d, gabster_h_d))

full_w = np.concatenate((anna_w, randy_w, james_w, bryan_w, jacob_w, gabster_w))
full_w_d = np.concatenate((anna_w_d, randy_w_d, james_w_d, bryan_w_d, jacob_w_d, gabster_w_d))

nPoints_full = len ( full_h )



#define some data points . . .
#x = array('f', (-0.22, 0.1, 0.25, 0.35, 0.5, 0.61, 0.7, 0.85, 0.89, 1.1) )
#y = array('f', (0.7, 2.9, 5.6, 7.4, 9., 9.6, 8.7, 6.3, 4.5, 1.1) )
#ey = array('f', (.8 ,.7 ,.6 ,.5 ,.4 ,.4 ,.5 ,.6 ,.7 ,.8) )
#ex = array('f', (.05 ,.1 ,.07 ,.07 ,.04 ,.05 ,.06 ,.07 ,.08 ,.05) )







# . . . and hand over to TGraphErros object

ann=TGraphErrors( nPoints_ann , x_ann , y_ann , ex_ann , ey_ann )
#gr.Fit("pol1")
ann.SetMarkerStyle(4)
ann.SetMarkerColor(1)

ran=TGraphErrors( nPoints_ran , x_ran , y_ran , ex_ran , ey_ran )
#gr.Fit("pol1")
ran.SetMarkerStyle(4)
ran.SetMarkerColor(2)

jam=TGraphErrors( nPoints_jam , x_jam , y_jam , ex_jam , ey_jam )
#gr.Fit("pol1")
jam.SetMarkerStyle(4)
jam.SetMarkerColor(3)


bry=TGraphErrors( nPoints_bry , x_bry , y_bry , ex_bry , ey_bry )
bry.Fit("pol1")
bry.GetFunction("pol1").SetLineColor(4)
bry.SetMarkerStyle(4)
bry.SetMarkerColor(4)

gab=TGraphErrors( nPoints_gab , x_gab , y_gab , ex_gab , ey_gab )
#gr.Fit("pol1")
gab.SetMarkerStyle(4)
gab.SetMarkerColor(5)

jac=TGraphErrors( nPoints_jac , x_jac , y_jac , ex_jac , ey_jac )
#gr.Fit("pol1")
jac.SetMarkerStyle(4)
jac.SetMarkerColor(6)





mg = TMultiGraph()
mg.Add(bry)
mg.Add(gab)
mg.Add(jac)
mg.Add(jam)
mg.Add(ran)
mg.Add(ann)




mg.SetTitle(";Wing Span (cm);Height (cm)")
mg . Draw ( "AP" ) ;
mg.GetXaxis().SetTitleSize(.04)
mg.GetYaxis().SetTitleSize(.04)


mg.Fit("pol1")
#gr.Fit("gaus")
c1 . Update ()
# request user action before ending (and deleting graphics window)
raw_input('Press <ret> to end -> ')