'''
Function name: auth_passwordreset_request()
Parameters: (email)
Return type: {}
Exception: N/A
Description: Given an email address,
if the user is a registered user,
send's them a an email containing a specific secret code,
that when entered in auth_passwordreset_reset,
shows that the user trying to reset the password is the one who got sent this email.
'''

from flask_mail import Mail, Message
import json
import myexcept

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

# simple placeholder throw error function
def sendError(message):
    return dumps({
        '_error' : message,
    })

def auth_passwordreset_request(email):
    mail = Mail(APP)
    data = getData()
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
                msg.body = "Hey " + first_name + " " + last_name + "\n\n" + \
                "Here's the special code" + \
                " to reset the password for your Slackr account.  \nSpecial code: " + \
                reset_code + "\n\n" + "Kind Regards, \nSlackr Support Team"
                mail.send(msg)
                user['pass_reset_code'] = reset_code
                updateData(data)
                return sendSuccess({})
            except Exception as e:
                return str(e)

    if mask == 0:
        # raise error saying email doesn't exist in database
        myexcept.not_registered_email()

    return sendSuccess({})