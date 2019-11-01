'''
Function: admin_userpermission_change()
Parameters: (token, u_id, permission_id)
Output: {}
Exception: ValueError when:
- u_id does not refer to a valid user
- permission_id does not refer to a value permission
AccessError when:
- The authorised user is not an admin or owner
Description: Given a User by their user ID, set their permissions
to new permissions described by permission_id
'''

from json import dumps
import myexcept
import json

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


def admin_userperm_change(token, u_id, permission_id):
    data = getData()

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
            updateData(data)
            return {}

    if user_found == False:
        myexcept.invalid_user()