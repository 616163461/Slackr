# Function name: channel_join()
# Parameters: (token, channel_id)
# Return type: {}
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# AccessError when:
# - channel_id refers to a channel that is private (when the authorised user is not an admin)
# Description: Given a channel_id of a channel that the authorised user can join, adds them to that channel
#

import pytest
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_auth_logout import auth_logout
import json

# retrieve data from local data base 
def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data


def test_channel_join(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid100@email.com", "validpassword", "first100name", "last100name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("valid2@email.com", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    # SETUP END 
    
    channel_join(token_one, channel_id)
    
    # checking output matches local data base
    data = getData()
    for channels in data['channels']:
        if channels['channel_id'] == channel_id:
            assert channels['all_members'] == [{"u_id": u_id, "name_first": "first100name", "name_last": "last100name"}, {"u_id": u_id_one, "name_first": "firstname1", "name_last": "lastname1"}]
    
    # Assuming admin isn't in all_members list since admin was specifically isn't a member
    assert channel_details(token, channel_id) == {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "first100name", "name_last": "last100name"}], "all_members": [{"u_id": u_id, "name_first": "first100name", "name_last": "last100name"}, {"u_id": u_id_one, "name_first": "firstname1", "name_last": "lastname1"}]}

    
def test_channel_join_bad(): 
   
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid10@email.com", "validpassword", "first10name", "last10name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", False)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("valid20@email.com", "validpassword1", "first20name1", "last20name1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    # SETUP END 
    '''
    with pytest.raises(ValueError): 
        # Testing function with invalid channel_id
        channel_join(token_one, "invalidchannel_id")
        # Testing function with unauthorised token when channel is private
        channel_join(token_one, channel_id)
    
    # Invalidate token
    auth_logout(token_one)
    
    with pytest.raises(ValueError): 
        # Testing function with invalid token
        channel_join(token_one, channel_id)
    '''
