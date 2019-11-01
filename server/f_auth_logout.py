'''
Function name: auth_logout()
Parameters: (token)
Return type: { is_success }
Exception: N/A
Description: Given an active token, invalidates the token to log the user out.
If a valid token is given, and the user is successfully logged out, it returns true,
otherwise false.
'''

import json

def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

# converting dictionary into string for flask
def sendSuccess(data):
    return json.dumps(data)

def updateData(data):
    with open('export.json', 'w') as FILE:
        json.dump(data, FILE)
    return 0

def auth_logout(token):
    data = getData()

    is_success = False

    for user in data['users']:
        if user['token'] == token:
            user['token'] = None
            is_success = True
    if is_success:
        updateData(data)
        return {
            'success' : is_success
        }