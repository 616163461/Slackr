from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channet_leave import channel_leave
from f_channels_list import channels_list
from f_auth_logout import auth_logout
import pytest

def test_channels_listall(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    channelsCreateDic1 = channels_create(token, "validchannel1", False)
    channel_id1 = channelsCreateDic1['channel_id']
    
    channelsCreateDic2 = channels_create(token, "validchannel2", True)
    channel_id2 = channelsCreateDic2['channel_id']
    
    channelsCreateDic3 = channels_create(token, "validchannel3", True)
    channel_id3 = channelsCreateDic3['channel_id']
    # SET UP END
    
    # calling function using authorised user
    assert channels_listall(token) = [{channels: {channel_id: "validchannel"}}, {channels: {channel_id1: "validchannel1"}}, {channels: {channel_id2: "validchannel2"}}, {channels: {channel_id3: "validchannel3"}}]
    
 
def test_channels_listall_bad(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    channelsCreateDic1 = channels_create(token, "validchannel1", False)
    channel_id1 = channelsCreateDic1['channel_id']
    
    channelsCreateDic2 = channels_create(token, "validchannel2", True)
    channel_id2 = channelsCreateDic2['channel_id']
    
    channelsCreateDic3 = channels_create(token, "validchannel3", True)
    channel_id3 = channelsCreateDic3['channel_id']
    
    # SET UP END 
    
    
    auth_logout(token)
    with pytest.raises(ValueError):
        # calling function using invalid token 
        channels_list(token)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
