import numpy as np
import matplotlib.pyplot as plt

# x data
x = np.linspace(-0.01,0.01,1000)
L = 0.01 # half the period

# Initial Sums
f3 = 0  # n=1..3
f9 = 0  # n=1..9
f49 = 0  # n=1..49


f1 = (4/np.pi) * (np.sin(np.pi*x/L))


for n in range(1, 4, 2):
    f3 += (4/np.pi)*(1/n)*np.sin(n*np.pi*x/L)


for n in range(1, 10, 2):
    f9 += (4/np.pi)*(1/n)*np.sin(n*np.pi*x/L)


for n in range(1, 50, 2):
    f49 += (4/np.pi)*(1/n)*np.sin(n*np.pi*x/L)

# Make the plots
plt.plot(x, f1, label="n=1")
plt.plot(x, f3, label="n=1..3")
plt.plot(x, f9, label="n=1..9")
plt.plot(x, f49, label="n=1..49")

# Plot settings
plt.title("Square Wave Fourier Series")
plt.legend()
plt.xlim([-0.01, 0.01])
plt.xlabel("Time (sec)")
plt.ylabel("Intensity")

plt.show()