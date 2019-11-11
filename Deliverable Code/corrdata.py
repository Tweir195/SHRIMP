def corrdata(boat,fish,timebucket,samplerate):
    """ This function takes in the amplitude over time of boats, and the number is fish heard per time bucket
    and then outputs the STATS
    boat: numpy array
    fish: numpy array
    timebucket: int of seconds per timebucket
    samplerate: int of samplerate in samples per second
    """
    import numpy as np
    import scipy.stats as stat
    
    #We need to find how much boat noise there is per timestamp
    sampsize = int(timebucket/samplerate)
    print(type(sampsize))
    boatnoise = []
    print(len(boat))
    for i in range(len(boat[0:-1])):
        print(i)
        boatnoise.append(np.mean(boat[i:i+sampsize]))

    #I need to have the timestamp length so that I can get accurate boat noise levels for each time

    #then we need to make arrays of the two datas to feed into the correlation function
    #Correlate the two arrays, and output result
import numpy as np
test = np.array([1,2,3,4,4,4,4,4,4,4,3,3,2,2])
test[1]
corrdata(test,1,2,3)