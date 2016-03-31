from Lib.facepp import *
from Lib.cv2fn import take_picture

while 1:
    existPersonName = [person['person_name'] for person in get_person_list()]
    print('Here is the list of person recorded:\n' +
        '\n'.join(['* ' + personName for personName in existPersonName]) + '\nEnd of List')

    name = raw_input('What\'s the name of the account you want to set?(q to exit) ')
    if name == 'q': break

    if name in existPersonName:
        if raw_input('You will overwrite account [%s]?(y/n) '%name) == 'y':
            delete_person(name)
        else:
            continue

    picNum = int(raw_input('How much picture do you want to input as sample? ')) or 10
    pictureList = take_picture(picNum)

    faceIdList = upload_img(pictureList)
    print '%s samples are set'%len(faceIdList)
    personId = create_person(name, faceIdList)
    trainSession = begin_train_verify(personId)
    print('Account [%s] is set'%name)
    break

print('Bye~');
