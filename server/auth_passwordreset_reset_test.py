from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channet_leave import channel_leave
from f_channels_list import channels_list
from f_auth_logout import auth_logout
from f_channel_addowner import channel_addowner
from f_auth_passwordreset_reset import auth_passwordreset_reset
import pytest

def test_auth_passwordreset_reset(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END 
    
    auth_passwordreset_request("valid@email")
    
    # I don't have anyway of getting the reset_code so I can't test this
    auth_passwordreset_reset("reset_code", "new_password")


def test_auth_passwordreset_reset(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END 
    
    auth_passwordreset_request("valid@email")
    
    with pytest.raises(ValueError):     
        # calling function with invalid reset code
        auth_passwordreset_reset("invalid_reset_code", "new_password")
        # calling function with invalid password
        auth_passwordreset_reset("reset_code", "ivp")
        
