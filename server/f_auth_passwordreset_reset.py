'''
Function name: auth_passwordreset_reset()
Parameters: (reset_code, new_password)
Return type: {}
Exception: ValueError when:
- reset_code is not a valid reset code
- Password entered is not a valid password
Description: Given a reset code for a user, set that user's new password to the password provided
'''

import json
import myexcept

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

# simple placeholder throw error function
def sendError(message):
    return dumps({
        '_error' : message,
    })


def auth_passwordreset_reset(reset_code, new_password):
    mask = 0
    data = getData()
    user_list = data['users']
    if len(new_password) < 6:
        # raise error saying password is too short
        myexcept.weak_password()
    for user in user_list:
        if user['pass_reset_code'] == reset_code:
            mask = 1
            # resetting user reset_code to None
            user['pass_reset_code'] = None
            # changing user's password to new password
            user['password'] = new_password
            updateData(data)
            return {}

    if mask == 0:
        # raise error saying email doesn't exist in database
        myexcept.reset_code()

    return {}