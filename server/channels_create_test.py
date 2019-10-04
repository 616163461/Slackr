from f_channels_create import channels_create
from f_auth_register import auth_register
from f_auth_logout import auth_logout
import pytest

def test_channels_create(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END 
    
    assert channels_create(token, "validchannel", True) == {channel_id: "validchannel"}
    assert channels_create(token, "validchannel1", False) == {channel_id: "validchannel1"}
    
def test_channels_create_bad():
   
    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END 
    
    with pytest.raises(ValueError): 
        # calling function with public channel_name which is too long 
        channels_create(token, "this name is way too long so it will cause an error", True)
        # calling function with private channel name which is too long
        channels_create(token, "this name is way too long so it will cause an error", False)
        
        
    auth_logout(token)
    with pytest.raises(ValueError): 
        # calling function with invalid token to create public channel
        channels_create(token, "validchannel", True)
        # calling function with invalid token to create private channel
        channels_create(token, "validchannel", False)
        
        
        
        
