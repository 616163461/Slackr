# Function name: message_pin()
# Parameters: (token, message_id)
# Return type: {}
# Exception: ValueError when:
# - message_id is not a valid message
# - The authorised user is not an admin
# - Message with ID message_id is already pinned
# AccessError when:
# - The authorised user is not a member of the channel that the message is within
# Description: Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend
#       
from flask import Flask, request
import json
# Have not implemented time
APP = Flask(__name__)

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

@APP.route('/message/pin', methods = ['POST'])    
def message_pin():
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    data_new = getData()
    flag = 0
    #Test for valid token
    for i in data_new['users']:
        if str(i['token']) == token and token != None:
            u_id = i['u_id']
            flag = 1
    if flag == 0:
        raise ValueError("Session has expired. Please refresh the page and login\n")
    
    #Test if message_id exists
    message_found = 0
    member_found = 0
   
    for j in data_new['channels']:
        #Finding the message
        for k in j['messages']:
            if str(k['message_id']) == message_id:
                message_found = 1
                #Testing to see if user is in the channel and has owner permission
                for l in j['owner_members']:
                    if l['u_id'] == u_id:
                        member_found = 1
                if member_found == 0:
                    raise ValueError("Member is not part of the channel")
                if k['is_pinned'] == True:
                    raise ValueError("Action could not be completed. Message is already pinned...\n")
                k['is_pinned'] = True
                answer = {}
                updateData(data_new)
                return sendSuccess(answer)       
    if message_found == 0:
       raise ValueError("Action could not be completed. Message ID could not be found...\n") 


if __name__ == '__main__':
    APP.run(port = 7878)

