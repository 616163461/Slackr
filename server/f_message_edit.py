'''
Function name: message_edit()
Parameters: (token, message_id, message)
Return type: {}
Exception: N/A
Description: Given a message, update it's text with new text
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

def message_edit(token, message_id, message):
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

    send_Success = False

    flag = 0
    for findchannel in data['channels']:
        for findmessage in findchannel['messages']:
            channel_id = findchannel['channel_id']
            if str(findmessage['message_id']) == message_id:
                # checking if token is channel owner
                for channel in data['channels']:
                    if channel['channel_id'] == channel_id:
                        for owner in channel['owner_members']:
                            if owner['u_id'] == u_id:
                                send_Success = True
                if findmessage['u_id'] == u_id:
                    if perm_id == '1' or perm_id == '2' or send_Success:
                        flag = 1
                        findmessage['message'] = message
                        updateData(data)
                        return sendSuccess({})

    if flag == 0:
        myexcept.edit_message_denied()