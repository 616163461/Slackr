'''
Function name: channel_leave()
Parameters: (token, channel_id)
Return type: {}
Exception: ValueError when:
- Channel (based on ID) does not exist
Description: Given a channel ID, the user removed as a member of this channel
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

def channel_leave(token, channel_id):

    data_new = getData()

    flag = 0
    #Test for valid token
    for i in data_new['users']:
        if str(i['token']) == token and token != None:
            u_id = i['u_id']
            flag = 1
    if flag == 0:
        myexcept.token_error()

    member_found = 0
    channel_found = 0
    for channels in data_new['channels']:
        if str(channels['channel_id']) == channel_id:
            channel_found = 1
            for members in channels['all_members']:
                member_count = len(channels['all_members'])
                if members['u_id'] == u_id:
                    member_found = 1
                    if members in channels['owner_members']:
                        channels['owner_members'].remove(members)
                    channels['all_members'].remove(members)
                    if member_count == 1:
                        data['channels'].remove(channels)
                    answer = {}
                    updateData(data_new)
                    return sendSuccess(answer)
    if channel_found == 0:
        myexcept.channel_not_found()
    if member_found == 0:
        myexcept.member_not_in_channel()

    answer = {}
    return sendSuccess(answer)