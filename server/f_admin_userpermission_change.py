# Function: admin_userpermission_change()
# Parameters: (token, u_id, permission_id)
# Output: {}
# Exception: ValueError when:
# - u_id does not refer to a valid user
# - permission_id does not refer to a value permission
# AccessError when:
# - The authorised user is not an admin or owner
# Description: Given a User by their user ID, set their permissions to new permissions described by permission_id
# 

from flask import Flask, request
from json import dumps
import myexcept

APP = Flask(__name__)

data = {
    'users' : [ {'token' : '123456', 'handle_str' : 'richardjiang', 'first_name' : 'Richard', 'last_name' : 'Jiang', 'password' : 'hello12345', 'email' : 'richard@email.com', 'u_id' : '22222', 'reset_code' : None, 'permission_id' : '3'} , 
                {'token' : '654321', 'handle_str' : 'danielyang', 'first_name' : 'Daniel', 'last_name' : 'Yang', 'password' : 'mixedsignals', 'email' : 'dy@email.com', 'u_id' : '11111', 'reset_code' : None, 'permission_id' : '1'},
                {'token' : '678910', 'handle_str' : 'geoffreyhe', 'first_name' : 'Geoffrey', 'last_name' : 'He', 'password' : 'sohyun ', 'email' : 'geoffrey@email.com', 'u_id' : '77777', 'reset_code' : None, 'permission_id' : '2'},
                {'token' : '000000', 'handle_str' : 'mattma', 'first_name' : 'Matt', 'last_name' : 'Ma', 'password' : 'Thom&Jerry', 'email' : 'Matt@email.com', 'u_id' : '00000', 'reset_code' : None, 'permission_id' : '2'},
                {'token' : '555555', 'handle_str' : 'hughchan', 'first_name' : 'Hugh', 'last_name' : 'Chan', 'password' : 'hughmongous', 'email' : 'hugh@email.com', 'u_id' : '33333', 'reset_code' : None, 'permission_id' : '1'}
              ],
    'channels' : [{ 'name' : 'COMP1531',
        'channel_id' : '123', 
        'owner_members' : [{'u_id' : '77777', 'name_first' : 'Geoffrey', 'name_last' : 'He', 'permission_id' : '1'}, {'u_id' : '22222', 'name_first' : 'Richard', 'name_last': 'Kang', 'permission_id' : '1'}], 
        'all_members' : [{'u_id' : '11111', 'name_first' : 'Daniel', 'name_last' : 'Kang', 'permission_id' : '2'}, {'u_id' : '00000', 'name_first' : 'Jack', 'name_last' : 'Ma', 'permission_id' : '2'}, {'u_id' : '77777', 'name_first' : 'Geoffrey', 'name_last' : 'He', 'permission_id' : '1'}, {'u_id' : '22222', 'name_first' : 'Richard', 'name_last': 'Kang', 'permission_id' : '1'}], 
        'messages' : [{'message_id' : '123', 'u_id' : '11111', 'message' : "Who's Joe?", 'time_created' : '12:00', 'reacts' : [{'react_id' : '1234', 'u_ids' : '1', 'is_this_user_reacted' : False}, {'react_id' : '1234', 'u_ids' : ['1', '2'], 'is_this_user_reacted' : True}], 'is_pinned' : True },
                      {'message_id' : '124', 'u_id' : '77777',  'message' : "JOE MAMA!", 'time_created' : '12:01', 'reacts' : [{'react_id' : '1235', 'u_ids' : ['1'], 'is_this_user_reacted' : False}], 'is_pinned' : True }],
        'stand_up' : [{'message_id' : '125', 'u_id' : '11111', 'message' : "Who's Joe?", 'time_created' : '12:15', 'reacts' : [{'react_id' : '1236', 'u_ids' : '11111', 'is_this_user_reacted' : False}, {'react_id' : '1236', 'u_ids' : ['11111', '22222'], 'is_this_user_reacted' : True}], 'is_pinned' : False }],
        'is_channel_private' : True
    }]
}

def getData():
    global data
    return data

def sendSuccess(data):
    return dumps(data)

@APP.route('/admin/userpermission/change', methods = ['POST'])
def admin_userperm_change():
    data = getData()
    token = request.form.get('token')
    permission_id = request.form.get('permission_id')
    u_id = request.form.get('u_id')
    
    #Test for valid token
    valid_token = False
    for user in data['users']:
        if user['token'] == token and token != None: 
            perm_id = user['permission_id']
            valid_token = True

    if valid_token == False:
        myexcept.token_error()

    if permission_id != '1' and permission_id != '2' and permission_id != '3':
        myexcept.invalid_permission_id()

    if perm_id != '1' and perm_id != '2':
        myexcept.edit_permission_denied()

    user_found = False
    for user in data['users']:
        if user['u_id'] == u_id:
            user_found = True
            user['permission_id'] = permission_id
            return sendSuccess({})

    if user_found == False:
        myexcept.invalid_user()

@APP.route('/data', methods = ['GET'])    
def getdataa():
    return sendSuccess(data)
        
if __name__ == '__main__':
    APP.run(port = 5999)

# Given a User by their user ID, 
# set their permissions to new permissions described 
# by permission_id