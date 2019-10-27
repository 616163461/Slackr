'''
Function name: user_profile_setemail
Parameters: (token, email)
Return: {}
Exception: ValueError when:
- handle_str is no more than 20 characters
Description: Update the authorised user's email address
'''

import re
import json
import myexcept

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

def user_profile_setemail(token, email):
    data_new = getData()
    email_used = 0
    for t in data_new['users']:
        if t['email'] == email:
            email_used = 1

    if email_used == 1:
        myexcept.registered_email()
    flag = 0
    for i in data_new['users']:
        if i['token'] == token:
            if check(email) == False:
                myexcept.invalid_email()
            i['email'] = email
            flag = 1
            answer = {}
            updateData(data_new)
            return answer

    if flag == 0:
        myexception.token_error()

def check(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if re.search(regex, email):
        return True
    else:
        return False