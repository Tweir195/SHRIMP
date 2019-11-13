from scipy.io.wavfile import read
import os
from scipy.signal import stft
import matplotlib.pyplot as plt
import numpy as np

sample_rate = 0
data = np.ndarray([])

for root, dirs, files in os.walk(r'P:\+Courses\AstroStats\LivingSeaSculpture\Initial Data for Testing'):
    for name in files:
        # print(os.path.abspath(os.path.join(root, name)))
        if name == "FFT_Test_2.wav":
            [sample_rate, data] = read(os.path.abspath(os.path.join(root, name)))

psd = np.abs(data[10*sample_rate:24*sample_rate, 0])
print(psd)
t = np.linspace(0, 15, 14*sample_rate)

timestamps = np.where(psd > 1000)[0]

timestamps_clean = np.array([])

current_val = timestamps[0]
last_val = t[timestamps[0]]
for time_index in range(1, timestamps.size):
    if last_val >= t[timestamps[time_index]] - 0.1:
        last_val = t[timestamps[time_index]]
        continue
    else:
        timestamps_clean = np.append(timestamps_clean, current_val)
        current_val = timestamps[time_index]
        last_val = t[timestamps[time_index]]

fig = plt.plot(t, psd)
axs = plt.axes()
for time in np.nditer(timestamps_clean):
    axs.axvline(t[int(time)], color='red', ymax=0.5)
plt.show()