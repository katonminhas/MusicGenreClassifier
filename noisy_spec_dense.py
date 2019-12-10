import pandas as pd
import numpy as np
import keras


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# import keras
from keras import models
from keras import layers
from keras.layers import Dense, Flatten


train_data = pd.read_csv('C:/Users/Katon/Documents/finalproject/spectrograms/all_spects.csv', header=None)
test_data = pd.read_csv('C:/Users/Katon/Documents/finalproject/spectrograms/noisy_specs.csv', header=None)

X_train = train_data.iloc[:-1,]
X_train = np.transpose(X_train)

X_test = test_data.iloc[:-1,]
X_test = np.transpose(X_test)

labels = train_data.iloc[-1,:]
labels = np.transpose(labels)


# Convert labels to categorical one-hot encoding
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)


model =  models.Sequential()
model.add(Dense(64, activation='relu', input_dim=128))
model.add(Dense(32, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])



# Train the model, iterating on the data in batches of 32 samples
model.fit(X_train, one_hot_labels, epochs=25, batch_size=128)


test_loss, test_acc = model.evaluate(X_test,one_hot_labels)


print('test_acc: ',test_acc)
























