from scipy.io.wavfile import read
import os
from scipy.signal import stft
from scipy.signal import spectrogram
import matplotlib.pyplot as plt
import numpy as np



def boatfilt(sample_rate, data,flag=False):
    """This function takes in a .WAV file and filters out background noise to output
    a numpy array of filtered data of boat noise
    sample_rate: int of units in samples per second
    data: multi-column array of audio data
    flag: boolean, set True if testing function
    """

    #TO DO:
    #Update the smoothing to take data from the center, instead of only datapoints in front


    ####################################### what is the original type of data? how do we convert/manipulate it?
    data_sample = data[:,0]

    #These are values that we chose to find the boat noises, they may not be perfect
    freq_cap=7000
    freq_floor=2000
    amp_cap=1e1

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

    # Cuts down data to the range of frequencies we are interested in
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

    boat_smooth = []
    f_s_smooth = []
    Sxx_smooth = []

    for i in range(0, (len(psd)-smoothness)):

        boat_smooth.append(max(psd[i:i+smoothness]))
        f_s_smooth.append(max(psd[i:i+smoothness]))
        Sxx_smooth.append(max(psd[i:i+smoothness]))

    t_s = t_s[0:len(psd)-smoothness]  

    if flag == True:
        return t_s, boat_smooth, f_s_smooth, Sxx_smooth
    else:
        return t_s, boat_smooth

if __name__ == "__main__":
    from scipy.io.wavfile import read
    import os
    from scipy.signal import stft
    from scipy.signal import spectrogram
    import matplotlib.pyplot as plt
    import numpy as np
    sample_rate = 0
    data = np.ndarray([])


    #import data & convert .wav to arrays
    for root, dirs, files in os.walk(r'P:\+Courses\AstroStats\LivingSeaSculpture\Initial Data for Testing'):
        for name in files:
            # print(os.path.abspath(os.path.join(root, name)))
            #if name == "Boat_Test.wav":

            #if name == "FFT_Test_2.wav":
            #if name == "Symphony1.wav":
            if name == "conv_through_VLC.wav":
                break

    [sample_rate, data] = read(os.path.abspath(os.path.join(root, name)))
    #Plots of spectrogram & psd with boatcheck line
    [times,boat,f_s,Sxx] = boatfilt(sample_rate,data,True)
    plt.figure()
    plt.subplot(2,1,1)
    plt.pcolormesh(times, f_s, Sxx)
    plt.ylabel('frequency [hz]')
    plt.xlabel('time [sec]')
    plt.title(name)

    plt.subplot(2,1,2)
    plt.plot(times, psd, times, boat)
    plt.show()
    plt.ylabel('psd')
    plt.xlabel('time [sec]')