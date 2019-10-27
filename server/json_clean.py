import json
import sys

def resetData(data):
    with open('export.json', 'w') as FILE:
        FILE.seek(0)
        FILE.truncate()
        json.dump(data, FILE)
    return 0

def jsonClean():
    resetData({"users": [{"token": "CIMICTOP1012345abcd", "handle_str": "Sohyun's bf", "first_name": "Geoffrey", "last_name": "Lee", "password": "4be954de7863e836a1bb4bf6ec57b3f005efb6bc371975d13fffa50a7f390b0a", "email": "geoffrey.he777@gmail.com", "u_id": 24, "permission_id": 2, "pass_reset_code": None}, {"token": None, "handle_str": "DanielKang", "first_name": "Daniel", "last_name": "Kang", "password": "a40af595e0c3d5cf0fe69e4c3f992b72f106282bdfa578f415e7e77ae3653d90", "email": "dynewemail@gmail.com", "u_id": 89, "permission_id": 3, "pass_reset_code": None}, {"token": "RichardJiang", "handle_str": "RichardJiang", "first_name": "Richard", "last_name": "Jiang", "password": "4eff7521de5bbd398dd2180bd4735648665f559a339ea3194b44d1eea50b8818", "email": "RichardKang@gmail.com", "u_id": 12, "permission_id": 2, "pass_reset_code": None}, {"token": "MattMa", "handle_str": "MattMa", "first_name": "Matt", "last_name": "Ma", "password": "1d893656a13f7ad7cdbac69ba56fa11de5d56fe89d251df497bf559ec571e5c5", "email": "JackMa@gmail.com", "u_id": 13, "permission_id": 3, "pass_reset_code": None}, {"token": "EricZhang", "handle_str": "EricZhang", "first_name": "Eric", "last_name": "Zhang", "password": "6b622167179cf64ed5732f3ed72919539acd73dea15768b35d316cbfe6e21194", "email": "EricZhang@gmail.com", "u_id": 30, "permission_id": 3}], "channels": [{"channel_id": 6666, "channel_name": "PSchannel", "is_public": "True", "owner_members": [{"u_id": 12, "name_first": "Richard", "name_last": "Jiang"}], "all_members": [{"u_id": 12, "name_first": "Richard", "name_last": "Jiang"}, {"u_id": "13", "name_first": "Matt", "name_last": "Ma"}], "messages": [{"message_id": 208943, "u_id": 12, "message": "Imagine having to takevalid 2 days off work to finish iteration 2... nvm I can't even say it !!!!!!!!", "time_created": "12:04", "reacts": [], "is_pinned": False}, {"message_id": 1, "u_id": 12, "message": "Good team mates were invented 2018, Thom_Clowne 2019 >:(", "time_created": "12:04", "reacts": {}, "is_pinned": False}]}, {"channel_id": 1533, "channel_name": "Thom&Jerry", "is_public": "False", "owner_members": [{"u_id": 12, "name_first": "Richard", "name_last": "Jiang"}], "all_members": [{"u_id": 12, "name_first": "Richard", "name_last": "Jiang"}], "messages": []}]})
    return 0
    
    
jsonClean()