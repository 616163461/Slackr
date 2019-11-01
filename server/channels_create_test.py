# Function name: channels_create()
# Parameters: (token, name, is_public)
# Return type: { channel_id }
# Exception: ValueError when:
# - Name is more than 20 characters long
# Description: Creates a new channel with that name that is either a public or private channel
#

import pytest
from f_channels_create import channels_create
from f_auth_register import auth_register
from f_auth_logout import auth_logout
from myexcept import ValueError
from json_clean import jsonClean
import myexcept
import json

# retrieve data from local data base 
def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data


def test_channels_create(): 
    jsonClean()
    # SETUP BEGIN 
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SETUP END 
    
    channels_create(token, "validchannel", True) 
    
    channel_found = False
    data = getData()
    for channels in data['channels']:
        if channels['channel_name'] == 'validchannel':
             channel_found = True
    
    assert channel_found == True
        
    assert channels_create(token, "validchannel1", False) == {'channel_id': "validchannel1"}
    
    channel2_found = False
    data = getData()
    for channels in data['channels']:
        if channels['channel_name'] == 'validchannel1':
             channel2_found = True
    
    assert channel2_found == True
    
def test_channels_create_bad():
   
    jsonClean() 
    # SETUP BEGIN 
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SETUP END 
    with pytest.raises(ValueError): 
        # Testing function with public channel_name which is too long 
        channels_create(token, "this name is way too long so it will cause an error", True)
        # Testing function with private channel name which is too long
        channels_create(token, "this name is way too long so it will cause an error", False)
        
        
    auth_logout(token)
    with pytest.raises(ValueError): 
        # Testing function with invalid token to create public channel
        channels_create(token, "validchannel", True)
        # Testing function with invalid token to create private channel
        channels_create(token, "validchannel", False)
