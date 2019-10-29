'''
Function name: message_pin()
Parameters: (token, message_id)
Return type: {}
Exception: ValueError when:
- message_id is not a valid message
- The authorised user is not an admin
- Message with ID message_id is already pinned
AccessError when:
- The authorised user is not a member of the channel that the message is within
Description: Given a message within a channel, mark it as "pinned"
to be given special display treatment by the frontend
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


def message_pin(token, message_id):
    data = getData()
    
    # checking that token is an admin
    owner = False
    authorised_user_exists = False
    for user in data['users']:
        if user['token'] == token and token != None:
            auth_u_id = user['u_id']
            perm_id = user['permission_id']
            authorised_user_exists = True
    
    # find channel_id
    for channels in data['channels']:
        channel_id = channels['channel_id']
        for messages in channels['messages']:
            if messages['message_id'] == message_id:
                break
    
    # checking that token is an owner of the channel
    for channels in data['channels']:
        if channels['channel_id'] == channel_id:
            for owners in channels['owner_members']:
                if owners['u_id'] == auth_u_id:
                    owner = True
    
    
    if perm_id == 3 and owner == False:
        myexcept.not_an_admin()
    
    if authorised_user_exists == False:
        myexcept.auth_token_not_found()
    
    #Test if message_id exists
    message_found = False
    member_has_admin = False
    member_found = False
    for channels in data['channels']:
        #Finding the message
        for messages in channels['messages']:
            if messages['message_id'] == message_id:
                message_found = True
                # checking if the authorised user is in the channel
                for members in channels['all_members']:
                    if members['u_id'] == auth_u_id:
                        member_found = True
                if member_found == False:
                    myexcept.member_not_in_channel()
                # checking if the message is already pinned
                if messages['is_pinned'] == True:
                    myexcept.message_already_pinned()
                messages['is_pinned'] = True
                answer = {}
                updateData(data)
                return answer
     
   
    # checking if the message_id exists
    if message_found == False:
        myexcept.message_not_found()
