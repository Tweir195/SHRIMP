# Gulp Filter
# This code filters an audio file and makes it easier to identify fish noises.
# It does this by finding the Energy Spectral Density of the sound, which is
# calculated with a short time fourier transform. It then filters the spectral
# density data to make it even easier to identify the gulps.

from scipy.io.wavfile import read
import os
from scipy.signal import stft
from scipy.signal.windows import hamming
import matplotlib.pyplot as plt
import numpy as np

# We're storing our sound files in public, since there's no way a Colab notebook can handle them.
for root, dirs, files in os.walk(r'P:\+Courses\AstroStats\LivingSeaSculpture\Initial Data for Testing'):
    for name in files:
        if name == "FFT_Test_2.wav":
            [sample_rate, data] = read(os.path.abspath(os.path.join(root, name)))

# We know that from 12 to 24 seconds there are some interesting gulp noises
starttime = 12
endtime = 24
# Trim that massive file down to a more manageable size, in the interest of processing time
data_sample = data[starttime*sample_rate:endtime*sample_rate, 0]

# Short Time Fourier Transform, because the gulps are a higher frequency and amplitude than the background noise.
f, t, Zxx = stft(data_sample, fs=sample_rate)

# Anything above 5000 Hz is not a fish noise, it's most likely a whine produced by the hydrophone,
# so we don't want it to give us a false positive if we flag it as a really high-pitched gulp
for freq in f:
    if freq > 5000:
        index = int(np.where(f == freq)[0])
        break
Zxx = Zxx[:index]
f = f[:index]

# ESD is Energy Spectral Density, the total energy of the signal in a section of time based on amplitude
esd = np.array([])
for slice in range(0, len(t)):
    esd = np.append(esd, np.trapz(np.abs(Zxx[:, slice]), f))

# This isn't technically the mean energy of the sound, it's the mean spectral density
mean_energy = np.mean(esd)

# Square every value, then divide by the mean spectral density.
# This stretches any values above the mean (spiky gulps) and squashes values below the mean (background noise)
for i in range(0, len(esd)):
    esd[i] = esd[i]**2/mean_energy

# The 'smoothness' coefficient is how many data points we group together, so a higher value is a more powerful filter
smoothness = 10

# This is a simple moving average filter to get rid of some noise.
for i in range(0, len(esd)-smoothness):
    esd[i] = sum(esd[i:i+smoothness])/(smoothness+1)

# This is a moving floor we also tried; it functioned nearly identically to the moving average.
#for i in range(0, len(esd)-smoothness):
#    esd[i] = min(esd[i:i+smoothness])

# And let's plot it! Worth nothing that the Y axis is not showing the true ESD,
# which is fine because we only care about relative values. The numbers on the
# Y axis are meaningless.
plt.plot(t, esd)
plt.xlabel('Time')
plt.ylabel('Energy Spectral Density (Modified)')
plt.show()