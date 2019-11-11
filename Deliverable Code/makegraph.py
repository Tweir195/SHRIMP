# Function Definition
def makegraph(boat_time,boat_amp,fish):
    """ This function takes in the amplitude over time of boats, and the number of fish heard per time bucket
    and then outputs a plot of that data
    boat_time: numpy array
    boat_amp: numpy array
    fish: numpy array
    """
    plt.plot(boat_time,boat_amp)
    plt.show()

""" TEST SECTION
Delete before including in master python file
"""
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import pandas as pd

# Define a boat-like array
time_boat = np.linspace(0,100,101)
boat_data = norm.pdf(time_boat,loc=50,scale=10)

# Define a set of fish noises with timestamps
time_fish = time_boat
fish_array = np.empty(len(time_fish))
removal = []
for i in range(0,len(time_fish)):
    fish_array[i] = np.random.randint(0,2)
    if fish_array[i] > 0:
        removal.append(i)
time_fish = np.delete(time_fish,removal)

# Plot
makegraph(time_boat,boat_data,0)