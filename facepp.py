import requests, os, mimetypes, json, time

BASE_URL = 'http://apicn.faceplusplus.com/v2'
API_KEY = ''
API_SECRET = ''
BASE_PARAMS = {
    'api_key': API_KEY,
    'api_secret': API_SECRET, }

def upload_img(fileDir):
    url = '%s/detection/detect?api_key=%s&api_secret=%s&mode=oneface&attribute=none'%(
            BASE_URL, API_KEY, API_SECRET)
    files = {'img': (os.path.basename(fileDir), open(fileDir, 'rb'),
            mimetypes.guess_type(fileDir)[0]), }
    r = requests.post(url, files = files)
    return json.loads(r.text)['face'][0]['face_id']

def create_person(personName = None, faceId = []):
    url = '%s/person/create'%BASE_URL
    params = {
        'api_key': API_KEY,
        'api_secret': API_SECRET, }
    if not personName is None: params['person_name'] = personName
    if faceId and isinstance(faceId, list): params['face_id'] = ','.join(faceId)
    r = requests.get(url, params = params)
    print r.text
    return json.loads(r.text)['person_id']

def get_person_list():
    url = '%s/info/get_person_list'%BASE_URL
    r = requests.get(url, params = BASE_PARAMS)
    return json.loads(r.text)['person']

def get_person_id(personName):
    personList = get_person_list()
    for person in personList:
        if person['person_name'] == personName: return person['person_id']

def begin_train_verify(personId = None, personName = None):
    if personId is None and personName is None: return
    url = '%s/train/verify'%BASE_URL
    params = BASE_PARAMS
    if not personId is None:
        params['person_id'] = personId
    else:
        params['person_name'] = personName
    r = requests.get(url, params = params)
    return r['session_id']

def get_session(sessionId):
    url = '%s/info/get_session'%BASE_URL
    params = BASE_PARAMS
    params['session_id'] = sessionId
    r = requests.get(url, params = params)
    return json.loads(r.text)

def verify(personId, faceId):
    url = '%s/recognition/verify'%BASE_URL
    params = BASE_PARAMS
    params['face_id'] = faceId
    params['person_id'] = personId
    r = request.get(url, params)
    return r.text

def compare(faceId1, faceId2):
    url = '%s/recognition/compare'%BASE_URL
    params = BASE_PARAMS
    params['face_id1'] = faceId1
    params['face_id2'] = faceId2
    r = requests.get(url, params)
    print r.text

def LittleCoder():
    name = 'LittleCoder'
    fileDir = 'pic.jpg'
    personId = get_person_id(name)
    if personId is None:
        faceId = upload_img(fileDir)
        personId = create_person('Geoff', faceId)
    trainSession = begin_train_verify(personId)
    print trainSession
    try:
        while 1:
            print get_session(trainSession)
            time.sleep(3)
    except:
        pass

compare(upload_img('pic1.jpg'), upload_img('pic2.jpg'))
