import json
import sys
import os

data = {
    'users' : [],
    'channels' : []
}

def getData():
    with open('export.json', 'r') as FILE:
        if os.stat('export.json').st_size == 0:
            data = {
                'users' : [],
                'channels' : []
            }
        else:
            data = json.load(FILE)
    return data

# converting dictionary into string for flask
def sendSuccess(data):
    return json.dumps(data)

def updateData(data):
    with open('export.json', 'w') as FILE:
        json.dump(data, FILE)
    return 0

def resetData(data):
    with open('export.json', 'w') as FILE:
        FILE.seek(0)
        FILE.truncate()
        json.dump(data, FILE)
    return 0

def jsonClean():
    resetData({'users': [], 'channels': []})
    return 0
    
jsonClean()

def data_test_initiate():
    jsonClean()

    data = getData()
    
    return data
