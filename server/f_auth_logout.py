# Function name: auth_logout()
# Parameters: (token)
# Return type: { is_success }
# Exception: N/A
# Description: Given an active token, invalidates the token to log the user out. 
# If a valid token is given, and the user is successfully logged out, it returns true, 
# otherwise false.
#

from flask import Flask, request
import json

APP = Flask(__name__)

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

@APP.route('/auth/logout', methods = ['POST'])
def auth_logout():
    data = getData()
    token = request.form.get('token')

    is_success = False

    for user in data['users']:
        if user['token'] == token:
            user['token'] = None
            is_success = True
    if is_success:
        updateData(data)
        return sendSuccess({
            'success' : is_success
        })

if __name__ == "__main__":
    APP.run(port = 7878)

