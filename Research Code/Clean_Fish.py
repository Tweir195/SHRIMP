from scipy.io.wavfile import read
import os
from scipy.signal import stft
from scipy.signal.windows import hamming
import matplotlib.pyplot as plt
import numpy as np

for root, dirs, files in os.walk(r'P:\+Courses\AstroStats\LivingSeaSculpture\Initial Data for Testing'):
    for name in files:
        #print(os.path.abspath(os.path.join(root, name)))
        if name == "FFT_Test_2.wav":
            [sample_rate, data] = read(os.path.abspath(os.path.join(root, name)))

data_sample = data[12*sample_rate:24*sample_rate, 0]
f, t, Zxx = stft(data_sample, fs=sample_rate)
for freq in f:
    if freq > 5000:
        index = int(np.where(f == freq)[0])
        break
Zxx = Zxx[:index]
f = f[:index]
print('Zxx.shape')
print(Zxx.shape)
# plt.pcolormesh(t, f, np.abs(Zxx))
# plt.ylim([0, 5])
# plt.show()

smoothness = 5 # This determines how wide the moving average is, higher is more filtered

#for i in range(len(Zxx[1,:])-smoothness): # A 2D moving floor, horizontal
#    Zxx[:,i] = min(sum(Zxx[:,i:i+smoothness]))

#for i in range(len(Zxx[:,1])-smoothness): # A 2D moving floor, vertical
#    Zxx[i,:] = min(sum(Zxx[i:i+smoothness,:]))


psd = np.array([])
for slice in range(0, len(t)):
    psd = np.append(psd, np.trapz(np.abs(Zxx[:, slice]), f))

pbar = np.mean(psd)

for i in range(0, len(psd)):
    psd[i] = psd[i]**2/pbar

for i in range(0, len(psd)-smoothness): # A moving average
    psd[i] = sum(psd[i:i+smoothness])/(smoothness+1)

#for i in range(0, len(psd)-smoothness): # A moving floor
#    psd[i] = min(psd[i:i+smoothness])


#timestamps = np.where(psd > 100000)
#print('timestamps')
#print(timestamps)
fig = plt.plot(t, psd)
axs = plt.axes()
#for time in np.nditer(timestamps):
    # print(time)
    #axs.axvline(t[int(time)], color='red', ymax=0.5)
plt.show()
