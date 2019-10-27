'''
Function name: user_profile_sethandle()
Parameters: (token, handle_str)
Return value: {}
Exception: ValueError when:
- handle_str is no more than 20 characters
Description: Update the authorised user's handle (i.e. display name)
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


def user_profile_sethandle(token, handle_str):
    if len(handle_str) >= 20 or len(handle_str) <= 3:
        raise myexcept.invalid_handle_str()

    data_new = getData()

    handle_str_used = 0
    for t in data_new['users']:
        if t['handle_str'] == handle_str:
            handle_str_used = 1

    if handle_str_used == 1:
        myexcept.registered_email()
    flag = 0
    for i in data_new['users']:
        if i['token'] == token and token != None:
            i['handle_str'] = handle_str
            flag = 1
            answer = {}
            updateData(data_new)
            return answer

    if flag == 0:
        myexcept.token_error()