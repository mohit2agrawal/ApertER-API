import cv2
from skimage import io

def fr_(url):
    image = io.imread(url)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
    return (format(len(faces)))


def main():
    test_image = "http://www.gstatic.com/tv/thumb/persons/835149/835149_v9_bb.jpg"
    print(json_(fr_(url=test_image)))

def json_(status,face=0,url=""):
    if(status=="fail"):
        json = '{"status": "error","data": null,"message": "An Error has occurred"}'
    else:
        json = '{"status": "success","data": {"url": "'+url+'","faces": "'+str(face)+'" },"message": null}'
    return json

if (__name__ == '__main__'):
    main()
