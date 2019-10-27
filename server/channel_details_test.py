# Function name: channel_details()
# Parameters: (token, channel_id)
# Return type: { name, owner_members, all_members }
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# AccessError when:
# - Authorised user is not a member of channel with channel_id
# Description: Given a Channel with ID channel_id that the authorised user is part of, provide basic details about the channel
#

import pytest
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_auth_logout import auth_logout
import json
# retrieve data from local data base 
def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

def test_channel_details(): 
    
    # SET UP BEGIN 

    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    # SETUP END 
    
    # checking output of channel_details matches our data base
    data = getData()
    for channels in data['channels']:
        if channels['channel_id'] == channel_id:
            assert channel_details(token, channel_id) == channels
    
    
    
def test_channel_details_bad(): 
    
    # SET UP BEGIN
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("valid2@email.com", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    channelsCreateDicOne = channels_create(token_one, "validchannel1", True)
    channel_id_one = channelsCreateDicOne['channel_id']
    # SETUP END 
    
    with pytest.raises(ValueError): 
        # Testing function with invalid channel_id
        channel_details(token, "invalidchannel_id")
        # Testing function with unauthorised user
        channel_details(token, channel_id_one)
