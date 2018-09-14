#include <iostream>
#include <fstream>
#include <string>
#include <TROOT.h>
#include <TFile.h>
#include <TH1F.h>
//#include <>

int main( )
{
  std::ifstream ifs( "Entanglement_TagsHistogram_Laser491p9_0.txt", std::ifstream::in );
  double mass, xsec;
  std::string line, dummy;
  TH1F* h = new TH1F("h", "h", 52,0,30);
  int ctr = 1;
  if ( ifs.is_open() )
    {
      getline (ifs,line);
      std::cout << line << std::endl;
      getline (ifs,line);
      getline (ifs,line);
      getline (ifs,line);
      getline (ifs,line);
      std::cout << line << std::endl;
      while ( ifs.good() )
      {
        ifs >> mass >> dummy >> xsec;
        h->SetBinContent(ctr,xsec);
        ctr++;
        if ( ifs.eof() ) break;
        std::cout << mass << ","  << xsec << std::endl;
      }
    }
  else
    {
      std::cout << "[ERROR] unable to open file; quitting" << std::endl;
    }


    double center = h->GetBinContent(15) + h->GetBinContent(16) + h->GetBinContent(17);
    double side = h->GetBinContent(6) + h->GetBinContent(7) + h->GetBinContent(23) + h->GetBinContent(24);
    std::cout << "HERE: " << center/side << std::endl;
    TFile* f = new TFile("fout.root", "RECREATE");
    h->Write();
    f->Close();

  return 0;
}
