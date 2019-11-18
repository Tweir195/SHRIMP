import os
from pydub import AudioSegment

# files

for root, dirs, files in os.walk(r'C:\Users\ecusato\Music'):
    for name in files:
        # print(os.path.abspath(os.path.join(root, name)))
        #if name == "Boat_Test.wav":

        #if name == "FFT_Test_2.wav":
        #if name == "Symphony1.wav":
        if name == "Symphony1.mp3":
            break 
                                                                         
src = "Symphony1.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
