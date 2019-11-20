def makefile(time,boat,fishstamps,foldername,filename):
    """This function takes in our filtered data and saves a .CSV file with
    the timestamps of fish noises
    boat: numpy array of boat values and timestamps
    fishstamps: numpy array of fish values
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
      writer.writerow(['Boat Time','Boat Value','Fish Timestamp'])
      for i in range(len(boat)):
          if i > len(fishstamps):
              writer.writerow([boat[i],boat[i],fishstamps[i]])
          #else:
          #    writer.writerow([boat[i,0],boat[i,1]])

if __name__ == "__main__":
    makefile([1,2,3],[2,2,2],[3,2,1],'test','test1')