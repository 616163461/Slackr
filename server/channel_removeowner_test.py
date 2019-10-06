from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channet_leave import channel_leave
from f_channels_list import channels_list
from f_auth_logout import auth_logout
from f_channel_removeowner import channel_removeowner
from f_channel_addowner import channel_addowner
import pytest

def test_channel_removeowner():
    
    # SET UP BEGIN
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic1 = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    
    authRegisterDic2 = auth_register("validemail2", "validpassword2", "firstname2", "lastname2")
    token2 = authRegisterDic2['token']
    u_id2 = authRegisterDic2['u_id']
    # SET UP END
    
    # adding user1 as an owner
    channel_addowner(token, channel_id, u_id1)
    # removing user1 as an owner
    channel_removeowner(token, channel_id, u_id1)
    # calling function with recently removed owner to check he's not an owner
    channel_addowner(token1, channel_id, u_id2)
    
def test_channel_removeowner_bad():
    # SET UP BEGIN
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic1 = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    
    authRegisterDic2 = auth_register("validemail2", "validpassword2", "firstname2", "lastname2")
    token2 = authRegisterDic2['token']
    u_id2 = authRegisterDic2['u_id']
    
    authRegisterDic3 = auth_register("validemail3", "validpassword3", "firstname3", "lastname3")
    token3 = authRegisterDic3['token']
    u_id3 = authRegisterDic3['u_id']
    # SET UP END
    channel_addowner(token, channel_id, u_id1)
    
    with pytest.raises(ValueError): 
        # calling function with invalid channel_id
        channel_removeowner(token, "invalidchannel_id", u_id1)
        # calling function removing a user who isn't an owner
        channel_removeowner(token, channel_id, u_id2)
        # calling function with a user who isn't an owner
        channel_removeowner(token2, channel_id, u_id3)
        
    auth_logout(token)
    with pytest.raises(ValueError): 
        # calling function with invalid token
        channel_removeowner(token, channel_id, u_id1)
    
    
    
    
    
    
    
    
    
    
    
    
    
