def corrdata(boat,fish):
    """ This function takes in the amplitude over time of boats, and the number is fish heard per time bucket
    and then outputs the STATS
    boat: numpy array
    fish: numpy array
    """
    #We need to find how much boat noise there is per timestamp
    #then we need to make arrays of the two datas to feed into the correlation function
    #Correlate the two arrays, and output result
    