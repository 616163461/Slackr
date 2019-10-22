# Function name: auth_login()
# Parameters: (email, password)
# Return type: { u_id, token }
# Exception: ValueError when:
# - Email entered is not a valid email
# - Email entered does not belong to a user
# - Password is not correct
# Description: Given a registered users' email and password and generates a valid token for the user to remain authenticated
#

import re
from flask import Flask, request
import json
from werkzeug.exceptions import HTTPException
#from flask_cors import CORS

APP = Flask(__name__)


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

@APP.route('/auth/login', methods = ['POST'])
def auth_login():
    data = getData()
    email = request.form.get('email')
    password = request.form.get('password')

    if check(email) == False:
        raise ValueError('Error, email entered is not a valid email')

    flag = 0
    for user in data['users']:
        if user['email'] == email and flag == 0:
            flag = 1
            if user['password'] != password:
                raise ValueError('Error, password is not correct')
            u_id = user['u_id']
            user['token'] = generateToken(password)
            updateData(data)
            return sendSuccess({
                'u_id' : u_id,
                'token' : generateToken(password)
            })
    
    if flag == 0:
        raise ValueError('Error, email entered does not belong to a user')


def check(email):  
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if(re.search(regex,email)):  
        return True  
          
    else:  
        return False

if __name__ == "__main__":
    APP.run(port = 7878)

