# Function: user_profile_setname()
# Parameters: (token, name_first, name_last)
# Return value: {}
# Exception: ValueError when: 
# - name_first is more than 50 characters
# - name_last is more than 50 characters
# Description: Update the authorised user's first and last name
#

from flask import Flask, request
import json

#from server import getData
'''
The data global variable
'''
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
    
    
@APP.route('/user/profile/setname', methods=['PUT'])
def user_profile_setname():
    
    token = request.form.get('token')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')
    
    if len(name_first) > 50 or len(name_last) > 50:
        raise ValueError
    flag = 0
    data_new = getData() 
    for i in data_new['users']:
        if i['token'] == token:
            i['first_name'] = name_first
            i['last_name'] = name_last
            flag = 1
            answer = {}
            updateData(data_new)
            return sendSuccess(answer)
    
    if flag == 0:
        print("Session has expired. Please refresh token\n")
        raise ValueError
    else:
        print("Successfully changed personal details\n")

        
@APP.route('/names', methods = ['GET'])    
def getnames():
    return sendSuccess(data)

if __name__ == '__main__':
    APP.run(port = 7878)
    

