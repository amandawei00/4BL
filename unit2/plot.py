import numpy as np
import matplotlib.pyplot as plt

dist = [0.4953, 0.381, 0.5588, 0.4318, 0.2794, 0.1778]  # distance in meters
time = [1422.4, 1099.94, 1622.47, 1246.7, 784.1, 494.32]  # time in microseconds

# pick two random points and find the speed of sound: v = ds/dt
v = ((dist[4] - dist[0])/(time[4] - time[0])) * 1000000

# producing parameters for linear fit y = m*x + b
param = np.polyfit(time, dist, 1)

xfit = np.linspace(0,1700, 1000000)
yfit = param[0]*xfit + param[1]

# defining error arrays:
dist_err = [0.02] * len(dist)
time_err = [5] * len(time)

# output details
print("speed of sound from fit: v = " + "{:.2f}".format(param[0]*1000000))
# output plot
# legend labels
fit_label = "linear fit: y = " + "{:.4f}".format(param[0]) + "*x + " + "{:.4f}".format(param[1])
scatter_label = "raw data"

# axis label
x_axis = "time (microseconds)"
y_axis = "distance (meters)"
title = "speed of sound (distance v. time)"

# plotting data, error bars
plt.scatter(time, dist, label=scatter_label)
plt.errorbar(time, dist, xerr=time_err, yerr=dist_err, ls='none')  # plot error bars
plt.plot(xfit, yfit, color='red', label=fit_label)

# plot details
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.title(title)
plt.legend()

# display plot
plt.show()