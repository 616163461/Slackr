from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_auth_logout import auth_logout
import pytest

def test_channel_details(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    # SET UP END 
    
    assert channel_details(token, channel_id) == {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}], "all_members": [{}]}
    
    
def test_channel_details_bad(): 
    
    # SET UP BEGIN
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic1 = auth_register("valid@email1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    channelsCreateDic1 = channels_create(token1, "validchannel1", True)
    channel_id1 = channelsCreateDic1['channel_id']
    # SET UP END 
    
    with pytest.raises(ValueError): 
        # calling function with invalid channel_id
        channel_details(token, "invalidchannel_id")
        # calling function with unauthorised user
        channel_details(token, channel_id1)

        
    auth_logout(token)
    with pytest.raises(ValueError): 
        # calling function with invalid token
        channel_details(token, channel_id)
        
        
