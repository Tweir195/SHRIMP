def makefile(time,boat,fishstamps,shrimpstamps,foldername,filename):
    """This function takes in our filtered data and saves a .CSV file with
    the timestamps of fish noises
    time: numpy array of boat timestamps
    boat: numpy array of boat values
    fishstamps: numpy array of fish values
    shrimpstamps: numpy array of shrimp values
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

    index = len(os.listdir(filepath)) #this makes sure that the file doesn't overwrite old files
    csvFile = filepath + filename + '_' + str(index) + '.csv'

    if not os.path.exists(csvFile):
        open(csvFile,'w',newline='')
    
    with open(csvFile,'a',newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',')
      writer.writerow(['Boat Time (s)','Boat Value','Fish Timestamp (s)','Shrimp Timestamp (s)'])
      for i in range(len(boat)):
          if i < len(fishstamps) and i < len(shrimpstamps):
              writer.writerow([time[i],boat[i],fishstamps[i],shrimpstamps[i]])
          elif i < len(fishstamps) and i >= len(shrimpstamps):
              writer.writerow([time[i],boat[i],fishstamps[i]])
          elif i >= len(fishstamps) and i < len(shrimpstamps):
              writer.writerow([time[i],boat[i],0,shrimpstamps[i]])
          else:
              writer.writerow([time[i],boat[i]])

if __name__ == "__main__":
    makefile([1,2,3,4,5,5,5],[2,2,2,4,5,4,4],[3,2,1,4,4],[1,3,4,5,5,5],'test','test1')