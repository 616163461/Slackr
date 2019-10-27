'''
Function name: user_profile()
Parameters: (token, u_id)
Return type: { email, name_first, name_last, handle_str }
Exception: ValueError when:
- User with u_id is not a valid user
Description: For a valid user, returns information
about their email, first name, last name, and handle
'''

import json
import myexcept


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

def user_profile(token, u_id):
    #Send Success
    data_new = getData()
    if testToken(token) == False:
        myexcept.token_error()

    for i in data_new['users']:
        if i['u_id'] == str(u_id):
            answer = {}
            answer['email'] = i['email']
            answer['first_name'] = i['first_name']
            answer['last_name'] = i['last_name']
            answer['handle_str'] = i['handle_str']
            return answer

    myexcept.invalid_user()