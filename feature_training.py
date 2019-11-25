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


data = pd.read_csv('norm_total_features.csv')
X = data.iloc[:,:]
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
