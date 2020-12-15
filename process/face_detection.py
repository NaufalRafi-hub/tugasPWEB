import argparse
import cv2 as cv

def load_classifier():
    return cv.CascadeClassifier('classifier/haarcascade_frontalface_default.xml'),cv.CascadeClassifier('classifier/haarcascade_eye.xml')

def detect(inputImg):
    img = cv.imread(inputImg)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faceCL, eyeCL = load_classifier()

    faces = faceCL.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eyeCL.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv.imshow('input',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Face detection process')
    parser.add_argument("-i", "--input", required=True, help="path to image file")
    args = vars(parser.parse_args())

    # print(args['input'])
    detect(args['input'])