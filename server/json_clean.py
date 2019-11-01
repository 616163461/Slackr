import json
import sys

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
