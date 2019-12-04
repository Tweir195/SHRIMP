# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Function Definition
def makegraph(boat,shrimp,fish,cliplength,time_interval):
    """ This function takes in the amplitude over time of boats, the times that shrimp were heard, and the times in which fish were heard
    and then outputs a plot of that data

    boat: list of numpy arrays with the first entry being time and the second entry being the noise levels
    shrimp: 1D numpy array of timestamps shrimp were heard
    fish: 1D numpy array of timestamps fish were heard
    cliplength: int of the length of clip
    time_interval: int of the length of one discrete bucket of time

    """
    # GENERATE DATA STUFF------------------------------------------------------------------------------------------------------------------
    # Create an xaxis to unify the plots between 0 and 100 seconds with 5 second intervals
    xaxis = np.array(range(0,int(cliplength),int(time_interval)))

    # Generate numbers of shrimp and fish in each bucket in the x axis
    [hist_points_shrimp, null] = np.histogram(shrimp, bins=xaxis)
    [hist_points_fish, null] = np.histogram(fish, bins=xaxis)

    # Remove all 0 points
    for i in range(0,len(xaxis)-1):
        if hist_points_shrimp[i] == 0:
            hist_points_shrimp[i] = np.nan
        if hist_points_fish[i] == 0:
            hist_points_fish[i] = np.nan
    
    # GENERATE PLOT STUFF------------------------------------------------------------------------------------------------------------------
    # Initialize plot, generate one set of axes for the shrimp and fish
    fig, ax1 = plt.subplots()
    ax1.tick_params(axis='y')

    # Create a second set of axes for the boat sound level
    ax2 = ax1.twinx()
    ax2.tick_params(axis='y')

    # Label everything
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Times Entity Heard')
    ax2.set_ylabel('Relative Boat Volume')
    plt.title('Noises from Marine Life in Conjunction with Boats')

    # Plot "histogram" of shrimp noises as points over time
    shrimp_dots = ax1.plot(xaxis, np.insert(hist_points_shrimp,0,0), color='orange', marker='.', linewidth=0, markersize=12)

    # Plot fish noises with duration as the dot size
    fish_dots = ax1.plot(xaxis, np.insert(hist_points_fish,0,0), '.', markersize=12)

    # Plot boat noise over time as a line
    line = ax2.plot(boat[0],boat[1],'k')

    # Tidy the graph, add a legend, and show plot
    fig.tight_layout()
    plt.legend(line+shrimp_dots+fish_dots,['Boat noise','Shrimp','Fish'])
    plt.show()
    print('Graphing Complete!')

# TEST DATA SECTION
if __name__ == "__main__":
    # Define a boat-like array
    time_boat = np.linspace(0,100,101)
    boat_data = norm.pdf(time_boat,loc=50,scale=10)
    boat_noise = [time_boat,boat_data]

    # Define a set of shrimp noises with timestamps
    time_shrimp = time_boat
    removal_indices = []
    for i in range(0,len(time_shrimp)):
        if np.random.randint(0,2) > 0:
            removal_indices.append(i)
    time_shrimp = np.delete(time_shrimp,removal_indices)
    
    # Do all of that again to make fish noises
    time_fish = time_boat
    removal_indices = []
    for i in range(0,len(time_fish)):
        if np.random.randint(0,2) > 0:
            removal_indices.append(i)
    time_fish = np.delete(time_fish,removal_indices)

    # Plot
    makegraph(boat_noise,time_shrimp,time_fish,120,15)