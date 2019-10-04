from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channet_leave import channel_leave
from f_channels_list import channels_list
from f_auth_logout import auth_logout
import pytest

def test_channel_addowner(): 
    
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
    
    with pytest.raises(ValueError): 
        # calling function with member token to confirm he's not an owner
        channel_addowner(token1, channel_id, u_id2)
    
    # make token1 an owner
    channel_addowner(token, channel_id, u_id1)
    
    # calling function with recently declared owner (token1) to check if he has owner permissions
    assert channel_addowner(token1, channel_id, u_id2) == {}
    
def test_channel_addowner_bad(): 
    
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
    
    authRegisterDic4 = auth_register("validemail4", "validpassword4", "firstname4", "lastname4")
    token4 = authRegisterDic4['token']
    u_id4 = authRegisterDic4['u_id']
    # SET UP END 
    
    with pytest.raises(ValueError):
        # calling function with invalid channel_id
        channel_addowner(token, "invalidchannel_id", u_id1)
        
    channel_addowner(token, channel_id, u_id1)
    with pytest.raises(ValueError):
        # calling function on a user who's already an owner
        channel_addowner(token, "invalidchannel_id", u_id1)
    
        # calling function with a user who isn't an owner
        channel_addowner(token2, channel_id, u_id3)
   
    auth_logout(token)
    with pytest.raises(ValueError): 
        # calling function on an invalid token 
        channel_addowner(token, channel_id, u_id4)
    
    
    
    
    
    
    
    
    
    
    
