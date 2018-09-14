import csv
import matplotlib.pyplot as plt
import numpy as np
import ROOT as rt

def mean(x, y):
    return x.dot(y)/y.sum()

def std(x, y):
    mu = mean(x, y)
    var = np.power(x, 2).dot(y)/y.sum() - mu * mu
    return np.sqrt(var)

x = []
y = []
x_err = []
y_err = []

with open('Mathematica.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
#        print ', '.join(row)
        x.append(float(row[0]))
        x_err.append(0)
        y.append(float(row[1]))
        y_err.append( 10. )

    #print x,y
    width = x[1]-x[0]
    x = np.asarray(x)
    y = np.asarray(y)
    x_err = np.asarray(x_err)
    y_err = np.asarray(y_err)
    gr = rt.TGraphErrors(len(x), x, y, x_err, y_err)
    c  = rt.TCanvas("c", "c", 800, 600)
    f1 = rt.TF1("f1", "[0]+[1]*cos([2]*x+[3])", 0, 4000)
    f1.SetParameter(0, 450.)
    f1.SetParameter(1, 400.)
    f1.SetParameter(2, 1./3000.)
    f1.SetParameter(3, 600./3000.)
    gr.Fit("f1","REM")
    gr.SetMarkerStyle(20)
    gr.SetMarkerColor(rt.kBlue)
    gr.SetMarkerSize(0.1)
    gr.SetLineColor(rt.kBlue)
    gr.Draw("AP")
    gr.SetTitle("")
    gr.GetXaxis().SetTitle("IM bias (adc count)")
    gr.GetYaxis().SetTitle("PM output (adc count)")
    f1.Draw("same")

    textCMS = rt.TLatex(0.1,0.95,"FQNET")
    textCMS.SetNDC()
    textCMS.SetTextAlign(13)
    textCMS.SetTextFont(62)
    textCMS.SetTextSize(0.05)
    textCMS.Draw()

    label = "f(x) = "+ str("%.2f"%f1.GetParameter(0)) + " + " + str("%.2f"%f1.GetParameter(1)) + "*Cos("+str("%.4f"%f1.GetParameter(2))+"*x + "+ str("%.2f"%f1.GetParameter(3)) +")"
    textF1 = rt.TLatex(0.4,0.8, label)
    textF1.SetNDC()
    textF1.SetTextAlign(13)
    textF1.SetTextFont(62)
    textF1.SetTextSize(0.03)
    textF1.Draw()

    c.SaveAs("tgrap.pdf")

    #fig, ax = plt.subplots(figsize=(8, 6))
    #plt.bar(x,y,width)
    #plt.xlabel('time [ps]')
    #plt.ylabel('entries')
    #plt.text(0.15, 0.7, 'mu: {:.3f}'.format(mean(x, y)),
    #                                        transform=ax.transAxes)
    #plt.text(0.15, 0.65, 'std: {:.3f}'.format(std(x, y)),
    #                                        transform=ax.transAxes)
    #plt.savefig('dustin.png')
    #print x.dot(y)/y.sum()
    #print np.sqrt(np.power(x,2).dot(y)/y.sum() - np.power( x.dot(y)/y.sum(), 2) )
    #rint mean(x, y)
    #print std(x, y)

    # test on random data
    #rand_data = np.random.normal(580, 16, size=100000)
    #counts, edges = np.histogram(rand_data, bins=100)
    #centers = (edges[1:] + edges[:-1])/2.0
    #print("Mean and std of simulated data histogram: {:.3f}, {:.3f}".format(
    #    mean(centers, counts), std(centers, counts)))

    #reader = csv.DictReader(csvfile)
    #for row in reader:
    #    print row
