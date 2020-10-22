import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile
from scipy import signal

rate, data = wavfile.read('sin_a440_3.wav')

# Define time with a sampling rate of 10,000 Hz
tstart = -1
tstop = 1
sample_time = 0.0001
t = np.arange(tstart, tstop, sample_time)



#define a 50 Hz squarewave
squareWave = signal.square(2 * np.pi * 50 * t)

#Setup and Run the fft
num_data_points_SW = len(data)
rate_SW = rate #Your code here
fft_squareWave =  signal.square(2 * np.pi * 50 * t)



# Create a frequency array that goes from 0 to the 10,000 Hz
xaxis_SW = np.arange(0,10000+1)


#Plot the FFT
plt.plot(fft(fft_squareWave))

# Plot Settings
plt.xlim(0, 400) #Shows from 0 to 400 Hz
plt.title("Square Wave FFT")
plt.xlabel("Freq (Hz)")
plt.ylabel("Intensity")

plt.show()