from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
import pytest

def test_channel_join(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic['token']
    u_id1 = authRegisterDic['u_id']
    # SET UP END 
    
    channel_join(token1, channel_id)
    #assuming admin isn't in all_members list since admin was specifically isn't a member
    assert channel_details(token, channel_id) == {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}], "all_members": [{"u_id": u_id1, "name_first": "firstname1", "name_last": "lastname1"}]}
    
    
def test_channel_join_bad(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    authRegisterDic = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic['token']
    u_id1 = authRegisterDic['u_id']
    # SET UP END 
    
    with pytest.raises(ValueError): 
        channel_details(token, "invalidchannel_id")
        
def test_channel_join_bad1(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", False)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic['token']
    u_id1 = authRegisterDic['u_id']
    # SET UP END 
    
    with pytest.raises(AccessError): 
        channel_details(token1, channel_id)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
