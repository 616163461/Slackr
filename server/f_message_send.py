# Function name: message_send()
# Parameters: (token, channel_id, message)
# Return type: {}
# Exception: ValueError when:
# - Message is more than 1000 characters
# Description: Send a message from authorised_user to the channel specified by channel_id
#

from flask import Flask, request
import json
from random import randint
# Have no implemented time
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


@APP.route('/message/send', methods = ['POST'])    
def message_send():
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    if len(message) > 1000:
        raise ValueError('Message contains too many characters\n')
    
    data_new = getData()
    flag = 0
    #Test for valid token
    for i in data_new['users']:
        if i['token'] == token and token != None:
            u_id = i['u_id']
            flag = 1
    if flag == 0:
        raise ValueError("Session has expired. Please refresh the page and login\n")
    
    #Test if channel_id is valid and that user is in the channel_id
    channel_found = 0
    member_found = 0
    for j in data_new['channels']:
        if str(j['channel_id']) == channel_id:
            channel_found = 1
            for k in j['all_members']:
                if k['u_id'] == u_id:
                    member_found = 1
                    answer = {}
                    # assuming message_id is randomly generated
                    message_id = randint(0, 1000000)
                    answer['message_id'] = message_id
                    answer['u_id'] = u_id
                    answer['message'] = message
                    answer['time_created'] = "12:04"
                    answer['reacts'] = []
                    answer['is_pinned'] = False
                    for i in range(0,50):
                        j['messages'].append(answer)
                    updateData(data_new)
                    return sendSuccess({'message_id' : message_id})
    if channel_found == 0:
       raise ValueError("Channel not found...")
    elif member_found == 0:
       raise ValueError("Action could not be completed. User does not belong in the channel...\n") 
                    
@APP.route('/data', methods = ['GET'])    
def getdataa():
    return sendSuccess(data)


if __name__ == '__main__':
    APP.run(port = 7878)

