'''
Function name: auth_register()
Parameters: (email, password, name_first, name_last)
Return type: { u_id, token }
Exception: ValueError when:
- Email entered is not a valid email.
- Email address is already being used by another user
- Password entered is not a valid password
- name_first is more than 50 characters
- name_last is more than 50 characters
Description: Given a user's first and last name, email address, and password,
create a new account for them and return a new token for authentication in their session
'''

from random import randint
import json
import myexcept
import re
import hashlib

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

def auth_register(email, password, name_first, name_last):

    password = hashlib.sha256(password.encode()).hexdigest()
    # assuming u_id is random number between 1 - 100
    u_id = randint(1, 101)
    data = getData()
    flag = 0
    for user in data['users']:
        if user['email'] == email and flag == 0:
            flag = 1

    if flag == 1:
        myexcept.registered_email()

    if check(email) == False:
        myexcept.invalid_email()
    if len(password) < 6:
        myexcept.weak_password()
    if len(name_first) > 50 or len(name_first) < 1:
        myexcept.name_first_invalid()
    if len(name_last) > 50 or len(name_first) < 1:
        myexcept.name_last_invalid()

    data['users'].append({
        'token' : name_first + name_last,
        'handle_str' : name_first + name_last,
        'first_name' : name_first,
        'last_name' : name_last,
        'password' : password,
        'email' : email,
        'u_id' : u_id,
        'permission_id' : 3,
        'pass_reset_code': None
    })

    updateData(data)
    return {
        'u_id' : u_id,
        'token' : name_first + name_last
    }

def check(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if re.search(regex, email):
        return True
    else:
        return False
