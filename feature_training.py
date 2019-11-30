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


data = pd.read_csv('C:/Users/Katon/Documents/finalproject/feature_files/norm_total_features.csv')
X = data.iloc[:-1,:]
X = np.transpose(X)

genre = data.iloc[-1:,]
encoder = OneHotEncoder(categories = 'auto')
y = encoder.fit_transform(genre).toarray()
y = np.transpose(y)

# print(np.shape(X))
# print(np.shape(y))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

model = models.Sequential()
model.add(layers.Dense(256, activation = 'relu', input_shape = (X_train.shape[1],)))


#model.add(layers.Dense(128, activation='relu'))
#
#model.add(layers.Dense(64, activation='relu'))
#
model.add(layers.Dense(64, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


history = model.fit(X_train, y_train, epochs=10, batch_size=128)

test_loss, test_acc = model.evaluate(X_test,y_test)

print('test_acc: ',test_acc)



