import cv2
from skimage import io
import numpy as np
from keras.models import load_model

def er_(url):
    emotion = {0: "Angry", 1: "Disgust", 2: "Fear", 3: "Happy", 4: "Sad", 5: "Surprise", 6: "Neutral"}
    classifier = load_model('data/cnn.h5')
    image = io.imread(url)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)
        rgray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(rgray, (48, 48)), -1), 0)
        cv2.normalize(cropped_img, cropped_img, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
        prediction = classifier.predict(cropped_img)
        em = emotion[int(np.argmax(prediction))]
        
    return em


def main():
    test_image = "http://www.gstatic.com/tv/thumb/persons/835149/835149_v9_bb.jpg"
    print((er_(url=test_image)))
    
if (__name__ == '__main__'):
    main()
