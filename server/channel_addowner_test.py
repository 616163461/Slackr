# Function name: channel_addowner()
# Parameters: (token, channel_id, u_id)
# Return type: {}
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# - When user with user id u_id is already an owner of the channel
# AccessError when:
# - the authorised user is not an owner of the slackr, or an owner of this channel
# Description: Make user with user id u_id an owner of this channel
#

import pytest
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channel_leave import channel_leave
from f_channels_list import channels_list
from f_auth_logout import auth_logout
from f_channel_addowner import channel_addowner
from myexcept import ValueError
from json_clean import jsonClean
import json

# retrieve data from local data base 
def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data


def test_channel_addowner(): 
    jsonClean()
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid9@email.com", "valid9password", "first9name", "last9name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("valid6@email.com", "valid6password1", "first6name1", "last6name1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    
    authRegisterDicTwo = auth_register("valid10@email.com", "validpassword2", "firstname2", "lastname2")
    token_two = authRegisterDicTwo['token']
    u_id_two = authRegisterDicTwo['u_id']
    # SETUP END 
    
    with pytest.raises(ValueError): 
        # Testing function with member token to confirm he's not an owner
        channel_addowner(token_one, channel_id, u_id_two)
    
    # Making token_one an owner
    channel_addowner(token, channel_id, u_id_one)
    
    # checking output matches local data base
    data = getData()
    for channels in data['channels']:
        if channels['channel_id'] == channel_id:
            assert channels['owner_members'] == [{"u_id": u_id, "name_first": "first9name", "name_last": "last9name"}, {"u_id": u_id_one, "name_first": "first6name1", "name_last": "last6name1"}]
            

    # Testing function with recently declared owner (token_one) to check if he has owner permissions
    assert channel_addowner(token_one, channel_id, u_id_two) == {}
    
    # checking output matches local data base
    data = getData()
    for channels in data['channels']:
        if channels['channel_id'] == channel_id:
            assert channels['owner_members'] == [{"u_id": u_id, "name_first": "first9name", "name_last": "last9name"}, {"u_id": u_id_one, "name_first": "first6name1", "name_last": "last6name1"}, {"u_id": u_id_two, "name_first": "firstname2", "name_last": "lastname2"}]
            
    
def test_channel_addowner_bad(): 
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
    
    authRegisterDicThree = auth_register("valid4@email.com", "validpassword3", "firstname3", "lastname3")
    token_three = authRegisterDicThree['token']
    u_id_three = authRegisterDicThree['u_id']
    
    authRegisterDicFour = auth_register("valid5@email.com", "validpassword4", "firstname4", "lastname4")
    token_four = authRegisterDicFour['token']
    u_id_four = authRegisterDicFour['u_id']
    # SETUP END 
    with pytest.raises(ValueError):
        # Testing function with invalid channel_id
        channel_addowner(token, "invalidchannel_id", u_id_one)
        
    channel_addowner(token, channel_id, u_id_one)
    with pytest.raises(ValueError):
        # Testing function on a user who's already an owner
        channel_addowner(token, "invalidchannel_id", u_id_one)
    
        # Testing function with a user who isn't an owner
        channel_addowner(token_two, channel_id, u_id_three)
   
    auth_logout(token)
    with pytest.raises(ValueError): 
        # Testing function on an invalid token 
        channel_addowner(token, channel_id, u_id_four)
