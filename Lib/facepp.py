import requests, os, mimetypes, json, time

with open(os.path.join('Lib', 'facepp.json')) as f: configInfo = json.loads(f.read())
BASE_URL = configInfo['base_url']
API_KEY = configInfo['api_key']
API_SECRET = configInfo['api_secret']
BASE_PARAMS = {
    'api_key': API_KEY,
    'api_secret': API_SECRET, }

def upload_img(fileDirList, oneface = True):
    if not isinstance(fileDirList, list): fileDirList = [fileDirList]
    faceList = []
    for fileDir in fileDirList:
        url = '%s/detection/detect?api_key=%s&api_secret=%s&attribute=none'%(
                BASE_URL, API_KEY, API_SECRET)
        if oneface: url += '&mode=oneface'
        files = {'img': (os.path.basename(fileDir), open(fileDir, 'rb'),
                mimetypes.guess_type(fileDir)[0]), }
        r = requests.post(url, files = files)
        for face in json.loads(r.text)['face']: faceList.append(face['face_id'])
    return faceList

def create_person(personName = None, faceId = []):
    url = '%s/person/create'%BASE_URL
    params = {
        'api_key': API_KEY,
        'api_secret': API_SECRET, }
    if not personName is None: params['person_name'] = personName
    if faceId and isinstance(faceId, list): params['face_id'] = ','.join(faceId)
    r = requests.get(url, params = params)
    return json.loads(r.text)['person_id']

def delete_person(personName):
    url = '%s/person/delete'%BASE_URL
    params = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'person_name': personName}
    r = requests.get(url, params = params)

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
    return json.loads(r.text)['session_id']

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
    r = requests.get(url, params)
    return r.json()

def compare(faceId1, faceId2):
    url = '%s/recognition/compare'%BASE_URL
    params = BASE_PARAMS
    params['face_id1'] = faceId1
    params['face_id2'] = faceId2
    r = requests.get(url, params)
    return r.json()

# compare(upload_img('pic1.jpg'), upload_img('pic2.jpg'))
