'''
Function name: message_send()
Parameters: (token, channel_id, message)
Return type: {}
Exception: ValueError when:
- Message is more than 1000 characters
Description: Send a message from authorised_user to the channel specified by channel_id
'''
import json
from random import randint
import myexcept
import datetime

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


def message_send(token, channel_id, message):
    if len(message) > 1000:
        myexcept.invalid_message()

    data_new = getData()
    flag = 0
    #Test for valid token
    for i in data_new['users']:
        if i['token'] == token and token != None:
            u_id = i['u_id']
            flag = 1
    if flag == 0:
        myexcept.token_error()

    #Test if channel_id is valid and that user is in the channel_id
    channel_found = 0
    member_found = 0
    for j in data_new['channels']:
        if str(j['channel_id']) == channel_id:
            channel_found = 1
            for k in j['all_members']:
                if k['u_id'] == u_id:
                    member_found = 1
                    answer = {}
                    # assuming message_id is randomly generated
                    message_id = randint(0, 1000000)
                    answer['message_id'] = message_id
                    answer['u_id'] = u_id
                    answer['message'] = message
                    answer['time_created'] = datetime.now()
                    answer['reacts'] = []
                    answer['is_pinned'] = False
                    for i in range(0, 50):
                        j['messages'].append(answer)
                    updateData(data_new)
                    return sendSuccess({'message_id' : message_id})
    if channel_found == 0:
        myexcept.channel_not_found()
    elif member_found == 0:
        myexcept.member_not_in_channel()