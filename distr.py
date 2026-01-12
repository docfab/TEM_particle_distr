#!/usr/bin/env python3

#imported packages
import numpy as np
import matplotlib.pyplot as plt
import csv

ratio=0.74

with open('combined.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

data_array = np.array(data, dtype=float)

R=(data_array[:,1]/3.14)**(1/2)/ratio

np.savetxt('output.dat', R)

#tracer les histogramme des position (x et y)
plt.hist(R, bins=25)  # arguments are passed to np.histogram
plt.yscale('log')
plt.xlabel("R (nm)")
plt.ylabel("Number of particles")
plt.savefig('Particle_distr.png')

#display graph
plt.show()
