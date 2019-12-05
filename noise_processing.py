# import librosa
import pandas as pd
import numpy as np

import os
import csv

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# import keras
from keras import models
from keras import layers


train_data = pd.read_csv('C:/Users/Katon/Documents/finalproject/spectrograms/all_spects.csv', header=None)
test_data = pd.read_csv('C:/Users/Katon/Documents/finalproject/spectrograms/noisy_specs.csv', header=None)

X = train_data.iloc[:-1,:]
X = np.transpose(X)


# print(np.shape(X))
# print(np.shape(y))

X_train = X
X_test = test_data.iloc[:-1,:]
X_test = np.transpose(X_test)
y_train = test_data.iloc[-1,:]
y_test = test_data.iloc[-1,:]

model = models.Sequential()
model.add(layers.Dense(128, activation = 'relu', input_shape = (X_train.shape[1],)))

model.add(layers.Dense(64, activation='relu'))

model.add(layers.Dense(32, activation='softmax'))

#model.add(layers.Dense(10, activation = 'softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


history = model.fit(X_train, y_train, epochs=20, batch_size=128)

test_loss, test_acc = model.evaluate(X_test,y_test)

print('test_acc: ',test_acc)







































