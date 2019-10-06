from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channel_leave import channel_leave
from f_auth_logout import auth_logout
import pytest

def test_channel_leave(): 
    
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
    
    channel_join(token1, channel_id)
    
    # assuming admin isn't in all_members list since admin was specifically isn't a member
    assert channel_details(token, channel_id) == {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}], "all_members": [{"u_id": u_id1, "name_first": "firstname1", "name_last": "lastname1"}]}
    
    channel_leave(token1, channel_id)
    
    # checking that token1 user left the channel
    assert channel_details(token, channel_id) = {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}], "all_members": [{}]}
    
    
def test_channel_leave_bad(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic1 = auth_register("valid@email1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    
    authRegisterDic2 = auth_register("valid@email2", "validpassword2", "firstname2", "lastname2")
    token2 = authRegisterDic2['token']
    u_id2 = authRegisterDic2['u_id']
    # SET UP END 
    
    channel_join(token1, channel_id)
    with pytest.raises(ValueError): 
        # calling function using invalid channel_id
        channel_leave(token1, "invalidchannel_id")
        # calling function on user who isn't part of the channel
        channel_leave(token2, channel_id)
        
    auth_logout(token1)
    with pytest.raises(ValueError): 
        # calling function using invalid token
        channel_leave(token1, channel_id)

