# Function name: channel_leave()
# Parameters: (token, channel_id)
# Return type: {}
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# Description: Given a channel ID, the user removed as a member of this channel
#

import pytest
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channel_leave import channel_leave
from f_auth_logout import auth_logout
from myexcept import ValueError
from json_clean import jsonClean
import json

# retrieve data from local data base 
def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

def test_channel_leave(): 
    jsonClean()
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("valid2@email.com", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    # SETUP END
    
    channel_join(token_one, channel_id)
    
    # assuming admin isn't in all_members list since admin was specifically isn't a member
    assert channel_details(token, channel_id) == {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}], "all_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}, {"u_id": u_id_one, "name_first": "firstname1", "name_last": "lastname1"}]}
    
    channel_leave(token_one, channel_id)
    
    # checking output matches local data base
    data = getData()
    for channels in data['channels']:
        if channels['channel_id'] == channel_id:
            assert channels['all_members'] == [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}]
            
            
    # checking that token1 user left the channel
    assert channel_details(token, channel_id) == {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}], "all_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}]}
    
    
def test_channel_leave_bad(): 
    
    jsonClean()
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("valid2@email.com", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    
    authRegisterDicTwo = auth_register("valid3@email.com", "validpassword2", "firstname2", "lastname2")
    token_two = authRegisterDicTwo['token']
    u_id_two = authRegisterDicTwo['u_id']
    # SETUP END 
    channel_join(token_one, channel_id)
    with pytest.raises(ValueError): 
        # Testing function using invalid channel_id
        channel_leave(token_one, "invalidchannel_id")
        # Testing function on user who isn't part of the channel
        channel_leave(token_two, channel_id)
        
    auth_logout(token_one)
    with pytest.raises(ValueError): 
        # Testing function using invalid token
        channel_leave(token_one, channel_id)