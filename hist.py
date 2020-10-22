import numpy as np
import matplotlib.pyplot as plt
import csv

light = []
sound = []


def outlier(arr):
    avg = np.average(arr)
    std = np.std(arr)
    arr1 = []
    for i in range(len(arr)):
        if (arr[i] <= avg+3*std) and (arr[i] >= avg-3*std):
            arr1.append(arr[i])
    return arr1


with open("unit1/led-sound.csv", "r") as infile:
    reader = csv.reader(infile, delimiter=",")
    for r in reader:
        light.append(float(r[0]))
        sound.append(float(r[1]))

light = outlier(light)
sound = outlier(sound)

av1 = np.average(light)
av2 = np.average(sound)

stdev1 = np.std(light)
stdev2 = np.std(sound)

# print("averages: 1: " + str(av1) + " 2: " + str(av2) + " 3: " + str(av3))
# print("stdev: 1: " + str(stdev1) + " 2: " + str(stdev2) + " 3: " + str(stdev3))

plt.hist(light, fc=(0,0,1,0.5), label= "light: avg = " + "{:.2f}".format(av1) + ", stdev = " + "{:.2f}".format(stdev1))
plt.hist(sound, fc=(0,1,0,0.5), label = "sound: avg = " + "{:.2f}".format(av2) + ", stdev = " + "{:.2f}".format(stdev2))

plt.xlabel("Reaction Time (ms)")
plt.ylabel("count")
plt.title("Histogram of Reaction Times (light vs. sound)")
plt.legend()
plt.show()

