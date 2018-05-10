import csv
import matplotlib.pyplot as plt
import numpy as np

def mean(x, y):
    return x.dot(y)/y.sum()

def std(x, y):
    mu = mean(x, y)
    var = np.power(x, 2).dot(y)/y.sum() - mu * mu
    return np.sqrt(var)

x = []
y = []

with open('/Users/cmorgoth/HistogramsfromScope/May2/58kV_Na22_Run2_20k_new_btl_assembly_biggerHole.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
#        print ', '.join(row)
        x.append(float(row[0]))
        y.append(float(row[1]))

    #print x,y
    width = x[1]-x[0]
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

    #reader = csv.DictReader(csvfile)
    #for row in reader:
    #    print row
