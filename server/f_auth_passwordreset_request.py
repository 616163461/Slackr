# Function name: auth_passwordreset_request()
# Parameters: (email)
# Return type: {}
# Exception: N/A
# Description: Given an email address, 
# if the user is a registered user, 
# send's them a an email containing a specific secret code, 
# that when entered in auth_passwordreset_reset, 
# shows that the user trying to reset the password is the one who got sent this email.
#


    
from flask import Flask, request
from flask_mail import Mail, Message
from json import dumps

APP = Flask(__name__)

data = {
    'users' : [ {'token' : '123456', 'handle_str' : 'richardjiang', 'first_name' : 'Richard', 'last_name' : 'Jiang', 'password' : 'hello12345', 'email' : 'richard@email.com', 'u_id' : '22222', 'reset_code' : None} , 
                {'token' : '654321', 'handle_str' : 'danielyang', 'first_name' : 'Daniel', 'last_name' : 'Yang', 'password' : 'mixedsignals', 'email' : 'dy@email.com', 'u_id' : '11111', 'reset_code' : None},
                {'token' : '678910', 'handle_str' : 'geoffreyhe', 'first_name' : 'Geoffrey', 'last_name' : 'He', 'password' : 'sohyun ', 'email' : 'geoffrey@email.com', 'u_id' : '77777', 'reset_code' : None},
                {'token' : '000000', 'handle_str' : 'mattma', 'first_name' : 'Matt', 'last_name' : 'Ma', 'password' : 'Thom&Jerry', 'email' : 'Matt@email.com', 'u_id' : '00000', 'reset_code' : None}
              ]
}

APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'snackathon123@gmail.com',
    MAIL_PASSWORD = "Where'smyHSP"
)

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
    
@APP.route('/auth/passwordreset/request', methods = ['POST'])
def auth_passwordreset_request():
    mail = Mail(APP)
    data = getData()
    email = request.form.get('email')
    mask = 0
    user_list = data['users']
    for user in user_list:
        if user['email'] == email:
            mask = 1
            first_name = user['first_name']
            last_name = user['last_name']
            # assuming that reset_code is handle_str
            reset_code = user['handle_str']
            try:
                msg = Message("Reset Slackr password",
                    sender="snackathon123@gmail.com",
                    recipients=["snackathon123@gmail.com"])
                msg.body = "Hey " + first_name + " " + last_name + "\n\n" + "Here's the special code to reset the password for your Slackr account.  \nSpecial code: " + reset_code + "\n\n" + "Kind Regards, \nSlackr Support Team"
                mail.send(msg)
                user['reset_code'] = reset_code
                return 'Slackr password reset code sent successfully!'
            except Exception as e:
                return (str(e))
            
    if mask == 0:
        # raise error saying email doesn't exist in database
        return sendError("User's email doesn't exist in the database, please try again.")
        
    return sendSuccess({})

if __name__ == '__main__':
    APP.run(port = 7878)
