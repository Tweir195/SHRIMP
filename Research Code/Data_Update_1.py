from scipy.io.wavfile import read
import os
from scipy import signal
import matplotlib.pyplot as plt

#Copied the following code from a StackOverflow question
#Import the audio file from Public
for root, dirs, files in os.walk(r'P:\+Courses\AstroStats\LivingSeaSculpture\Initial Data for Testing'): #Iterate through files in our testing folder
    for name in files:
        # print(os.path.abspath(os.path.join(root, name)))
        if name == "FFT_Test_2.wav": #If the file is the one we want:
            [sample_rate, data] = read(os.path.abspath(os.path.join(root, name))) #Open the file into a 2D array

print(data)
print(sample_rate)

data_sample = data[10*sample_rate:24*sample_rate, 0] #Restrict the data to a section of interest
f, t, Sxx = signal.spectrogram(data_sample, sample_rate) #Calculate the spectrogram
plt.pcolormesh(t, f, Sxx) #Plot the spectrogram
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()