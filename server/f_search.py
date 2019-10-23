# Function: search()
# Parameter: (token, query_str)
# Output: { messages }
# Exception: N/A
# Description: Given a query string, return a collection of messages that match the query
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
    
    
@APP.route('/search', methods = ['GET'])   
def search():
    token = request.args.get('token')
    query_str = request.args.get('query_str')
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
    #search through channels, find the channels that the user is in
    for j in data_new['channels']:
        for members in j['all_members']:
            if members['u_id'] == u_id:
                #This is a channel that the user is in
                for messages in j['messages']:
                    if query_str in messages['message']:
                        answer.append(messages)
                        
    
                
                
    #search through all messages and find prefix (if contains)
    return sendSuccess(answer)


if __name__ == '__main__':
    APP.run(port = 7878)

