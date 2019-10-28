# Function name: auth_passwordreset_request()
# Parameters:(email)
# Return type: {}
# Exception: N/A
# Description: Given an email address, if the user is a registered user, 
# send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, 
# shows that the user trying to reset the password is the one who got sent this email.
#

import pytest
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channel_leave import channel_leave
from f_auth_logout import auth_logout
from f_auth_passwordreset_request import auth_passwordreset_request
from myexcept import ValueError

def test_auth_passwordreset_request(): 

    # SETUP BEGIN 
    
    authRegisterDic = auth_register("valid14@email.com", "valid14password", "first14name", "last14name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SETUP END 
    
    # Testing function with valid email
    auth_passwordreset_request("valid14@email.com")
    
    
def test_auth_passwordreset_request_bad(): 

    # SETUP BEGIN 

    authRegisterDic = auth_register("valid15@email.com", "valid15password", "first15name", "last15name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SETUP END 
    
    with pytest.raises(ValueError):
        # Testing function with invalid email
        auth_passwordreset_request("invalidemail")