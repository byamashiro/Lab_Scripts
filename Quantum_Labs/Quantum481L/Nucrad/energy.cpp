#include <TMultiGraph.h>

int energy(){
    
gStyle->SetOptFit();
TCanvas *c1=new TCanvas("c1","multigraph",700,500);

c1->SetGrid();
    
    
TMultiGraph *mg = new TMultiGraph();

//====================GOES flux data
    
    TGraphErrors *gr1 = new TGraphErrors("energyangle.dat","%*lg %lg %lg");
    gr1->SetTitle("E1");
    gr1->SetMarkerColor(kBlue);
    gr1->SetMarkerStyle(4);
    gr1->SetFillStyle(0);
    gr1->SetLineColor(kBlue);
    gr1->SetLineWidth(1);
    
    //TF1 * f1 = new TF1("f1","-[0]*(1.-2*exp(-x/[1]))");
    //gr1->Fit("f1","R","R", 0.0001, 0.06);

    mg->Add(gr1);
    
    
    TGraphErrors *gr2 = new TGraphErrors("energyangle.dat","%*lg %lg %*lg %lg");
    gr2->SetTitle("E2");
    gr2->SetMarkerColor(kRed);
    gr2->SetMarkerStyle(4);
    gr2->SetFillStyle(0);
    gr2->SetLineColor(kBlue);
    gr2->SetLineWidth(1);
    
    mg->Add(gr2);

    
    //c1.SetLogy();
    mg->Draw("AP");
    mg.SetTitle("5 GeV #pi^{0} Decay Angles;Angle (#circ);Energy (MeV)");
    
    c1->BuildLegend();
    //leg = new TLegend(0.7,0.7,.85,0.85); //TLegend(0.1,0.7,0.48,0.9); \\left,bottom,right,top
    //leg->SetHeader("The Legend Title");
    //leg->SetLineWidth(1);
    //leg->Set
    //leg->AddEntry(gr1,"#gamma E_{1}","l");
    //leg->AddEntry(gr2,"#gamma E_{2}","l");
    //leg->AddEntry("gr","Graph with error bars","lep");
    leg->Draw();

    gStyle->SetPadLeftMargin(0.01);
    gStyle->SetPadRightMargin(0.01);

c1->Print("nacl1.pdf");


}
/*
TGraphErrors * gr1 = new TGraphErrors("t1.dat","%lg %lg %lg");
gr1->SetTitle("T1");
gr1->SetMarkerColor(kBlue);
gr1->SetMarkerStyle(4);
gr1->SetFillStyle(0);
gr1->SetLineColor(kBlue);
gr1->SetLineWidth(1);

TF1 * f1 = new TF1("f1","([0]*1.)-(2.*[0]*exp(-x/[1]))+[2]");
gr1->Fit("f1","R","R", 0.01, 0.06);

gr1->Draw("AP");


}
*/
