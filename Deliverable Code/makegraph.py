# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Function Definition
def makegraph(boat,fish):
    """ This function takes in the amplitude over time of boats, and the number of fish heard per time bucket
    and then outputs a plot of that data
    boat: list of numpy arrays with the first entry being time and the second entry being the noise levels
    fish: numpy array of timestamps fish were heard
    """
    # Create an xaxis to unify the plots between 0 and 100 seconds with 5 second intervals
    xaxis = np.array(range(0,101,5))

    # Initialize plot, generate one set of axes for the fish
    fig, ax1 = plt.subplots()
    ax1.tick_params(axis='y')

    # Create a second set of axes for the boat sound level
    ax2 = ax1.twinx()
    ax2.tick_params(axis='y')

    # Label everything
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Fish Heard')
    ax2.set_ylabel('Boat Volume (dB)')
    plt.title('Test Plot')

    # Plot boat noise over time as a line
    line = ax2.plot(boat[0],boat[1])

    # Generate numbers of fish in each bucket in the x axis
    [hist_points, null] = np.histogram(fish, bins=xaxis)

    # Plot "histogram" as points over time
    dots = ax1.plot(xaxis, np.insert(hist_points,0,0), 'r.')

    # Tidy the graph, add a legend, and show plot
    fig.tight_layout()
    plt.legend(line+dots,['Boat noise','Fish heard'])
    plt.show()
    print('Graphing Complete!')

# TEST DATA SECTION
if __name__ == "__main__":
    # Define a boat-like array
    time_boat = np.linspace(0,100,101)
    boat_data = norm.pdf(time_boat,loc=50,scale=10)
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