import numpy as np
import matplotlib.pyplot as plt
import csv

c1 = []
c2 = []
c3  = []

with open("unit1/unit1.csv", "r") as infile:
    reader = csv.reader(infile, delimiter=",")
    for r in reader:
        c1.append(float(r[0]))
        c2.append(float(r[1]))
        if r[2] != '':
            c3.append(float(r[2]))


plt.hist(c1, fc=(0,0,1,0.5))
plt.hist(c2, fc=(0,1,0,0.5))
plt.hist(c3, fc=(1,0,0,0.5))

plt.show()

