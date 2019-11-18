def makefile(times,boat,fish,foldername,filename):
    """This function takes in our filtered data and saves a .CSV file with
    the timestamps of fish noises
    times: numpy array of timestamps
    boat: numpy array of boat values
    fish: numpy array of fish values
    foldername: string of the folder you want data to be saved in, new file will 
        be created if it doesn't exist
    filename: string of the filename you want to be saved, new file will be created
        if it doesn't exist
    """
    import os
    import csv
    from datetime import datetime

    filepath = foldername + '/'
    if not os.path.exists(filepath):
        os.mkdir(filepath)

    #date = datetime.today().strftime('%Y-%m-%d')
    index = len(os.listdir(filepath)) #this makes sure that the file doesn't overwrite old files
    csvFile = filepath + filename + '_' + str(index) + '.csv'

    if not os.path.exists(csvFile):
        open(csvFile,'w',newline='')
    else:
        print('Warning: You are writing on a file that already exists.')
    
    with open(csvFile,'a',newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      writer.writerow(['Time','Boat','Fish'])
      for i in range(len(boat)):
        #I'm not sure if we need the time, boat, and fish to match length
        writer.writerow([times[i],boat[i],fish[i]])

if __name__ == "__main__":
    makefile([1,2,3],[2,2,2],[3,2,1],'test','test1')