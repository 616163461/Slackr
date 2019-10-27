'''
Function name: message_unpin()
Parameters: (token, message_id)
Return type: {}
Exception: ValueError when:
- message_id is not a valid message
- The authorised user is not an admin
- Message with ID message_id is already unpinned
AccessError when:
- The authorised user is not a member of the channel that the message is within
Description: Given a message within a channel, remove it's mark as unpinned
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


def message_unpin(token, message_id):
    data = getData()
    flag = 0
    
    # checking that token is an admin
    authorised_user_exists = False
    for user in data['users']:
        if str(user['token']) == token and token != None:
            auth_u_id = user['u_id']
            perm_id = user['permission_id']
            authorised_user_exists = True

    if authorised_user_exists == False:
        myexcept.auth_token_not_found()
        
    if perm_id == 3:
        myexcept.not_an_admin()
        
    #Test if message_id exists
    message_found = False
    member_has_admin = False
    member_found = False
    for channels in data['channels']:
        #Finding the message
        for messages in channels['messages']:
            if str(messages['message_id']) == message_id:
                message_found = True
                # checking if the authorised user is in the channel
                for members in channels['all_members']:
                    if members['u_id'] == auth_u_id:
                        member_found = True
                if member_found == False:
                    myexcept.member_not_in_channel()
                # checking if the message is already unpinned
                if messages['is_pinned'] == False:
                    myexcept.message_already_unpinned()
                messages['is_pinned'] = False
                answer = {}
                updateData(data)
                return answer
    # checking if the message_id exists
    if message_found == False:
        myexcept.message_not_found()