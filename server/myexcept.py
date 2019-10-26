"""

1) Run the flask server
2) Access /valueerror

Note: You may need to run "pip3 install flask_cors" for this to work

Would strongly recommend using this pattern for iteration 2

A lot of this code isn't meant to be fully explained by us - but you're
 welcome to do your own reading to make sense of it. The gist of it is that
 you can register an error handler, that is a function, and tell flask
 to call that function every time an exception of a certain type is thrown.
 What this code is saying to flask is "Every time you have an Exception
 thrown please call this particular function. In this case, our function is
  "defaultHandler" which just takes in an error type and packages it up
 to be sent to the frontend
"""

from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
from flask_cors import CORS
from json import dumps

def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.description,
    })
    response.content_type = 'application/json'
    return response

app = Flask(__name__)
app.config['TRAP_HTTP_EXCEPTIONS'] = True
app.register_error_handler(Exception, defaultHandler)
CORS(app)

class ValueError(HTTPException):
    code = 400
    message = 'No message specified'
    
class AccessError(HTTPException):
    code = 200
    message = 'No message specified'

# Post
def token_error():
    raise ValueError("Security Warning! \n Your submission token does not match your session token. \n This occurs when:\n - You are performing an action \n - Your session has expired \n - High security plugin is enabled (with CSRF protection)\n")

def auth_token_not_found():
    raise ValueError("Action could not be completed. Invalid token inputted...\n")

def member_not_in_channel():
    raise ValueError("Action could not be completed. Member is not in the channel...\n")

def member_in_channel():
    raise ValueError("Action could not be completed. Member is not already in in the channel...\n")

def authorised_member_not_in_channel():
    raise AccessError("Error! Authorised user is not already a member of the channel...")

def member_not_in_channel():
    raise AccessError("Error! Authorised user is not a member of the channe...\n")

def not_an_admin():
    raise ValueError("Error! The authorised user is not an admin...\n")

def channel_not_found():
    raise ValueError("Action could not be completed. Channel could not be found...\n")

def invalid_email():
    raise ValueError("Error! The email entered is not a valid email...\n")
 
def invalid_permission():
    raise ValueError("Action could not be completed. You do have the appropriate permission to make this change...\n")

def message_not_found():
    raise ValueError("Error! Message not found within channel...\n")

def invalid_message():
    raise ValueError("Please make your message shorter. The message limit is set to 1,000 characters...\n")

def invalid_time():
    raise ValueError("Please select a valid time. The input time is in the past...\n")

def invalid_user():
    raise ValueError("Error! The user you have entered does not refer to a valid user...\n")

def invalid_permission_id():
    raise ValueError("Error! Please enter a valid permission ID value...\n")

def invalid_password():
    raise ValueError("Incorrect password entered! Please try again...\n")

def registered_email():
    raise ValueError("The email you have entered has already been registered. Please try again..\n")

def not_registered_email():
    raise ValueError("The email you have entered does not belong to a user. Please try again..\n")

def weak_password():
    raise ValueError("Password has to be at least 6 characters long...\n")

def name_first_invalid():
    raise ValueError("First name has to be between 1-50 characters long...\n")

def name_last_invalid():
    raise ValueError("Last name has to be between 1-50 characters long...\n")

def reset_code():
    raise ValueError("Reset code is not valid...\n")

def start_message_invalid():
    raise ValueError("Error! The value you have input is larger than the total number of messages in the channel...\n")

def private_channel_denied():
    raise ValueError("Access denied! You are trying to access a private channel...\n")

def edit_permission_denied():
    raise ValueError("Access denied! You are not authorised to edit these permissions...\n")

def edit_message_denied():
    raise ValueError("Access denied! You are not authroised to edit this message...\n")

def remove_permission_denied():
    raise ValueError("Access denied! You are not authorised to remove these permissions...\n")

def owner_already():
    raise ValueError("Error! You are already an owner of this channel...\n")

def channel_name_invalid():
    raise ValueError("Error! Channel name has exceeded 20 characters...\n")

'''
'''

def invalid_react_id():
    raise ValueError("Error! The entered react ID is not a valid react ID...\n")

def message_already_reacted():
    raise ValueError("Error! You have already reacted to this message!...\n")

def message_already_unreacted():
    raise ValueError("Error! You have already unreacted to this message!...\n")

def invalid_message_id():
    raise ValueError("Error! The given message ID is not a valid message...\n")

def pin_permission_denied():
    raise ValueError("Access denied! You are not authorised to pin these permissions...\n")

def message_already_pinned():
    raise ValueError("Error! Message has already been pinned...\n")

def message_already_unpinned():
    raise ValueError("Error! Message has already been unpinned...\n") 

def invalid_handle_str():
    raise ValueError("Error! Username needs to be between 3 and 20 characters...\n")

def registered_handle_str():
    raise ValueError("The username you have entered has already been registered. Please try again..\n")

def active_stand_up():
    raise ValueError("Error! An active stand-up is already running within the channel...\n")

def inactive_stand_up():
    raise ValueError("Error! No active stand-ups are currently running within the channel...\n")

if __name__ == '__main__':
    app.run(debug=True)