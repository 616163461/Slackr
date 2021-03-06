# Function name: auth_passwordreset_reset()
# Parameters:(reset_code, new_password)
# Return type: {}
# Exception:  ValueError when:
# - reset_code is not a valid reset code
# - Password entered is not a valid password
# Description: Given a reset code for a user, set that user's new password to the password provided
#

import pytest
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channel_leave import channel_leave
from f_channels_list import channels_list
from f_auth_logout import auth_logout
from f_channel_addowner import channel_addowner
from f_auth_passwordreset_reset import auth_passwordreset_reset
from f_auth_passwordreset_request import auth_passwordreset_request
from myexcept import ValueError
from json_clean import jsonClean

def test_auth_passwordreset_reset(): 
    jsonClean()
    # SETUP BEGIN 
    
    authRegisterDic = auth_register("valid@16email,com", "valid16password", "first16name", "last16name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SETUP END 
    
    auth_passwordreset_request("valid16@email.com")
    
    # setting password 
    auth_passwordreset_reset("first16namelast16name", "new_password")
    
    # checking I can log in with the new password
    auth_login("valid16@email.com", "new_password")


def test_auth_passwordreset_reset_bad(): 
    jsonClean()
    # SETUP BEGIN 

    authRegisterDic = auth_register("valid17@email.com", "valid17password", "first17name", "last17name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SETUP END 
    
    auth_passwordreset_request("valid17@email.com")
    
    with pytest.raises(ValueError):     
        # Testing function with invalid reset code
        auth_passwordreset_reset("invalid_reset_code", "new_password")
        # Testing function with invalid password
        auth_passwordreset_reset("reset_code", "ivp")
