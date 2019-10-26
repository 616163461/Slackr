# Fumction name: echo_post()
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

@APP.route('/echo/post', methods = ['POST'])    
def echo_post():
    answer = {}
    echo = request.form.get('echo')
    answer['echo'] = echo
    return sendSuccess(answer)

if __name__ == '__main__':
    APP.run(port = 7220)
    

