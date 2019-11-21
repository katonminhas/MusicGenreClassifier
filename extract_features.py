import librosa
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf



genre_list = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]

row = 27
col = 1000
# preallocate arrays for total, percussive, and harmonic spectrograms (26 rows x 1000 cols)
total_spects = [[0 for j in range(col)] for i in range(row)]

count = 0

#file = open("C:/Users/Katon/Documents/finalproject/total_features.csv", 'w', newline=' ')

for genre in genre_list:
    directory = "C:/Users/Katon/Documents/finalproject/audio_files/" + genre + "/"
    for name in os.listdir(directory):
        filename = directory+name    # filename is the .wav file of the spectrogram for each song
        y, sr = sf.read(filename, dtype='float32')
        y=y.T
        y = librosa.resample(y, sr, 22050)
        
        # Get individual features
        tempo = librosa.beat.tempo(y=y, sr=sr)
        zcr = librosa.feature.zero_crossing_rate(y)
        sce = librosa.feature.spectral_centroid(y=y, sr=sr)
        spec_flat = librosa.feature.spectral_flatness(y=y) 
        chroma_freq = librosa.feature.chroma_stft(y=y, sr=sr)
        
        # might not use
        spec_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
        
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        
        
        total_spects[0][count] = tempo[0]
        total_spects[1][count] = np.mean(zcr)
        total_spects[2][count] = np.mean(sce)
        total_spects[3][count] = np.mean(spec_flat)
        total_spects[4][count] = np.mean(chroma_freq)
        total_spects[5][count] = np.mean(spec_contrast)
        
        x = 0
        for i in mfcc:
            total_spects[6 + x][count] = np.mean(mfcc[x])
            x += 1
        
        # add genre tag to index 26
        if genre == "blues":
            total_spects[26][count] = 0
        elif genre == "classical":
            total_spects[26][count] = 1
        elif genre == "country":
            total_spects[26][count] = 2
        elif genre == "disco":
            total_spects[26][count] = 3
        elif genre == "hiphop":
            total_spects[26][count] = 4
        elif genre == "jazz":
            total_spects[26][count] = 5
        elif genre == "metal":
            total_spects[26][count] = 6
        elif genre == "pop":
            total_spects[26][count] = 7
        elif genre == "reggae":
            total_spects[26][count] = 8
        elif genre == "rock":
            total_spects[26][count] = 9
            
        
        
        count += 1
    # end of name loop



np.savetxt("C:/Users/Katon/Documents/finalproject/total_features.csv", total_spects, delimiter=",")   

        
        
        
        

