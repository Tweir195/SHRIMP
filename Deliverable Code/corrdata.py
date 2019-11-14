def corrdata(boat,fish,cliplength,timebucket,samplerate):
    """ This function takes in the amplitude over time of boats, and the number is fish heard per time bucket
    and then outputs the pearson correlation between the fish and boats
    boat: numpy array
    fish: numpy array
    cliplength: int of duration of clip in seconds
    timebucket: int of bucket size in seconds
    samplerate: int of samplerate in samples per second
    """
    import numpy as np
    import scipy.stats as stat
    
    #Divide the timestamps of fish into buckets
    #times = np.array(range(0,cliplength+1,timebucket))
    #np.histogram(fish,bins=times)

    #We need to find how much boat noise there is per timestamp
    sampsize = timebucket*samplerate #Make sure we know how many values are in a second
    print('Sample size', sampsize)
    remain = len(boat) % sampsize #Find out if our boat can be divided nicely
    if remain !=0: #Let's make sure we don't have a remainder
        boat = boat[0:-remain]
    chunksize = len(boat)/sampsize
    boatchunk = np.array_split(boat,chunksize) #We split the array into equal smaller arrays
    print(boatchunk)
    boatnoise = []
    for each in boatchunk: #Find the mean in each time bucket so that it matches the fish data
        print(each)
        if len(each)!= sampsize:
            print('The array was not divisible')
            break
        boatmean = np.mean(each)
        print(each, boatmean)
        boatnoise.append(boatmean)
    #print(boatnoise)
    #print('output length', len(boatnoise))
    
    #I need to have the timestamp length so that I can get accurate boat noise levels for each time
    #Correlate the two arrays, and output result
    if len(boatnoise) != len(fish):
        print('not the same length',len(boatnoise),len(fish))
    corr = stat.pearsonr(boatnoise,fish)
    print(corr)
    return boatnoise
    #this might not be the best correlation, since it only finds linear correlations

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plot
    test = np.array([1,2,3,2,1])
    fakeboat = np.array([1,2,3,4,4,4,4,4,4,4,3,3,3,2,2,2,1,1,10])
    fakefish = np.array([3,1,1,2,2.5,3])
    print('test length', len(test), len(fakeboat))
    newboat = corrdata(fakeboat,fakefish,2,1,3)
    plot.plot(newboat,fakefish)
    plot.xlabel('Boat Noise')
    plot.ylabel('Fish Noise')
    plot.title('Boats vs. Fish, Test Data')
    plot.show()