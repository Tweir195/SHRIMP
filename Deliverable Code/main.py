"""This file is the main running file for our project
"""
# Import graph making function
from boatfilt import *
from fishfilt import *
from timestamp import *
from corrdata import *
from makegraph import *
from makefile import *

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
from datetime import datetime
from scipy.io.wavfile import read
from scipy.signal import stft
from scipy.signal.windows import hamming
from scipy.signal import find_peaks

# Import the data
#Import the audio file from Public
for root, dirs, files in os.walk(r'P:\+Courses\AstroStats\LivingSeaSculpture\Initial Data for Testing'): #Iterate through files in our testing folder
    for name in files:
        # print(os.path.abspath(os.path.join(root, name)))
        if name == "FFT_Test_2.wav": #If the file is the one we want:
            [sample_rate, data] = read(os.path.abspath(os.path.join(root, name))) #Open the file into a 2D array

# Filter the data
boat = boatfilt(sample_rate,data)
[t, fish] = fishfilt(data,sample_rate)

# Timestamp the data
[shrimpstamps,fishstamps] = timestamp(t, fish)
print(fishstamps/sample_rate)

# Find correlation
#corrdata(boat,fish,12,1,sample_rate)

# Make the CSV file
#print(len(timestamps[0]),len(timestamps[1]))
#makefile(timestamps[0],boat,timestamps[1],'test_folder','testdata')

# Plot the output
makegraph(boat,shrimpstamps,fishstamps, 90)


"""
# Define a boat-like array
time_boat = np.linspace(0,100,101)
boat_data = stats.norm.pdf(time_boat,loc=50,scale=10)
boat_noise = [time_boat,boat_data]

# Define a set of fish noises with timestamps
time_fish = time_boat
fish_array = np.empty(len(time_fish))
removal_indices = []
for i in range(0,len(time_fish)):
    fish_array[i] = np.random.randint(0,2)
    if fish_array[i] > 0:
        removal_indices.append(i)
time_fish = np.delete(time_fish,removal_indices)

# Plot
makegraph(boat_noise,time_fish)

# Find correlation
corrdata(boat_noise[1],time_fish,100,5,1,True)
"""