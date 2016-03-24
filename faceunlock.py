from Lib.facepp import *
from Lib.cv2fn import take_picture

name = raw_input('What\'s your name?')
while 1:
    if get_person_id(name):
        if not raw_input('Do you want to reset samples?[y/n] ') == 'y':
            if test_login(name):
                print('Login sucessfully!')
            else:
                print('Login failed!')
            continue
    set_samples(name)

    
def set_samples(name):
    picNum = int(raw_input('How much picture do you want to input as sample? ')) or 10
    pictureList = take_picture(picNum)

    personId = get_person_id(name)
    if personId: delete_person(name)
    faceIdList = upload_img(pictureList)
    print '%s samples are set'%len(faceIdList)
    personId = create_person(name, faceIdList)
    trainSession = begin_train_verify(personId)

def test_login(name):
    personId = get_person_id(name)
    pictureList = take_picture(1)
    faceToVerifyId = upload_img(pictureList)[0]
    result = verify(personId, faceToVerifyId)
    return result['is_same_person'] and result['confidence'] > 80
