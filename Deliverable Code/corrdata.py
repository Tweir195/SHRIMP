def corrdata(boat,fish,cliplength,timebucket,samplerate,plot=False):
    """ This function takes in the amplitude over time of boats, and the number is fish heard per 
    time bucket and then prints the pearson correlation coefficient between the fish and boats 
    and returns the boat data in timebuckets

    boat: numpy array
    fish: numpy array
    cliplength: int of duration of clip in seconds
    timebucket: int of bucket size in seconds
    samplerate: int of samplerate in samples per second
    plot: True or False, if True outputs a plot
    """
    import numpy as np
    import scipy.stats as stats
    import matplotlib.pyplot as plt
    
    #Divide the timestamps of fish into buckets
    times = np.array(range(0,cliplength+1,timebucket))
    [fishbucket,null] = np.histogram(fish,bins=times)

    #We need to find how much boat noise there is per timestamp
    sampsize = timebucket*samplerate #Make sure we know how many values are in a second
    #print('Sample size', sampsize)
    remain = len(boat) % sampsize #Find out if our boat can be divided nicely
    if remain !=0: #Let's make sure we don't have a remainder
        boat = boat[0:-remain]
    chunksize = len(boat)/sampsize
    boatchunk = np.array_split(boat,chunksize) #We split the array into equal smaller arrays
    #print(boatchunk)
    boatnoise = []
    for each in boatchunk: #Find the mean in each time bucket so that it matches the fish data
        #print(each)
        if len(each)!= sampsize:
            print('The array was not divisible') #catch error
            break
        boatmean = np.mean(each)
        #print(each, boatmean)
        boatnoise.append(boatmean)
    
    #Correlate the two arrays, and output result
    if len(boatnoise) != len(fish):
        print('not the same length',len(boatnoise),len(fish)) #this catches a possible error
    [corr,null] = stats.pearsonr(boatnoise,fish)
    print('Pearson Correlation Coeff:',' %.2f' % corr)
    if plot ==True:
        plt.plot(newboat,fishbucket,'o')
        plt.xlabel('Boat Noise')
        plt.ylabel('Fish Noise')
        plt.title('Boats vs. Fish, Test Data')
        plt.show()
    return boatnoise
    #this might not be the best correlation, since it only finds linear correlations

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.stats as stats
    fakeboat = np.array([1,2,3,4,4,4,4,4,4,4,3,3,3,2,2,2,1,1,10])
    fakefish = np.array([3,1,1,2,2.5,3])

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


    newboat = corrdata(boat_noise,time_fish,100,5,1)
    plt.plot(newboat,time_fish,'o')
    plt.xlabel('Boat Noise')
    plt.ylabel('Fish Noise')
    plt.title('Boats vs. Fish, Test Data')
    plt.show()