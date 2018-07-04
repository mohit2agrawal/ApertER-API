#   importing libraries
import pandas as pd
import numpy as np
import cv2
from constants import *
from sklearn.model_selection import train_test_split
from keras.models import Sequential,load_model
from keras.layers import Convolution2D,MaxPooling2D,Flatten,Dense
from keras.callbacks import ModelCheckpoint


dataset = pd.read_csv("data/dataset.csv")

pixels = dataset['pixels'].tolist()

faces = []

for pixel_sequence in pixels:

    face = [int(pixel) for pixel in pixel_sequence.split(' ')]

    face = np.asarray(face).reshape(width, height)

    face = face / 255.0

    face = cv2.resize(face.astype('uint8'),
                      (width, height))

    faces.append(face.astype('float32'))


faces = np.asarray(faces)

faces = np.expand_dims(faces, -1)

emotions = pd.get_dummies(dataset['emotion']).as_matrix()

X_train, X_test, y_train, y_test = train_test_split(faces,
                                                    emotions,
                                                    test_size=0.2,
                                                    random_state=0)

classifier = Sequential()

classifier.add(Convolution2D(48,3,3,
                             input_shape=(width, height, 1),
                             activation='relu'))

classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Flatten())

classifier.add(Dense(output_dim = 192,
                     activation='relu'))

classifier.add(Dense(output_dim = 96,
                     activation='relu'))

classifier.add(Dense(output_dim = 7,
                     activation='softmax'))

classifier.compile(optimizer='adam',
                   loss='categorical_crossentropy',
                   metrics=['accuracy'])

checkpoint = ModelCheckpoint(model_path,
                             monitor='acc',
                             verbose=1,
                             save_best_only=True)

classifier.fit(np.array(X_train),
               np.array(y_train),
               batch_size=batch_size,
               epochs=epochs,
               callbacks=[checkpoint])

