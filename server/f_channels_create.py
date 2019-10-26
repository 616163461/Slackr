'''
Function name: channels_create()
Parameters: (token, name, is_public)
Return type: { channel_id }
Exception: ValueError when:
- Name is more than 20 characters long
Description: Creates a new channel with that name that is either a public or private channel
'''

import json
from random import randint
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


def channels_create(token, name, is_public):
    
    data = getData()
    valid_user = False
    # ValueError when name is more than 20 characters long as per the specs
    if len(channel_name) > 20:
        myexcept.channel_name_invalid()

    for users in data['users']:
        if users['token'] == token:
            name_first = users['first_name']
            name_last = users['last_name']
            u_id = users['u_id']
            valid_user = True

    if valid_user == False:
        myexcept.token_error()

    # assuming that channel_id's are randomly generated
    channel_id = randint(0, 10000)
    channels_list = data['channels']
    channels_list.append({'channel_id' : channel_id,
                          'channel_name' : channel_name,
                          'is_public' : is_public,
                          'owner_members' : [{'u_id' : u_id, 'name_first' : name_first,
                                              'name_last' : name_last}],
                          'all_members' : [{'u_id' : u_id, 'name_first' : name_first,
                                            'name_last' : name_last}],
                          'messages' : []
                         })
    updateData(data)
    return sendSuccess({'channel_id' : channel_id})