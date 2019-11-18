from scipy.io.wavfile import read
import os
from scipy.signal import stft
from scipy.signal.windows import hamming
import matplotlib.pyplot as plt
import numpy as np

def fishfilt(data, sample_rate):
    """This function takes in an array of audio data file and filters out boats and background noise to output
    a numpy array of filtered data
    """
    
    data_sample = data[:, 0]

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

    return [t, esd]