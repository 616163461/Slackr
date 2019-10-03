from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
import pytest

def test_channel_details(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    # SET UP END 
    
    assert channel_details(token, channel_id) = {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}], "all_members": [{}]}
    
    
def test_channel_details_bad(): 
    
    # SET UP BEGIN
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END 
    
    with pytest.raises(ValueError): 
        channel_details(token, "invalidchannel_id")
        
        
        
def test_channel_details_bad1(): 
    
    # SET UP BEGIN 
    #creating user1 and channel1
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    #creating user2 and channel2
    authRegisterDic1 = auth_register("validemail", "validpassword", "firstname", "lastname")
    token1 = authRegisterDic['token']
    u_id1 = authRegisterDic['u_id']
    channelsCreateDic1 = channels_create(token1, "validchannel1", True)
    channel_id1 = channelsCreateDic['channel_id']
    
    # SET UP END 
    with pytest.raises(AccessError): 
        channel_details("invalidtoken", channel_id)
        channel_details(token, channel_id1)
        channel_details(token1, channel_id)
        
