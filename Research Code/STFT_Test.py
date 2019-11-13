from scipy.io.wavfile import read
import os
from scipy.signal import stft
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import numpy as np

# Initializing these values just in case the audio file doesn't exist, that way Python doesn't show an error
sample_rate = 0
data = np.ndarray([])

# Walk through files in our folder in Public and find the file that matches the input
for root, dirs, files in os.walk(r'P:\+Courses\AstroStats\LivingSeaSculpture\Initial Data for Testing'):
    for name in files:
        # print(os.path.abspath(os.path.join(root, name)))
        if name == "FFT_Test_2.wav":
            [sample_rate, data] = read(os.path.abspath(os.path.join(root, name)))
            # .wav files import as 2-column arrays of sampled audio at 44100 Hz

data_sample = data[:,0] #Commented out so I can easily switch between running on a section
# and running on the whole thing
# data_sample = data[10*sample_rate:24*sample_rate, 0]

# Take the STFT so we can see amplitudes at specific frequencies with respect to time
f, t, Zxx = stft(data_sample, fs=sample_rate)

# Remove frequencies above 5 kHz to speed up runtime
for freq in f:
    if freq > 5000:
        index = int(np.where(f == freq)[0])
        break
Zxx = Zxx[:index]
f = f[:index]

# Using Eric's smoothing code, see Clean_Fish.py for details
smoothness = 5
psd = np.array([])
for slice in range(0, len(t)):
    psd = np.append(psd, np.trapz(np.abs(Zxx[:, slice]), f))

pbar = np.mean(psd)

for i in range(0, len(psd)):
    psd[i] = psd[i]**2/pbar

for i in range(0, len(psd)-smoothness): # A moving average
    psd[i] = sum(psd[i:i+smoothness])/(smoothness+1)

# Using Scipy's find_peaks method
timestamps_clean, _ = find_peaks(psd, height=1000000, distance=50)

# I didn't realize that scipy had a find_peaks method, so I wrote code to find peaks and group clusters into single peaks
# pbar = np.mean(psd)
# timestamps = np.where(psd > pbar)[0]
#
# timestamps_clean = np.array([])
#
# current_val = timestamps[0]
# last_val = t[timestamps[0]]
# for time_index in range(1, timestamps.size):
#     if last_val >= t[timestamps[time_index]] - 0.1:
#         last_val = t[timestamps[time_index]]
#         continue
#     else:
#         timestamps_clean = np.append(timestamps_clean, current_val)
#         current_val = timestamps[time_index]
#         last_val = t[timestamps[time_index]]
# if timestamps_clean[-1] != current_val:
#     timestamps_clean = np.append(timestamps_clean, current_val)
# print(timestamps_clean.size)

# Plot peaks
fig = plt.plot(t, psd)
axs = plt.axes()
for time in np.nditer(timestamps_clean):
    axs.axvline(t[int(time)], color='red', ymax=0.5)
plt.show()
