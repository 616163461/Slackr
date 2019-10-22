# Function name: user_profile_sethandle()
# Parameters: (token, handle_str)
# Return value: {}
# Exception: ValueError when: 
# - handle_str is no more than 20 characters
# Description: Update the authorised user's handle (i.e. display name)
#
from flask import Flask, request
import json

APP = Flask(__name__)

data = {
    'users' : [ {'token' : '123456', 'handle_str' : 'richardjiang', 'first_name' : 'Richard', 'last_name' : 'Jiang', 'password' : 'hash(hello12345)', 'email' : 'richard@email.com'} , {'token' : '654321', 'handle_str' : 'danielyang', 'first_name' : 'Daniel', 'last_name' : 'Yang', 'password' : 'mixedsignals', 'email' : 'dy@email.com'}]
}

def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

def sendSuccess(data):
    return json.dumps(data)
    
def updateData(data):
    with open('export.json', 'w') as FILE:
        json.dump(data, FILE)
    return 0

@APP.route('/user/profile/sethandle', methods = ['PUT'])    
def user_profile_sethandle():

    token = request.form.get('token')
    handle_str = request.form.get('handle_str')
    
    if len(handle_str) >= 20:
        raise ValueError("Error: String is longer than 20 characters")
        
    flag = 0
    data_new = getData() 
    for i in data_new['users']:
        if i['token'] == token and token != None:
            i['handle_str'] = handle_str
            flag = 1
            answer = {}
            updateData(data_new)
            return sendSuccess(answer)
    
    if flag == 0:
        print("Session has expired. Please refresh token\n")
        return sendSuccess("Error")
    else:
        print("Successfully changed personal details\n")


@APP.route('/names', methods = ['GET'])    
def getnames():
    return sendSuccess(data)



if __name__ == '__main__':
    APP.run(port = 7878)
    

