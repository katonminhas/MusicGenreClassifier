
import pandas as pd
import numpy as np
import keras
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# import keras
from keras import models
from keras import layers
from keras.layers import Dense, Flatten, Conv2D


## read in spectrograms
genre_list = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
spectrograms = np.empty((1000,128,216))
i=0
for genre in genre_list:
    directory = "C:/Users/Katon/Documents/finalproject/spectrograms/" + genre + "/"
    
    for name in os.listdir(directory):
        filename = directory + name
        
        curr_spec = pd.read_csv(filename, header=None)
        
        spectrograms[i,:,:] = curr_spec
        i += 1
        
        
        
# Set up CNN data

# Get labels from last line of all_spects
labels = pd.read_csv('C:/Users/Katon/Documents/finalproject/spectrograms/all_spects.csv', header=None)
labels = labels.iloc[-1,:]
labels = np.transpose(labels)

one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

X_train, X_test, y_train, y_test = train_test_split(spectrograms, one_hot_labels, test_size = 0.2)

X_train = X_train.reshape(800,128,216,1)
X_test = X_test.reshape(200,128,216,1)

     
#   Build model
model = models.Sequential()

model.add(Conv2D(64, kernel_size = 3, activation='relu', input_shape = (128,216,1)))

model.add(Conv2D(32, kernel_size = 3, activation = 'relu'))

model.add(Flatten())

model.add(Dense(10, activation='softmax'))


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


# Train the model, iterating on the data in batches of 32 samples
model.fit(X_train, y_train, epochs=10, batch_size=128)


test_loss, test_acc = model.evaluate(X_test,y_test)


print('test_acc: ',test_acc)


