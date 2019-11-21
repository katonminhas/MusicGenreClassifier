import librosa
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf




def get_features(y, sr, genre):
    column = [0 for i in range(27)]
    
    # Get individual features
    tempo = librosa.beat.tempo(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    sce = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_flat = librosa.feature.spectral_flatness(y=y) 
    chroma_freq = librosa.feature.chroma_stft(y=y, sr=sr)
    
    # might not use
    spec_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
        
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    
    column[0] = tempo[0]
    column[1] = np.mean(zcr)
    column[2] = np.mean(sce)
    column[3] = np.mean(spec_flat)
    column[4] = np.mean(chroma_freq)
    column[5] = np.mean(spec_contrast)
    
    x = 0
    for i in mfcc:
        column[6 + x] = np.mean(mfcc[x])
        x += 1
    
    # add genre tag to index 26
    if genre == "blues":
        column[26] = 0
    elif genre == "classical":
        column[26] = 1
    elif genre == "country":
        column[26] = 2
    elif genre == "disco":
        column[26] = 3
    elif genre == "hiphop":
        column[26] = 4
    elif genre == "jazz":
        column[26] = 5
    elif genre == "metal":
        column[26] = 6
    elif genre == "pop":
        column[26] = 7
    elif genre == "reggae":
        column[26] = 8
    elif genre == "rock":
        column[26] = 9
    
    return column
    
    


genre_list = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]

row = 27
col = 1000
# preallocate arrays for total, percussive, and harmonic spectrograms (26 rows x 1000 cols)
total_features = [[0 for j in range(col)] for i in range(row)]
total_harmonic = [[0 for j in range(col)] for i in range(row)]
total_percussive = [[0 for j in range(col)] for i in range(row)]

count = 0

#file = open("C:/Users/Katon/Documents/finalproject/total_features.csv", 'w', newline=' ')

for genre in genre_list:
    directory = "C:/Users/Katon/Documents/finalproject/audio_files/" + genre + "/"
    for name in os.listdir(directory):
        filename = directory+name    # filename is the .wav file of the spectrogram for each song
        y, sr = sf.read(filename, dtype='float32')
        y=y.T
        y = librosa.resample(y, sr, 22050)
        
        y_harmonic = librosa.effects.harmonic(y=y)
        y_percussive = librosa.effects.percussive(y=y)
        
        # Get the song features
        song_features = get_features(y, sr, genre)
        harmonic_features = get_features(y_harmonic, sr, genre)
        percussive_features = get_features(y_percussive, sr, genre)
        
        #Add to total arrays
        for i in range(27):
            total_features[i][count] = song_features[i]
            total_harmonic[i][count] = harmonic_features[i]
            total_percussive[i][count] = percussive_features[i]
            continue
        
        
        count += 1
    # end of name loop
#end of genre loop


np.savetxt("C:/Users/Katon/Documents/finalproject/total_features.csv", total_features, delimiter=",")   
np.savetxt("C:/Users/Katon/Documents/finalproject/harmonic_features.csv", total_harmonic, delimiter=",")
np.savetxt("C:/Users/Katon/Documents/finalproject/percussive_features.csv", total_percussive, delimiter=",")
        
        
        
        

