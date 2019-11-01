'''
Function name: channel_invite()
Parameters: (token, channel_id, u_id)
Return type: {}
Exception: ValueError when:
- channel_id does not refer to a valid channel that the authorised user is part of.
- u_id does not refer to a valid user
Description: Invites a user (with user id u_id) to join a channel with ID channel_id.
Once invited the user is added to the channel immediately
What happens when the user invited is already a part of the channel?
'''
import json
import myexcept

# retrieve data from local data base 
def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

# converting dictionary into string for flask 
def sendSuccess(data):
    return json.dumps(data)

# updates the local data base 
def updateData(data):
    with open('export.json', 'w') as FILE:
        json.dump(data, FILE)
    return 0

def channel_invite(token, channel_id, u_id):
    data = getData()
    # checking that token is a valid user 
    authorised_user_exists = False
    for user in data['users']:
        if str(user['token']) == token and token != None:
            auth_u_id = user['u_id']
            perm_id = user['permission_id']
            authorised_user_exists = True

    if authorised_user_exists == False:
        myexcept.token_error()
    # checking that u_id is a valid user
    member_exists = False
    for user in data['users']:
        if user['u_id'] == u_id:
            name_first = user['first_name']
            name_last = user['last_name']
            member_exists = True
    
    if member_exists == False:
        myexcept.invalid_user()
        
        
    token_is_member = False
    valid_channel = False
    # checking authorised user is already a member of the channel
    for channel in data['channels']:
        if channel['channel_id'] == channel_id: 
            valid_channel = True
            for member in channel['all_members']:
                if member['u_id'] == auth_u_id:
                    token_is_member = True
    if valid_channel == False: 
        myexcept.channel_not_found()
    
    if token_is_member == False: 
        myexcept.authorised_member_not_in_channel()
        
    # adding user to channel
    for channel in data['channels']:
        if channel['channel_id'] == channel_id:
            add_user = {
                'u_id' : u_id,
                'name_first' : name_first,
                'name_last' : name_last
            }
            channel['all_members'].append(add_user)
            if perm_id == '1' or perm_id == '2':
                channel['owner_members'].append(add_user)
            updateData(data)
            return {}