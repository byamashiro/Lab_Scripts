#include <TMultiGraph.h>

int nacl2(){
    
gStyle->SetOptFit();
TCanvas *c1=new TCanvas("c1","multigraph",700,500);

c1->SetGrid();
    
    
TMultiGraph *mg = new TMultiGraph();

//====================GOES flux data
    
    TGraphErrors *gr1 = new TGraphErrors("nacl2.dat","%lg %lg %lg %lg");
    gr1->SetTitle("No Filter");
    gr1->SetMarkerColor(kBlue);
    gr1->SetMarkerStyle(0);
    gr1->SetFillStyle(0);
    gr1->SetLineColor(kBlue);
    gr1->SetLineWidth(1);

    //gr4->SetTitle("graph 3");
    mg->Add(gr1);
    /*
    TGraph *gr7 = new TGraph("rigkp.dat","%lg %*lg %*lg %lg");
    gr7->SetTitle("Kp");
    gr7->SetMarkerColor(kCyan+1);
    gr7->SetMarkerStyle(0);
    gr7->SetFillStyle(0);
    gr7->SetLineColor(kPink+1);
    //gr4->SetTitle("graph 3");
    mg->Add(gr7);
    */
    
    TGraphErrors *gr2 = new TGraphErrors("nacl2.dat","%lg %*lg %*lg %*lg %lg %lg %lg");
    gr2->SetTitle("Ni Filter");
    gr2->SetMarkerColor(kRed);
    //gr1->SetMarkerColor(3);
    gr2->SetMarkerStyle(2);
    gr2->SetFillStyle(0);
    gr2->SetLineColor(kRed);
    gr2->SetLineWidth(1);
        mg->Add(gr2);

//=================Drawing the data
    
    //c1.SetLogy();
    mg->Draw("ALP");


    //gr2->Draw("LP");
    //gr3->Draw("LP");
    //gr4->Draw("LP");
    mg.SetTitle("NaCl (n=2);Angle (#circ);Counts");
    //c1->BuildLegend();

    
    leg = new TLegend(0.7,0.7,.85,0.85); //TLegend(0.1,0.7,0.48,0.9); \\left,bottom,right,top
    //leg->SetHeader("The Legend Title");
    //leg->SetLineWidth(1);
    //leg->Set
    leg->AddEntry(gr1,"No Filter","l");
    leg->AddEntry(gr2,"Ni Filter","l");
    //leg->AddEntry("gr","Graph with error bars","lep");
    leg->Draw();

    

    
    
    
//=================Converting to Time axis
/*    mg.GetXaxis()->SetTimeDisplay(1);
    mg.GetXaxis()->SetNdivisions(-503);
    mg.GetXaxis()->SetTimeFormat("%m/%d/%Y");
    mg.GetXaxis()->SetTimeOffset(0,"gmt");
    //mg.GetYaxis()->SetRange(0,2);
*/
    
//=================Finishing the axis
    
    //mg.SetTitle("GOES 100MeV Proton;Time;Flux");
    
    
    
    gStyle->SetPadLeftMargin(0.01);
    gStyle->SetPadRightMargin(0.01);

    

    
    //mg->Update();
    
    //mg->Add( gr1 );
    //mg->Add( gr2 );
    //gr3->Draw("ALP");
    //mg->Draw("P");
    //gr1->Draw("l");
    //gr2->Draw("p");
    
    //mg.DrawClone("E3AL");
    //mg.DrawClone("PESame");
    
    //mg->Update();

    
    
//graph.SetMarkerStyle(kCircle);
//graph.SetFillColor(0);

    

//mg.Print();

c1->Print("nacl2.pdf");
 //   c1->Print("testing.png");


}