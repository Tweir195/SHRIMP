from scipy.io.wavfile import read
import os
from scipy.signal import stft
from scipy.signal import spectrogram
import matplotlib.pyplot as plt
import numpy as np

freq_cap=10000

sample_rate = 0
data = np.ndarray([])
#import data & convert .wav to arrays
for root, dirs, files in os.walk(r'P:\+Courses\AstroStats\LivingSeaSculpture\Initial Data for Testing'):
    for name in files:
        # print(os.path.abspath(os.path.join(root, name)))
        if name == "Boat_Test.wav":
        #if name == "FFT_Test_2.wav":
            [sample_rate, data] = read(os.path.abspath(os.path.join(root, name)))

#define data sample range
data_sample = data[11*sample_rate:24*sample_rate, 0]

#############################################################################
#run short time fourier transform on time range
f, t, Zxx = stft(data_sample, fs=sample_rate)
#print(Zxx.shape)

#filter out anything above a certain frequency
for freq in f:
    if freq > freq_cap:
        index = int(np.where(f == freq)[0])
        break
Zxx = Zxx[:index]
f = f[:index]

#calculate power spectral density (psd)
psd = np.array([])
for slice in range(0, len(t)):
    psd = np.append(psd, np.trapz(np.abs(Zxx[:, slice]), f))
timestamps = np.where(psd > 300000)[0]

timestamps_clean = np.array([])

#eliminate duplicate peaks
current_val = timestamps[0]
last_val = t[timestamps[0]]
for time_index in range(1, timestamps.size):
    # print(last_val)
    # print(t[timestamps[time_index]])
    if last_val >= t[timestamps[time_index]] - 0.1:
        last_val = t[timestamps[time_index]]
        continue
    else:
        timestamps_clean = np.append(timestamps_clean, current_val)
        current_val = timestamps[time_index]
        last_val = t[timestamps[time_index]]
#print(timestamps)
#print(timestamps_clean)

#fig1 = plt.plot(t, psd)
#axs1 = plt.axes()
#for time in np.nditer(timestamps_clean):
#    axs1.axvline(t[int(time)], color='red', ymax=0.5)
#plt.show()

######################################################################################################################
#take spectrogram for boat noises
f_s, t_s, Sxx = spectrogram(data_sample, fs=sample_rate)
#for y in data_sample:
#    print(y)
#for x in Sxx:
#    print(x)
#print(Sxx)
print(f_s)
#print(t_s)


#filter out anything above a certain frequency
for freq in f_s:
    if freq > freq_cap:
        index = int(np.where(f_s == freq)[0])
        break
Sxx = Sxx[:index]
f_s = f_s[:index]


#plt.pcolormesh(t_s, f_s, Sxx)
#plt.ylabel('Frequency [Hz]')
#plt.xlabel('Time [sec]')
#plt.show()