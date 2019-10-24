# Function name: user_profile_setemail
# Parameters: (token, email)
# Return: {}
# Exception: ValueError when:
# - handle_str is no more than 20 characters
# Description: Update the authorised user's email address
#
import re
import json
from flask import Flask, request

APP = Flask(__name__)

data = {
    'users' : [ {'token' : '123456', 'handle_str' : 'richardjiang', 'first_name' : 'Richard', 'last_name' : 'Jiang', 'password' : 'hash(hello12345)', 'email' : 'richard@email.com', 'u_id' : '22222'} , {'token' : '654321', 'handle_str' : 'danielyang', 'first_name' : 'Daniel', 'last_name' : 'Yang', 'password' : 'mixedsignals', 'email' : 'dy@email.com', 'u_id' : '11111'}]
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

@APP.route('/user/profile/setemail', methods = ['PUT'])
def user_profile_setemail():
    
    token = request.form.get('token')
    email = request.form.get('email')
    
    if check(email) == False:
        raise ValueError("Error: NOT a valid email. Terminating process")
        
    flag = 0
    data_new = getData() 
    for i in data_new['users']:
        if i['token'] == token:
            i['email'] = email
            flag = 1
            answer = {}
            updateData(data_new)
            return sendSuccess(answer)
    
    if flag == 0:
        print("Session has expired. Please refresh token\n")
        return sendSuccess("Error!")
    else:
        print("Successfully changed personal details\n")
        

@APP.route('/names', methods = ['GET'])    
def getnames():
    return sendSuccess(data)


def check(email):  
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if(re.search(regex,email)):  
        return True  
          
    else:  
        return False


if __name__ == '__main__':
    APP.run(port = 7720)


