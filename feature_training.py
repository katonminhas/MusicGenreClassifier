import pandas as pd
import numpy as np
import keras


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# import keras
from keras import models
from keras import layers
from keras.layers import Dense, Flatten


data = pd.read_csv('C:/Users/Katon/Documents/finalproject/feature_files/norm_total_features.csv', header=None)
X = data.iloc[:-1,]
X = np.transpose(X)

labels = data.iloc[-1,:]
labels = np.transpose(labels)


# Convert labels to categorical one-hot encoding
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

X_train, X_test, y_train, y_test = train_test_split(X, one_hot_labels, test_size = 0.2)


model =  models.Sequential()
model.add(Dense(64, activation='relu', input_dim=26))
model.add(Dense(32, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])



# Train the model, iterating on the data in batches of 32 samples
model.fit(X_train, y_train, epochs=50, batch_size=128)


test_loss, test_acc = model.evaluate(X_test,y_test)


print('test_acc: ',test_acc)

