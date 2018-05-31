# FACE RECOGNITION to test server ( work pending on build )



import cv2, sys, json
from skimage import io

def read_in():
    lines = sys.stdin.readlines()
    return json.loads(lines[0])

def img(url):
    image = io.imread(url)
    casc_path = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(casc_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    return (format(len(faces)))


def main():
    url = read_in()
    print("py   ")
    print(url)
    # url2 = "http://www.gstatic.com/tv/thumb/persons/835149/835149_v9_bb.jpg"
    img(url)


if __name__ == '__main__':
    main()






