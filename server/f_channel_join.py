'''
Function name: channel_join()
Parameters: (token, channel_id)
Return type: {}
Exception: ValueError when:
- Channel (based on ID) does not exist
- u_id does not refer to a valid user
AccessError when:
- channel_id refers to a channel that is private (when the authorised user is not an admin)
Description: Given a channel_id of a channel that the authorised
user can join, adds them to that channel
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

def channel_join(token, channel_id):
    data = getData()
    #Test for valid token
    flag = 0
    for user in data['users']:
        # If token is valid, get user's u_id, first name, last name
        if user['token'] == token and token != None:
            u_id = user['u_id']
            name_first = user['first_name']
            name_last = user['last_name']
            perm_id = user['permission_id']
            flag = 1

    if flag == 0:
        myexcept.token_error()

    channel_found = 0
    member_not_found = 0

    # search for the channel with channel_id
    for channel in data['channels']:
        if channel['channel_id'] == channel_id:
            if channel['is_public'] == False:
                if perm_id == '1' or perm_id == '2':
                    channel_found = 1
                    # search in channel members, if the user is not already in the channel
                    for member in channel['all_members']:
                        if member['u_id'] != u_id:
                            member_not_found = 1
                            add_user = {
                                'u_id' : u_id,
                                'name_first' : name_first,
                                'name_last' : name_last
                            }
                            channel['all_members'].append(add_user)
                            channel['owner_members'].append(add_user)
                            return {}
                else:
                    myexcept.private_channel_denied()
            elif channel['is_public'] == True:
                channel_found = 1
                # search in channel members, if the user is not already in the channel
                for member in channel['all_members']:
                    if member['u_id'] != u_id:
                        member_not_found = 1
                        if perm_id == '1' or perm_id == '2':
                            p_id = '1'
                        else:
                            p_id = '2'
                        add_user = {
                            'u_id' : u_id,
                            'name_first' : name_first,
                            'name_last' : name_last
                        }
                        channel['all_members'].append(add_user)
                        updateData(data)
                        return {}

    if channel_found == 0:
        myexcept.channel_not_found()
    elif member_not_found == 0:
        myexcept.member_in_channel()