# Fumction name: echo_get()
# Parameters: (echo)
# Return type: {echo}
# Exception: None
# Description: Returns the input
#

from flask import Flask, request
from json import dumps

APP = Flask(__name__)

def sendSuccess(data):
    return dumps(data)

@APP.route('/echo/get', methods = ['GET'])    
def echo_get():
    answer = {}
    echo = request.args.get('echo')
    answer['echo'] = echo
    return sendSuccess(answer)

if __name__ == '__main__':
    APP.run(port = 7220)
    

