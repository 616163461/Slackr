# Function name: channel_removeowner()
# Parameters: (token, channel_id, u_id)
# Return type: {}
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# - When user with user id u_id is not an owner of the channel
# AccessError when:
# - the authorised user is not an owner of the slackr, or an owner of this channel
# Description: Remove user with user id u_id an owner of this channel
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

@APP.route('/channel/removeowner', methods = ['POST'])
def channelRemoveOwner(): 

    data = getData()    
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')
    found_Token = False
    found_User = False
    # finding token and user data
    for user in data['users']:
        if str(user['token']) == token:
            tu_id = user['u_id']
            found_Token = True
        if str(user['u_id']) == u_id:
            name_first = user['first_name']
            name_last = user['last_name']
            found_User = True
            
    
    if found_User == False:
        raise ValueError("u_id not found in system.")
    if found_Token == False: 
        raise ValueError("token not found in system.")
        
    found_Token = False
    found_User = False
    # checking user and token belongs to an owner
    for channel in data['channels']:
        if str(channel['channel_id']) == channel_id: 
            for owner in channel['owner_members']:
                if owner['u_id'] == tu_id:
                    found_Token = True
                if str(owner['u_id']) == u_id:
                    found_User = True
    
    if found_Token == False: 
        raise ValueError("token does not belong to an owner.")
    if found_User == False:
        raise ValueError("u_id does not belong to an owner.")
 
    send_Success = False
    # remove user from owner_members list
    for channel in data['channels']:
        if str(channel['channel_id']) == channel_id: 
            channel['owner_members'].remove({'u_id' : u_id,
                'name_first' : name_first,
                'name_last' : name_last
            })
            send_Success = True
            updateData(data)
            return sendSuccess({})
    
    if send_Success == False: 
        raise ValueError("channel_id not found in system.")
            

        
if __name__ == '__main__':
    APP.run(port = 7878)

