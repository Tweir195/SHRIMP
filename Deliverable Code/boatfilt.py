from scipy.io.wavfile import read
import os
from scipy.signal import stft
from scipy.signal import spectrogram
import matplotlib.pyplot as plt
import numpy as np



def boatfilt(sample_rate, data):
    """This function takes in a .WAV file and filters out background noise to output
    a numpy array of filtered data of boat noise
    rawdata: .WAV
    """
 

    #pass in data and sample_rate
    #pass out the overall max values

    ####################################### what is the original type of data? how do we convert/manipulate it?
    data_sample = data[20*sample_rate:6*60*sample_rate, 0]

    #take spectrogram for boat noises
    f_s, t_s, Sxx = spectrogram(data_sample, fs=sample_rate)


    #filter out anything above a certain frequency
    for freq in f_s:
        if freq > freq_cap: 
            index1 = int(np.where(f_s == freq)[0])
            break

    for freq in f_s:
        if freq > freq_floor:
            index2 = int(np.where(f_s == freq)[0])
            break

    Sxx = Sxx[index2:index1]
    f_s = f_s[index2:index1]

    for line in range(0,len(Sxx)):
        for amp in range(0,len(Sxx[line])):
            if Sxx[line][amp] > amp_cap:
                #index = int(np.where(Sxx == amp)[0])
                Sxx[line][amp]=0

   
    #calculate power spectral density (psd)
    psd = np.array([])
    for slice in range(0, len(t_s)):
        psd = np.append(psd, np.trapz(np.abs(Sxx[:, slice]), f_s))

    # NEW CONTENT STARTS HERE

    #this is really the smoothing coefficient, but we're not using it for smoothing
    smoothness = 100

    boatcheck = []

    for i in range(0, (len(psd)-smoothness)):

        boatcheck.append(max(psd[i:i+smoothness]))

    trime = t_s[0:len(psd)-smoothness]


    #Plots of spectrogram & psd with boatcheck line
    #plt.figure()
    #plt.subplot(2,1,1)
    #plt.pcolormesh(t_s, f_s, sxx)
    #plt.ylabel('frequency [hz]')
    #plt.xlabel('time [sec]')
    #plt.title(name)

    #plt.subplot(2,1,2)
    #plt.plot(t_s, psd, trime, boatcheck)
    #plt.show()
    #plt.ylabel('psd')
    #plt.xlabel('time [sec]')

    return t_s, boatcheck
