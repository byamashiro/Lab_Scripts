
void nsew() {
    //Draw a graph with error bars
    // To see the output of this macro, click begin_html <a href="gif/gerrors.gif">here</a>. end_html
    //Author: Rene Brun
    
    TCanvas *c1 = new TCanvas("c1","A Simple Graph with error bars",200,10,700,500);
    
    c1->SetFillColor(0);
    c1->SetGrid();
    c1->GetFrame()->SetFillColor(0); //(21);
    c1->GetFrame()->SetBorderSize(0); //(12);
    //c1.SetLogy();

    
    //const Int_t n = 10;
    //Float_t x[n]  = {-0.22, 0.05, 0.25, 0.35, 0.5, 0.61,0.7,0.85,0.89,0.95};
    //Float_t y[n]  = {1,2.9,5.6,7.4,9,9.6,8.7,6.3,4.5,1};
    //Float_t ex[n] = {.05,.1,.07,.07,.04,.05,.06,.07,.08,.05};
    //Float_t ey[n] = {.8,.7,.6,.5,.4,.4,.5,.6,.7,.8};
    TGraphErrors *gr = new TGraphErrors("nsew.dat","%lg %lg %lg %lg");
    gr->SetTitle("Directional Flux Dependence");
    gr->GetXaxis()->SetTitle("West(-)--East(+) Coordinate Flux");
    gr->GetYaxis()->SetTitle("North(+)--South(-) Coordinate Flux");
    gr->SetMarkerColor(4);
    gr->SetMarkerStyle(4);
    gr->Draw("ALP");
    /*
    TLatex *latex = new TLatex(gr->GetX()[1], gr->GetY()[1],"S,663");
    gr->GetListOfFunctions()->Add(latex);
    latex->SetTextSize(0.05);
    latex->SetTextColor(1);
    gr->Draw("ap");
    
    TLatex *latex = new TLatex(gr->GetX()[2], gr->GetY()[2],"E,639");
    gr->GetListOfFunctions()->Add(latex);
    latex->SetTextSize(0.05);
    latex->SetTextColor(1);
    gr->Draw("ap");
    
    TLatex *latex = new TLatex(gr->GetX()[3], gr->GetY()[3],"W,708");
    gr->GetListOfFunctions()->Add(latex);
    latex->SetTextSize(0.05);
    latex->SetTextColor(1);
    gr->Draw("ap");
    
    TLatex *latex = new TLatex(gr->GetX()[4], gr->GetY()[4],"N");
    gr->GetListOfFunctions()->Add(latex);
    latex->SetTextSize(0.05);
    latex->SetTextColor(1);
    gr->Draw("ap");
     */
    
    
    
    c1->Update();
}





/*
int flux(){
    
TCanvas* c=new TCanvas();
c->SetGrid();

   TGraphErrors graph("muondata2.dat","%lg %lg %lg %*lg");
   graph.SetMarkerStyle(20); 

   graph.Draw("ap");
    
    //graph->SetMarkerColor(kRed);
    graph->SetLineColor(4);
    c1.SetLogy();

   graph.SetTitle("GOES 100MeV Proton;Time;Flux");
    gStyle->SetPadLeftMargin(0.01);
    gStyle->SetPadRightMargin(0.01);

graph.DrawClone("E3AL");
//graph.SetMarkerStyle(kCircle);
//graph.SetFillColor(0);
//graph.DrawClone("PESame");
    

graph.Print();
    
c1->Print("tester.pdf");


}
*/