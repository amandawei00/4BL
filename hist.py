import numpy as np
import matplotlib.pyplot as plt
import csv

c1 = []
c2 = []
c3 = []


def outlier(arr):
    avg = np.average(arr)
    std = np.std(arr)
    arr1 = []
    for i in range(len(arr)):
        if (arr[i] <= avg+3*std) and (arr[i] >= avg-3*std):
            arr1.append(arr[i])
    return arr1


with open("unit1/unit1.csv", "r") as infile:
    reader = csv.reader(infile, delimiter=",")
    for r in reader:
        c1.append(float(r[0]))
        c2.append(float(r[1]))
        if r[2] != '':
            c3.append(float(r[2]))

c1 = outlier(c1)
c2 = outlier(c2)
c3 = outlier(c3)

av1 = np.average(c1)
av2 = np.average(c2)
av3 = np.average(c3)

stdev1 = np.std(c1)
stdev2 = np.std(c2)
stdev3 = np.std(c3)

print("averages: 1: " + str(av1) + " 2: " + str(av2) + " 3: " + str(av3))
print("stdev: 1: " + str(stdev1) + " 2: " + str(stdev2) + " 3: " + str(stdev3))

plt.hist(c1, fc=(0,0,1,0.5), label= "3 colors: avg = 512.93, stdev = 180.54")
plt.hist(c2, fc=(0,1,0,0.5), label = "2 colors: avg = 409.20, stdev = 117.97")
plt.hist(c3, fc=(1,0,0,0.5), label = "1 color: avg = 231.52, stdev = 65.86")

plt.xlabel("Reaction Time (ms)")
plt.ylabel("count")
plt.title("Histogram of Reaction Times (RGB LED)")
plt.legend()
plt.show()

