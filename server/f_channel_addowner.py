'''
Function name: channel_addowner()
Parameters: (token, channel_id, u_id)
Return type: {}
Exception: ValueError when:
- Channel (based on ID) does not exist
- When user with user id u_id is already an owner of the channel
AccessError when:
- the authorised user is not an owner of the slackr, or an owner of this channel
Description: Make user with user id u_id an owner of this channel
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


def channel_addowner(token, channel_id, u_id):
    data = getData()
    send_Success = False
    found_Token = False

    # finding user data
    for user in data['users']:
        if str(user['u_id']) == u_id:
            name_first = user['first_name']
            name_last = user['last_name']
            send_Success = True
        if str(user['token']) == token:
            tu_id = user['u_id']
            found_Token = True

    if send_Success == False:
        myexcept.invalid_user()


    if found_Token == False:
        myexcept.token_error()

    send_Success = False
    # checking token belongs to an owner
    for channel in data['channels']:
        if str(channel['channel_id']) == channel_id:
            for owner in channel['owner_members']:
                if owner['u_id'] == tu_id:
                    send_Success = True

    if send_Success == False:
        myexcept.token_error()

    send_Success = False
    # adding user to owner_members list
    for channel in data['channels']:
        if str(channel['channel_id']) == channel_id:
            channel['owner_members'].append({'u_id' : u_id,
                                             'name_first' : name_first,
                                             'name_last' : name_last
                                            })
            send_Success = True
            updateData(data)
            return sendSuccess({})

    if send_Success == False:
        myexcept.channel_not_found()