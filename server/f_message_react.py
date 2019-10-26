'''
Function name: message_react()
Parameters: (token, message_id, react_id)
Return type: {}
Exception: ValueError when:
- message_id is not a valid message within a channel that the authorised user has joined
- react_id is not a valid React ID
- Message with ID message_id already contains an active React with ID react_id
Description: Given a message within a channel the authorised
user is part of, add a "react" to that particular message
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


def message_react(token, message_id, react_id):
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
            if str(k['message_id']) == message_id:
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
                    if len(react) != 0 and str(react['react_id']) == react_id:
                        react_check = 1
                        if u_id in react['u_ids']:
                            myexcept.message_already_reacted()
                        react['u_ids'].append(u_id)
                        if message_uid == u_id:
                            react['is_this_user_reacted'] = True
                        else:
                            react['is_this_user_reacted'] = False
                if react_check == 0:
                    answer = {}
                    answer['react_id'] = react_id
                    answer['u_ids'] = [u_id]
                    if message_uid == u_id:
                        answer['is_this_user_reacted'] = True
                    else:
                        answer['is_this_user_reacted'] = False
                    k['reacts'].append(answer)

                answer = {}
                updateData(data_new)
                return sendSuccess(answer)
    if message_found == 0:
       myexcept.message_not_found()