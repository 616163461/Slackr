# Function name: channel_messages()
# Parameters: (token, channel_id, start)
# Return type: { messages, start, end }
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# - start is greater than the total number of messages in the channel
# AccessError when:
# - Authorised user is not a member of channel with channel_id
# Description: Given a Channel with ID channel_id that the authorised user is part of, 
# return up to 50 messages between index "start" and "start + 50". 
# Message with index 0 is the most recent message in the channel. 
# This function returns a new index "end" which is the value of "start + 50", 
# or, if this function has returned the least recent messages in the channel, 
# returns -1 in "end" to indicate there are no more messages to load after this return.
#

import json
from flask import Flask, request

APP = Flask(__name__)


def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

# converting dictionary into string for flask
def sendSuccess(data):
    return json.dumps(data)
    
    
@APP.route('/channel/messages', methods = ['GET'])
def channel_messages():
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    start = request.args.get('start')
    data = getData()
    send_Success = False
    for channel in data['channels']:
        if str(channel['channel_id']) == channel_id:
            for message in channel['messages']:
                messages = channel['messages']
                end = 50 + int(start)
                send_Success = True
                end2 = end
                if end == 50:
                    end2 = -1
                return sendSuccess({'messages' : messages[int(start):end], 'start' : start, 'end' : end2})
                
    if send_Success == False:
        raise ValueError("No such channel_id was found.")
                    
if __name__ == "__main__":
    APP.run(port = 7878)                            
                    
                    
                    
                    
                    
                    
