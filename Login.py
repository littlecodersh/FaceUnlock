import cv2, numpy, time

from Lib.facepp import *
from Lib.cv2fn import take_picture

def login():
    while 1:
        existPersonName = [person['person_name'] for person in get_person_list()]
        print('Here is the list of account:\n' +
            '\n'.join(['* ' + personName for personName in existPersonName]) + '\nEnd of List')
        account = raw_input('Account: ')
        if not account in existPersonName:
            print('No account matched')
        else:
            if login_as(account):
                print('Login successfully')
                break
            else:
                print('Login failed')

def login_as(name, timeout = 20):
    personId = get_person_id(name)
    if not os.path.exists('tmp'): os.mkdir('tmp')

    faceCascade = cv2.CascadeClassifier(os.path.join('Lib', 'haarcascade_frontalface_default.xml'))
    capInput = cv2.VideoCapture(0)
    if not capInput.isOpened(): print('Capture failed because of camera')
    endCaptureTime = time.time() + timeout
    success = False

    while 1:
        ret, img = capInput.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        if len(faces) > 0:
            picDir = os.path.join('tmp', 'pic.jpg')
            cv2.imwrite(picDir, img)
            pictureId = upload_img(picDir)
        if len(pictureId) > 0:
            while 1:
                result = verify(personId, pictureId)
                if not result.get('is_same_person') is None: break
            if result['is_same_person'] and result['confidence'] > 50: success = True;break
        if endCaptureTime < time.time(): break
    capInput.release()
    return success

if __name__ == '__main__':
    login()
