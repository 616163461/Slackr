'''
Function name: channel_details()
Parameters: (token, channel_id)
Return type: { name, owner_members, all_members }
Exception: ValueError when:
- Channel (based on ID) does not exist
AccessError when:
- Authorised user is not a member of channel with channel_id
Description: Given a Channel with ID channel_id that the authorised user is
part of, provide basic details about the channel
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


def channel_details(token, channel_id):
    data = getData()
    #Test for valid token
    flag = 0
    for user in data['users']:
        if str(user['token']) == token and token != None:
            u_id = user['u_id']
            flag = 1

    if flag == 0:
        myexcept.token_error()

    flag = 0
    flag2 = 0
    for channel in data['channels']:
        if str(channel['channel_id']) == channel_id:
            flag = 1
            for member in channel['all_members']:
                if member['u_id'] == u_id:
                    flag2 = 1
                    answer = {
                        'name' : channel['channel_name'],
                        'owner_members' : channel['owner_members'],
                        'all_members' : channel['all_members']
                    }
                    return sendSuccess(answer)

    if flag == 0 or flag2 == 0:
        myexcept.member_not_in_channel()