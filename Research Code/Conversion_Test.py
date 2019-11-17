import os
from librosa.core import load
from scipy.io.wavfile import read

for root, dirs, files in os.walk(r'P:\+Courses\AstroStats\LivingSeaSculpture'):
    for name in files:
        # print(os.path.abspath(os.path.join(root, name)))
        if name == "2019-01-06 13~00~00 - 00~55~00 EST LivingSeaSculptureLiveStreamAudio.mp3":
        # if name == "FFT_Test_2.wav":
            print(os.path.abspath(os.path.join(root, name)))
            data, sample_rate = load(os.path.join(root, name), sr=None)
print(sample_rate)