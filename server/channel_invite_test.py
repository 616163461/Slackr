import pytest
from f_channel_invite import channel_invite
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_auth_logout import auth_logout
from f_channel_details import channel_details

def test_channel_invite(): 
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic1 = auth_register("valid@email1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    # SET UP END 
    
    channel_invite(token, channel_id, u_id1)
    # asserting that the invited user is now a member of the channel
    assert channel_details(token1, channel_id) == {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}], "all_members": [{"u_id": u_id, "name_first": "firstname1", "name_last": "lastname1"}]}
    # calling leave to check that he's a member of the channel
    channel_leave(token1, channel_id)
    
def test_channel_invite_bad(): 
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
    
    authRegisterDic2 = auth_register("valid@email2", "validpassword2", "firstname2", "lastname2")
    token2 = authRegisterDic2['token']
    u_id2 = authRegisterDic2['u_id']
    # SET UP END 
    
    with pytest.raises(ValueError): 
        # calling function with invalid channel_id
        channel_invite(token, "invalidchannel_id", u_id1)
        # calling function with channel_id which the authorised user isn't a member of
        channel_invite(token, channel_id1, u_id2)
        # calling function with an invalid u_id
        channel_invite(token, channel_id, "invalidu_id")
        
    auth_logout(token1)
    with pytest.raises(ValueError): 
        # calling function with invalid token
        channel_invite(token1, channel_id1, u_id2)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
