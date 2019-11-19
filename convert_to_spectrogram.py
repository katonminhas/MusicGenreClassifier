import librosa
import os
import soundfile as sf
import numpy as np
from PIL import Image


genre_list = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]

#os.chdir("C:/Users/Katon/Documents/finalproject/AudioFiles/disco")
#
#filename = "disco03.wav"
#
#y, sr = sf.read(filename, dtype='float32')
#y=y.T
#y_22k = librosa.resample(y, sr, 22050)
#spect = librosa.feature.melspectrogram(y=y_22k, sr=sr,n_fft=2048, hop_length=512)
#spect = librosa.power_to_db(spect, ref=np.max)
#
#np.savetxt("testing.csv", spect, delimiter=",")




for genre in genre_list:
    directory = "C:/Users/Katon/Documents/finalproject/AudioFiles/" + genre + "/"
    os.chdir(directory)
    for filename in os.listdir(directory):
        y, sr = sf.read(filename, dtype='float32')
        y=y.T
        y_22k = librosa.resample(y, sr, 22050)
        spect = librosa.feature.melspectrogram(y=y_22k, sr=sr,n_fft=2048, hop_length=512)
        spect = librosa.power_to_db(spect, ref=np.max)
        spect = np.absolute(spect) * 4.5    #increase contrast

        np.savetxt(filename[:-4] + ".csv", spect, delimiter=",")
        
        