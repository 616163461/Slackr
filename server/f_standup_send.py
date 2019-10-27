from datetime import datetime
import json
import threading
import time
import myexcept
import standup_start

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

def standup_send(token, channel_id, message):
    data = getData()

    token_valid = False
    for user in data['users']:
        if str(user['token']) == token and token != None:
            u_id = user['u_id']
            token_valid = True

    if token_valid == False:
        myexcept.token_error()

    if len(message) > 1000:
        myexcept.invalid_message()

    channel_found = False
    member_found = False

    standup_queue = []

    for channel in data['channels']:
        if str(channel['channel_id']) == channel_id:
            channel_found = True
            if channel['standup_active'] == False:
                myexcept.inactive_stand_up()
            for member in channel['all_members']:
                if member['u_id'] == u_id:
                    member_found = True
                    standup_start.standup_start(token, channel_id)
                    standup_queue.append(message)
                    return sendSuccess({})

    if channel_found == False:
        myexcept.channel_name_invalid()
    if member_found == False:
        myexcept.member_not_in_channel()
