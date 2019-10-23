# Function name: channel_invite()
# Parameters: (token, channel_id, u_id)
# Return type: {}
# Exception: ValueError when:
# - channel_id does not refer to a valid channel that the authorised user is part of.
# - u_id does not refer to a valid user
# Description: Invites a user (with user id u_id) to join a channel with ID channel_id. Once invited the user is added to the channel immediately
#

from flask import Flask, request
import json

APP = Flask(__name__)

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
    
@APP.route('/channel/invite', methods = ['POST'])
def channel_invite():
    data = getData()
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')

    #Test for valid token
    flag = 0
    for user in data['users']:
        if str(user['token']) == token and token != None: 
            member_user = user['u_id']   
            perm_id = user['permission_id']
            flag = 1

    if flag == 0:
        raise ValueError("Session has expired. Please refresh the page and login\n")

    for user in data['users']:
        if str(user['u_id']) == u_id:
            name_first = user['first_name']
            name_last = user['last_name']

    channel_found = 0
    member_found = 0

    for channel in data['channels']:
        if str(channel['channel_id']) == channel_id:
            channel_found = 1
            for member in channel['all_members']:
                if member['u_id'] == member_user:
                    member_found = 1
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
                    return sendSuccess({})

    if channel_found == 0:
        raise ValueError("Channel not found...")
    elif member_found == 0:
        raise ValueError("Action could not be completed. User does not belong in the channel...\n")


if __name__ == '__main__':
    APP.run(port = 7878)


