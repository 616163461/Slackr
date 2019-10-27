'''
Function name: message_unreact()
Parameters: (token, message_id, react_id)
Return type: {}
Exception: ValueError when:
- message_id is not a valid message within a channel that the authorised user has joined
- react_id is not a valid React ID
- Message with ID message_id does not contain an active React with ID react_id
Description: Given a message within a channel the
authorised user is part of, remove a "react" to that particular message
'''
import json
import myexcept

def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

# converting dictionary into string for flask
def sendSuccess(data):
    return json.dumps(data)

def updateData(data):
    with open('export.json', 'w') as FILE:
        json.dump(data, FILE)
    return 0

def message_unreact(token, message_id, react_id):
    data_new = getData()
    flag = 0
    #Test for valid token
    for i in data_new['users']:
        if str(i['token']) == token and token != None:
            u_id = i['u_id']
            flag = 1
    if flag == 0:
        myexcept.token_error()

    #Test if message_id exists
    message_found = 0
    member_found = 0

    for j in data_new['channels']:
        #Finding the message
        for k in j['messages']:
            if k['message_id'] == message_id:
                message_uid = k['u_id']
                message_found = 1
                #Testing to see if user is in the channel and has owner permission
                for l in j['all_members']:
                    if l['u_id'] == u_id:
                        member_found = 1
                if member_found == 0:
                    myexcept.member_not_in_channel()
                react_check = 0
                for react in k['reacts']:
                    react_dic = react
                    if str(react['react_id']) == react_id:
                        print(f"\n\n\n\n\n {react_dic} \n\n\n\n\n\n")
                        k['reacts'].remove(react_dic)
                        react_check = 1
                    if message_uid == u_id:
                        react['is_this_user_reacted'] = False
                if react_check == 0:
                    myexcept.message_already_unreacted()
                answer = {}
                updateData(data_new)
                return answer
    if message_found == 0:
        myexcept.invalid_message_id()