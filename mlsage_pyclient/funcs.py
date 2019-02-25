import requests
import json

server_url = "http://178.62.239.103:3004"

def signIn(email, password):
    r = requests.post("{}/app/sign-in".format(server_url), data={"email": email, "password": password})
    try:
        return json.loads(r.text)["token"]
    except:
        pass
    raise Exception("Could not to sign in")

def sendSolution(token, courseId, lessonId, exerciseId, data):
    data['courseId'] = courseId
    data['lessonId'] = lessonId
    data['exerciseId'] = exerciseId

    r = requests.post("{}/app/data".format(server_url), headers = { 'Authorization': 'Bearer {}'.format(token) }, data=data)
    try:
        return json.loads(r.text)
    except:
        pass
    raise Exception("Could not send solutions")

def getSolutions(token):
    req = requests.get("{}/app/solutions".format(server_url),
                     headers = {
                         'Authorization': 'Bearer {}'.format(token)
                     })
    try:
        return json.loads(req.text)
    except:
        pass
    raise Exception("Could not get solutions")
