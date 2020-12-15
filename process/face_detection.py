import argparse
import cv2 as cv

def load_classifier():
    return cv.CascadeClassifier('classifier/haarcascade_frontalface_default.xml'),cv.CascadeClassifier('classifier/haarcascade_eye.xml')

def detect(inputImg, show):
    img = cv.imread(inputImg)
    width = img.shape[0]
    height = img.shape[1]

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faceCL, eyeCL = load_classifier()
    check = False

    faces = faceCL.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        area = (x+w)*(y+h)
        if int((area/(width*height))*100) > 40:
            check = True
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eyeCL.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    if show:
        cv.imshow('input',img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        return check

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Face detection process')
    parser.add_argument("-i", "--input", required=True, help="path to image file")
    parser.add_argument("-s", "--show", action="store_true", help="to show image")
    args = vars(parser.parse_args())

    find = detect(args['input'], args['show'])
    print(find)