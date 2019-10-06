from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channel_leave import channel_leave
from f_auth_logout import auth_logout
import pytest

def test_auth_passwordreset_request(): 

    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END 
    
    # calling function with valid email
    auth_passwordreset_request("valid@email")
    
    
    
    
def test_auth_passwordreset_request_bad(): 

    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END 
    
    with pytest.raises(ValueError):
        # calling function with invalid email
        auth_passwordreset_request("invalidemail")
    
    
    
    
    
