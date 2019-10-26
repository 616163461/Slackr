'''
Function name: message_remove()
Parameters: (token, message_id)
Return type: {}
Exception: ValueError when:
- Message (based on ID) no longer exists
AccessError when:
- Message with message_id was not sent by the authorised user making this request
- Message with message_id was not sent by an owner of this channel
- Message with message_id was not sent by an admin or owner of the slack
Description: Given a message_id for a message, this message is removed from the channel
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


def message_remove(token, message_id):
    data = getData()
    #Test for valid token
    flag = 0
    for user in data['users']:
        if str(user['token']) == token and token != None:
            u_id = user['u_id']
            perm_id = user['permission_id']
            flag = 1

    if flag == 0:
        myexcept.token_error()

    # find channel_id
    for channel in data['channels']:
        for message in channel['messages']:
            channel_id = channel['channel_id']
            if str(message['message_id']) == message_id:
                break

    # checking token belongs to an owner
    send_Success = False
    for channel in data['channels']:
        if channel['channel_id'] == channel_id:
            for owner in channel['owner_members']:
                if owner['u_id'] == u_id:
                    send_Success = True

    if send_Success == False:
        raise ValueError("token does not belong to an owner.")

    send_Success = False
    for channel in data['channels']:
        for message in channel['messages']:
            if str(message['message_id']) == message_id:
                if message['u_id'] == u_id:
                    send_Success = True
                    channel['messages'].remove(message)
                    updateData(data)
                    return sendSuccess({})

    if send_Success == False:
        raise ValueError("You cannot edit other users message, or message no longer exists.")