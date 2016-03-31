import cv2, os

faceCascade = cv2.CascadeClassifier(os.path.join('Lib', 'haarcascade_frontalface_default.xml'))

def take_picture(num, storageDir = 'picture'):
    if not os.path.exists(storageDir): os.mkdir(storageDir)
    cap = cv2.VideoCapture(0)
    picNum = 1
    if not cap.isOpened(): print('Cap failed because of camera')

    print('Press **SPACE** to capture a picture')
    while 1:
        ret, img = cap.read()
        cv2.imshow('Image',img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord(' '):
            cv2.imshow('Capture Image', img)
            faces = detect_face(img)
            if len(faces) == 1:
                cv2.imwrite(os.path.join(storageDir, 'pic%s.jpg'%picNum), img)
                picNum += 1
            elif not faces:
                print('No face found')
            else:
                print('More than one face found')
            if picNum >= num: break
    cap.release()
    cv2.destroyAllWindows()
    return [os.path.join(storageDir, 'pic%s.jpg'%i) for i in range(1, num + 1)]

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    return faces
