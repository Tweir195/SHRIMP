"""This file is the main running file for our project
"""
# Import graph making function
#from boatfilt import *
from fishfilt import *
#from timestamp import *
from corrdata import *
from makegraph import *

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import os
from scipy.signal import stft
from scipy.signal.windows import hamming

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
newboat = corrdata(fakeboat,fakefish,2,1,3)
plt.plot(newboat,fakefish,'o')
plt.xlabel('Boat Noise')
plt.ylabel('Fish Noise')
plt.title('Boats vs. Fish, Test Data')
plt.show()