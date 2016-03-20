import cv2, numpy, time

print('Press SPACE to capture')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
imgWindow = cv2.namedWindow('FaceDetect', cv2.WINDOW_NORMAL)

def detect_face():
    capInput = cv2.VideoCapture(0)
    if not capInput.isOpened(): print('Capture failed because of camera')
    while 1:
        ret, img = capInput.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        for x, y, w, h in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('FaceDetect', img)
        while cv2.waitKey(1) & 0xFF != ord(' '): time.sleep(.1)
    capInput.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_face()
