# Function name: channels_list()
# Parameters: (token)
# Return type: { channels }
# Exception: N/A
# Description: Provide a list of all channels (and their associated details) that the authorised user is part of
#

import pytest
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channel_leave import channel_leave
from f_channels_list import channels_list
from f_auth_logout import auth_logout
import json

# retrieve data from local data base 
def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data


def test_channels_list(): 
    
    # SETUP BEGIN 
    
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("validemail1@gmail.com", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    
    # SETUP END
    
    # Testing function using authorised user
    assert channels_list(token) == [{channels: {channel_id: "validchannel"}}]
    
    for channels in data['channels']:
        assert channels == {'channel_id' : channel_id, 'channel_name' : "validchannel", 'is_public' : True, 'owner_members' : [{'u_id' : u_id, 'name_first' : name_first,'name_last' : name_last}], 'all_members' : [{'u_id' : u_id, 'name_first' : name_first,'name_last' : name_last}], 'messages' : []}
            

def test_channels_list_bad(): 
    
    # SETUP BEGIN 
    authRegisterDic = auth_register("invalidemail", "invalidpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    # SETUP END 

    auth_logout(token)
    with pytest.raises(ValueError):
        # Testing function using invalid token 
        channels_list(token)
