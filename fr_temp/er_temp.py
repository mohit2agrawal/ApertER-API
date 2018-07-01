
#   importing libraries
import pandas as pd
import numpy as np
import cv2
from sklearn.model_selection import train_test_split

#   importing dataset
dataset = pd.read_csv("data/dataset.csv")

#   Preprocessing Data
pixels = dataset['pixels'].tolist()
width, height = 48, 48
faces = []
for pixel_sequence in pixels:
    face = [int(pixel) for pixel in pixel_sequence.split(' ')]
    face = np.asarray(face).reshape(width, height)
    face = face / 255.0
    face = cv2.resize(face.astype('uint8'), (width, height))
    faces.append(face.astype('float32'))

faces = np.asarray(faces)
faces = np.expand_dims(faces, -1)
emotions = pd.get_dummies(dataset['emotion']).as_matrix()

#   Spliting into test set and training set
X_train, X_test, y_train, y_test = train_test_split(faces, emotions, test_size=0.2, random_state=0)
