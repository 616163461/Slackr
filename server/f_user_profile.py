# Function name: user_profile()
# Parameters: (token, u_id)
# Return type: { email, name_first, name_last, handle_str }
# Exception: ValueError when:
# - User with u_id is not a valid user
# Description: For a valid user, returns information about their email, first name, last name, and handle
#

from flask import Flask, request
import json

APP = Flask(__name__)

def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data
    
def sendSuccess(data):
    return json.dumps(data)

    

def testToken(token):
    #Testing to see if the token is authenticated
    data_new = getData()
    for i in data_new['users']:
        if i['token'] == token:
            return True

    return False
    
@APP.route('/user/profile', methods=['GET'])
def user_profile():
    #Send Success
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    
    data_new = getData()
    if testToken(token) == False:
        raise ValueError
        
    for i in data_new['users']:
        if i['u_id'] == str(u_id):
            answer = {}
            answer['email'] = i['email']
            answer['first_name'] = i['first_name']
            answer['last_name'] = i['last_name']
            answer['handle_str'] = i['handle_str']
            print("Successfully found profile!\n")
            return sendSuccess(answer)
    

    print("Not a valid user\n")
    new_answer = "Not a valid user"
    return sendSuccess(new_answer)

@APP.route('/names', methods = ['GET'])    
def getnames():
    return sendSuccess(data)        



if __name__ == '__main__':
    APP.run(port = 7878)
    

