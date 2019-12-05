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
<<<<<<< HEAD
        if name == "FFT_Test.wav": #If the file is the one we want:
>>>>>>> 8a62b64d993124bc68fc778083681f6faa351367
            [sample_rate, data] = read(os.path.abspath(os.path.join(root, name))) #Open the file into a 2D array

# Filter the data
boat = boatfilt(sample_rate,data)
[t, fish] = fishfilt(data,sample_rate)

# Timestamp the data
[shrimpstamps,fishstamps] = timestamp(t, fish)

# Make the CSV file
# In progress
makefile(boat[0],boat[1],fishstamps,shrimpstamps,'test_folder','testdata')

# Plot the output
makegraph(boat,shrimpstamps,fishstamps, len(data[:,0])/sample_rate,15)