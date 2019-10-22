from flask import Flask, request
import json
from random import randint

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

@APP.route('/channel/create', methods = ['POST'])
def channelsCreate(): 

    data = getData()    
    token = request.form.get('token')
    channel_name = request.form.get('name')
    is_public = request.form.get('is_public')
    valid_user = False
    
    # ValueError when name is more than 20 characters long as per the specs
    if len(channel_name) > 20: 
        raise ValueError("channel's name has exceeded 20 characters.")
   
    for users in data['users']:
        if users['token'] == token: 
            name_first = users['first_name']
            name_last = users['last_name']
            u_id = users['u_id']
            valid_user = True
    
    if valid_user == False: 
        raise ValueError("user's token not found in system.")
            
        
    
    # assuming that channel_id's are randomly generated
    channel_id = randint(0, 10000)
    channels_list = data['channels']
    channels_list.append({'channel_id' : channel_id,
        'channel_name' : channel_name,
        'is_public' : is_public,
        'owner_members' : [{'u_id' : u_id, 'name_first' : name_first, 'name_last' : name_last}],
        'all_members' : [{'u_id' : u_id, 'name_first' : name_first, 'name_last' : name_last}],
        'messages' : [{}]
    })
    updateData(data)
    return sendSuccess({'channel_id' : channel_id})
        
if __name__ == '__main__':
    APP.run(port = 7878)
        
        
        
        
        
        
        
