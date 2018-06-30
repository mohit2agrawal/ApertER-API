import cv2
import numpy as np
import pandas as pd

width, height = 48, 48

data = pd.read_csv('./fer2013.csv')
pixels = data['pixels'].tolist()

faces = []
for pixel_sequence in pixels:
    face = [int(pixel) for pixel in pixel_sequence.split(' ')]
    face = np.asarray(face).reshape(width, height)
    face = face / 255.0
    face = cv2.resize(face.astype('uint8'), (width, height))
    faces.append(face.astype('float32'))

faces = np.asarray(faces)
faces = np.expand_dims(faces, -1)

emotions = pd.get_dummies(data['emotion']).as_matrix()