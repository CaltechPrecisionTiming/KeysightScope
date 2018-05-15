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

with open('/Users/cmorgoth/Downloads/Na22_ORKA_No_Wrapping_70V.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
#        print ', '.join(row)
        x.append(float(row[0]))
        y.append(float(row[1]))

    #print x,y
    width = x[1]-x[0]
    print len(x),x[0],x[len(x)-1]
    histo = rt.TH1F("histo", "histo", len(x),x[0]*1e9,x[len(x)-1]*1e9)
    x = np.asarray(x)
    y = np.asarray(y)

    fig, ax = plt.subplots(figsize=(8, 6))
    plt.bar(x,y,width)
    plt.xlabel('time [ps]')
    plt.ylabel('entries')
    plt.text(0.15, 0.7, 'mu: {:.3f}'.format(mean(x, y)),
                                            transform=ax.transAxes)
    plt.text(0.15, 0.65, 'std: {:.3f}'.format(std(x, y)),
                                            transform=ax.transAxes)
    plt.savefig('dustin.png')
    print x.dot(y)/y.sum()
    print np.sqrt(np.power(x,2).dot(y)/y.sum() - np.power( x.dot(y)/y.sum(), 2) )
    print mean(x, y)
    print std(x, y)

    # test on random data
    rand_data = np.random.normal(580, 16, size=100000)
    counts, edges = np.histogram(rand_data, bins=100)
    centers = (edges[1:] + edges[:-1])/2.0
    print("Mean and std of simulated data histogram: {:.3f}, {:.3f}".format(
        mean(centers, counts), std(centers, counts)))

    for ii in range(len(x)):
        #print ii, x[ii],y[ii]
        histo.SetBinContent(ii+1,y[ii])


    cv = rt.TCanvas("cv", "cv", 800,600)
    histo.Draw("HISTO")
    cv.SaveAs("test.pdf")
    f = rt.TFile("Na_22_No_Wrapping.root", "RECREATE")
    histo.Write("Na_22_No_Wrapping")
    f.Close()
    #reader = csv.DictReader(csvfile)
    #for row in reader:
    #    print row
