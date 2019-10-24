# Function name: auth_passwordreset_reset()
# Parameters: (reset_code, new_password)
# Return type: {}
# Exception: ValueError when:
# - reset_code is not a valid reset code
# - Password entered is not a valid password
# Description: Given a reset code for a user, set that user's new password to the password provided
#

from json import dumps
from flask import Flask, request

APP = Flask(__name__)

data = {
    'users' : [ {'token' : '123456', 'handle_str' : 'richardjiang', 'first_name' : 'Richard', 'last_name' : 'Jiang', 'password' : 'hello12345', 'email' : 'richard@email.com', 'u_id' : '22222', 'reset_code' : None} , 
                {'token' : '654321', 'handle_str' : 'danielyang', 'first_name' : 'Daniel', 'last_name' : 'Yang', 'password' : 'mixedsignals', 'email' : 'dy@email.com', 'u_id' : '11111', 'reset_code' : 'danielyang'},
                {'token' : '678910', 'handle_str' : 'geoffreyhe', 'first_name' : 'Geoffrey', 'last_name' : 'He', 'password' : 'sohyun ', 'email' : 'geoffrey@email.com', 'u_id' : '77777', 'reset_code' : None},
                {'token' : '000000', 'handle_str' : 'mattma', 'first_name' : 'Matt', 'last_name' : 'Ma', 'password' : 'Thom&Jerry', 'email' : 'Matt@email.com', 'u_id' : '00000', 'reset_code' : None}
              ]
}

def getData():
    global data
    return data
    
# converting dictionary into string for flask
def sendSuccess(data):
    return dumps(data)

# simple placeholder throw error function 
def sendError(message):  
    return dumps({
        '_error' : message,
    })

@APP.route('/auth/passwordreset/reset', methods = ['POST'])
def auth_passwordreset_reset():
    
    reset_code = request.form.get('reset_code')
    new_password = request.form.get('new_password')
    mask = 0 
    user_list = data['users']
    if len(new_password) < 6:
        # raise error saying password is too short 
        return sendError("User's new password is too short , please re-enter valid password.")
    for user in user_list:
        if user['reset_code'] == reset_code:
            mask = 1
            # resetting user reset_code to None
            user['reset_code'] = None
            # changing user's password to new password
            user['password'] = new_password
            return 'Slackr password was successfully reset to ' + user['password'] + '.'
        
    if mask == 0: 
        # raise error saying email doesn't exist in database
        return sendError("User's reset code doesn't exist in the database, please try again.")
    
    return sendSuccess({})

if __name__ == '__main__':
    APP.run(port = 7878)
