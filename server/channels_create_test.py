from f_channels_create import channels_create
from f_auth_register import auth_register
import pytest

def test_channels_create(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END 
    
    assert channels_create(token, "validchannel", True) == {channel_id: "validchannel"}

    
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
        
        
        
        
        
