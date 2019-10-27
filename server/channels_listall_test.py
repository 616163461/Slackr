# Function name: channels_list()
# Parameters: (token)
# Return type: { channels }
# Exception: N/A
# Description: Provide a list of all channels (and their associated details)
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



def test_channels_listall(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    channelsCreateDicOne = channels_create(token, "validchannel1", False)
    channel_id_one = channelsCreateDicOne['channel_id']
    
    channelsCreateDicTwo = channels_create(token, "validchannel2", True)
    channel_id_two = channelsCreateDicTwo['channel_id']
    
    channelsCreateDicThree = channels_create(token, "validchannel3", True)
    channel_id_three = channelsCreateDic_three['channel_id']
    # SETUP END
    
    # Testing function using authorised user
    assert channels_listall(token) == [{channels: {channel_id: "validchannel"}}, {channels: {channel_id_one: "validchannel1"}}, {channels: {channel_id_two: "validchannel2"}}, {channels: {channel_id_three: "validchannel3"}}]

 
def test_channels_listall_bad(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    channelsCreateDicOne = channels_create(token, "validchannel1", False)
    channel_id_one = channelsCreateDicOne['channel_id']
    
    channelsCreateDicTwo = channels_create(token, "validchannel2", True)
    channel_id_two = channelsCreateDic2['channel_id']
    
    channelsCreateDicThree = channels_create(token, "validchannel3", True)
    channel_id_three = channelsCreateDicThree['channel_id']
    
    # SETUP END 
    
    # Invalidating token
    auth_logout(token)
    with pytest.raises(ValueError):
        # Testing function using invalid token 
        channels_list(token)
        