import os
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

for root, dirs, files in os.walk(r'P:\+Courses\AstroStats\LivingSeaSculpture'):
    for name in files:
        if name == "conv_through_online.wav":
            # print(os.path.abspath(os.path.join(root, name)))
            [sample_rate, data] = read(os.path.abspath(os.path.join(root, name)))
        if name == "conv_through_VLC.wav":
            # print(os.path.abspath(os.path.join(root, name)))
            [sample_rate2, data2] = read(os.path.abspath(os.path.join(root, name)))

# time = np.arange(data[:,0].size)
# plt.plot(time, data)
# plt.figure()

f, t, Sxx = signal.spectrogram(data[:, 0], sample_rate)
plt.pcolormesh(t, f, Sxx)
plt.ylim([0, 5000])
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.figure()
# f2, t2, Sxx2 = signal.spectrogram(data2[:, 0], sample_rate2)
# plt.pcolormesh(t2, f2, Sxx2)
# plt.ylim([0, 5])
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
plt.show()
