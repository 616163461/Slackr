'''
Function name: auth_login()
Parameters: (email, password)
Return type: { u_id, token }
Exception: ValueError when:
- Email entered is not a valid email
- Email entered does not belong to a user
- Password is not correct
Description: Given a registered users' email and password
and generates a valid token for the user to remain authenticated
'''
import re
import json
from werkzeug.exceptions import HTTPException
import myexcept
import hashlib


def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

def generateToken(password):
    return password + '12345abcd'

# converting dictionary into string for flask
def sendSuccess(data):
    return json.dumps(data)

def updateData(data):
    with open('export.json', 'w') as FILE:
        json.dump(data, FILE)
    return 0

def auth_login(email, password):
    data = getData()
    password = hashlib.sha256(password.encode()).hexdigest()
    
    if check(email) == False:
        myexcept.invalid_email()

    flag = 0
    for user in data['users']:
        if user['email'] == email and flag == 0:
            flag = 1
            if user['password'] != password:
                myexcept.invalid_password()
            u_id = user['u_id']
            user['token'] = generateToken(password)
            updateData(data)
            return sendSuccess(
                'u_id' : u_id,
                'token' : generateToken(password)
            )

    if flag == 0:
        myexcept.not_registered_email()


def check(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if re.search(regex, email):
        return True
    else:
        return False