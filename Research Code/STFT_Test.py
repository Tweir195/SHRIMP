from scipy.io.wavfile import read
import os
from scipy.signal import stft
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import numpy as np
import time

start_time = time.time()

# Initializing these values just in case the audio file doesn't exist, that way Python doesn't show an error
sample_rate = 0
data = np.ndarray([])

# Walk through files in our folder in Public and find the file that matches the input
for root, dirs, files in os.walk(r'P:\+Courses\AstroStats\LivingSeaSculpture'):
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

max_val = max(psd)

# Using Scipy's find_peaks method
# Peaks that are significantly above the baseline but not quite the highest peaks are likely glupping or other
# fish-based noises
timestamps, _ = find_peaks(psd, height=[1000000, 0.75*max_val], distance=50)

# Snapping shrimp can reach up to 218 decibels and are basically always snapping, so they make a stable marker
# This means that the loudest peaks on the PSD are always going to be snapping shrimp
shrimp_stamps, _ = find_peaks(psd, height=0.75*max_val, distance=50)

# Find the start of the very first group
# Initialize timestamps_groups as a 1x2 array
# Each row is a new group of glupping, with the format (starting time, ending time)
timestamps_groups = np.array([])
init_time_index = None
for init_time_index in range(0, timestamps.size-1):
    # Look for the first peak that has a closely clustered peak right after that, which indicates it's part of a group
    if t[timestamps[init_time_index+1]]-t[timestamps[init_time_index]] < 3:
        break
# Look fo rhte rest of the groups:
if init_time_index != None:
    start_time_index = init_time_index
    # Find the endpoints of every other group of glupping
    for time_index in range(init_time_index+1, timestamps.size-1):
        prev_time = t[timestamps[time_index-1]]
        next_time = t[timestamps[time_index+1]]
        current_time = t[timestamps[time_index]]
        # Find endpoints
        if next_time-current_time > 3 and current_time-prev_time < 3: # Make sure the previous peaks are clustered close and the next peaks are far
            timestamps_groups = np.append(timestamps_groups, timestamps[start_time_index:time_index+1])
        # Find startpoints
        if next_time-current_time < 3 and current_time-prev_time > 3: # Make sure the next peaks are clustered close and the previous peaks are far
            # timestamps_groups = np.append(timestamps_groups, timestamps[time_index])
            start_time_index = time_index

# print("--- %s seconds ---" % (time.time() - start_time)) #Check the runtime

# Plot peaks
fig = plt.plot(t, psd)
axs = plt.axes()
if timestamps.size > 0:
    for time in np.nditer(shrimp_stamps):
        axs.axvline(t[int(time)], color='red', ymax=0.5) #plot the highest peaks (shrimp peaks) in red vertical lines
if timestamps_groups.size > 0:
    for time in np.nditer(timestamps_groups):
        axs.axvline(t[int(time)], color='green', ymax=0.5) #Plot the start and end points of each group of glupping in green
plt.show()
