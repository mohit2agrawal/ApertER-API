import cv2
import numpy as np
from constants import *
from skimage import io
from keras.models import load_model


def er_(url):
    """emotion recognition
    identify emotion in the image

    Args:
        url (str): image url

    Returns:
        int: emotion
    """

    em = -1
    classifier = load_model(model_path)
    image = io.imread(url)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(casc_path)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)
        rgray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(rgray, (height, width)), -1), 0)
        cv2.normalize(cropped_img, cropped_img, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
        prediction = classifier.predict(cropped_img)
        em = int(np.argmax(prediction))
    return em

def fr_(url):
    """face recognition
    detect faces in the image

    Args:
        url (str): image url

    Returns:
        str: number of faces detected
    """

    image = io.imread(url)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
    return (format(len(faces)))

def json_(status, em=0, url=""):
    """[summary]

    Args:
        status (str): status string
        em (int, optional): Defaults to 0. emotion id
        url (str, optional): Defaults to "". url string

    Returns:
        str: the response json string
    """

    if status == "fail":
        json = '{"status": "error_fail","data": null,"message": "An Error has occurred"}'
    elif em == -1:
        json = '{"status": "error_no_face","data": null,"message": "No face found"}'
    else:
        json = '{"status": "success", "data": {"url": "'+url+'", "emotion": "'+str(emotion[em])+'" }, "message": "Successfully evaluated"}'
    return json

def main():
    test_image = "http://www.gstatic.com/tv/thumb/persons/835149/835149_v9_bb.jpg"
    em = er_(url=test_image)
    print(json_(status="success",em=em,url=test_image))


if __name__ == '__main__':
    main()
