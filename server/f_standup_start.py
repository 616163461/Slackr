from datetime import datetime, timedelta
import json
import threading
import time
import myexcept
import f_standup_send

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

def timerAction():
    data = getData()
    timer = threading.Timer(1.0, standup_send)
    timer.start()
    updateData(data)

def standup_start(token, channel_id):
    data = getData()

    #Test for valid token
    token_valid = False
    for user in data['users']:
        if str(user['token']) == token and token != None:
            u_id = user['u_id']
            token_valid = True

    if token_valid == False:
        myexcept.token_error()

    now = datetime.now()
    present_time_str = datetime.strftime(now, '%H:%M')
    present_time = datetime.strptime(present_time_str, '%H:%M')

    present_time_dict = {
        'time_finish' : present_time_str
    }

    standup_end = present_time + timedelta(minutes = 15)

    standup_end_dict = {
        'time_finish' : standup_end
    }

    channel_found = False
    member_found = False

    for channel in data['channels']:
        if str(channel['channel_id']) == channel_id:
            channel_found = True
            if channel['standup_active'] == True:
                myexcept.active_stand_up()
            for member in channel['all_members']:
                if member['u_id'] == u_id:
                    member_found = True
                    channel['standup_active'] == True
                    # can't input more messages but can test for 1 message
                    while present_time_dict != standup_end_dict:
                        now_update = datetime.now()
                        present_time_str = datetime.strftime(now_update, '%H:%M')
                        present_time_dict = {
                            'time_finish' : present_time_str
                        } 
                        timerAction()
                    return sendSuccess(standup_end_dict)
    
    if channel_found == False:
        myexcept.channel_name_invalid()
    if member_found == False:
        myexcept.member_not_in_channel()
