import cv2, os

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def take_picture(num, storageDir = 'picture'):
    if not os.path.exists(storageDir): os.mkdir(storageDir)
    cap = cv2.VideoCapture(0)
    picNum = 1
    if not cap.isOpened(): print('Cap failed because of camera')

    while 1:
        ret, img = cap.read()
        cv2.imshow('Image',img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord(' '):
            cv2.imshow('Capture Image', img)
            if num < picNum: break
            faces = detect_face(img):
            if len(faces) == 1:
                cv2.imwrite(os.path.join(storageDir, 'pic%s.jpg'%picNum), img)
                picNum += 1
            elif not faces:
                print('No face found')
            else:
                print('More than one face found')
    cap.release()
    cv2.destroyAllWindows()

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    return faces
