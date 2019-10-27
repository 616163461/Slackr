'''
Function: user_profile_setname()
Parameters: (token, name_first, name_last)
Return value: {}
Exception: ValueError when:
- name_first is more than 50 characters
- name_last is more than 50 characters
Description: Update the authorised user's first and last name
'''
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

def user_profile_setname(token, name_first, name_last):
    if len(name_first) >= 50 or len(name_first) <= 1:
        myexcept.name_first_invalid()
    if len(name_last) >= 50 or len(name_last) <= 1:
        myexcept.name_last_invalid()

    flag = 0
    data_new = getData()
    for i in data_new['users']:
        if i['token'] == token:
            i['first_name'] = name_first
            i['last_name'] = name_last
            flag = 1
            answer = {}
            updateData(data_new)
            return answer

    if flag == 0:
        myexcept.token_error()