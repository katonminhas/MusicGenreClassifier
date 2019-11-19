
import librosa
import os
import random


genre_list = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]


# Trim data to random 5 sec chunks
start_times = range(0,26) 

for genre in genre_list:
    directory = "C:/Users/Katon/Documents/finalproject/AudioFiles/" + genre + "/"
    for name in os.listdir(directory):
        filename = directory+name
        start_at = random.choice(start_times)
        y, sr = librosa.load(filename, sr=22050, mono=True, offset=start_at, duration=5.0)
        librosa.output.write_wav(filename,y,sr)


