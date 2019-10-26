'''
Function name: message_sendlater()
Parameters: (token, channel_id, message, time_sent)
Return type: {}
Exception: ValueError when:
- Channel (based on ID) does not exist
- Message is more than 1000 characters
- Time sent is a time in the past
Description: Send a message from authorised_user to the channel specified
by channel_id automatically at a specified time in the future
'''
import json
from datetime import datetime
import time
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


def message_sendlater(token, channel_id, messsage, time_sent):
    data = getData()
    
    #Test for valid message
    if len(message) > 1000:
        myexcept.invalid_message()

    #Test for valid token
    flag = 0
    for user in data['users']:
        if str(user['token']) == token and token != None:
            u_id = user['u_id']
            flag = 1

    if flag == 0:
        myexcept.token_error()

    #Test for valid time
    format = '%Y-%m-%d %H:%M:%S'
    present_time = datetime.now()
    send_time = datetime.strptime(time_sent, format)
    convert_present_time = datetime.strftime(present_time, format)
    present = datetime.strptime(convert_present_time, format)

    if send_time < present:
        myexcept.invalid_time()

    tdelta = send_time - present
    sendlater_time = present + tdelta
    delay_time = (sendlater_time - present).total_seconds()

    #Test if channel_id is valid and that user is in the channel_id
    channel_found = 0
    member_found = 0

    for channel in data['channels']:
        if str(channel['channel_id']) == channel_id:
            channel_found = 1
            for member in channel['all_members']:
                if member['u_id'] == u_id:
                    member_found = 1
                    time.sleep(delay_time)
                    answer = {
                        'message_id' : 1,
                        'u_id' : u_id,
                        'message' : message,
                        'time_created' : datetime.now(),
                        'reacts' : {},
                        'is_pinned' : False
                    }
                    channel['messages'].append(answer)
                    sendlater = {
                        'message_id' : answer['message_id']
                    }
                    updateData(data)
                    return sendlater

    if channel_found == 0:
        myexcept.channel_not_found()
    elif member_found == 0:
        myexcept.member_not_in_channel()