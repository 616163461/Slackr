# Function name: channels_listall()
# Parameters: (token)
# Return type: { channels }
# Description: Provide a list of all channels (and their associated details)
#
from flask import Flask, request
import json


APP = Flask(__name__)

def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

# converting dictionary into string for flask
def sendSuccess(data):
    return json.dumps(data)
    

@APP.route('/channel/listall', methods=['GET'])
def channels_listall():
    token = request.args.get('token')
    data_new = getData()
    
    flag = 0
    #Test for valid token
    for i in data_new['users']:
        if i['token'] == token and token != None:
            u_id = i['u_id']
            flag = 1
    if flag == 0:
        raise ValueError("Session has expired. Please refresh the page and login\n")
    
    answer = []
    for channels in data_new['channels']:
        temp = {}
        temp['name'] = channels['channel_name']
        temp['channel_id'] = channels['channel_id']
        answer.append(temp)
   
    return sendSuccess(answer)
         

if __name__ == '__main__':
    APP.run(port = 7878)
    

