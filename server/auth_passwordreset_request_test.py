<<<<<<< HEAD
=======
# Function name: auth_passwordreset_request()
# Parameters:(email)
# Return type: {}
# Exception: N/A
# Description: Given an email address, if the user is a registered user, 
# send's them a an email containing a specific secret code, that when entered in auth_passwordreset_reset, 
# shows that the user trying to reset the password is the one who got sent this email.
#

import pytest
>>>>>>> daniel_branch
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channel_leave import channel_leave
from f_auth_logout import auth_logout
<<<<<<< HEAD
import pytest

def test_auth_passwordreset_request(): 

    # SET UP BEGIN 
=======

def test_auth_passwordreset_request(): 

    # SETUP BEGIN 
>>>>>>> daniel_branch
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
<<<<<<< HEAD
    # SET UP END 
    
    # calling function with valid email
    auth_passwordreset_request("valid@email")
    
    
    
    
def test_auth_passwordreset_request_bad(): 

    # SET UP BEGIN 
=======
    # SETUP END 
    
    # Testing function with valid email
    auth_passwordreset_request("valid@email")
    
    
def test_auth_passwordreset_request_bad(): 

    # SETUP BEGIN 
>>>>>>> daniel_branch
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
<<<<<<< HEAD
    # SET UP END 
    
    with pytest.raises(ValueError):
        # calling function with invalid email
        auth_passwordreset_request("invalidemail")
    
    
    
    
    
=======
    # SETUP END 
    with pytest.raises(ValueError):
        # Testing function with invalid email
        auth_passwordreset_request("invalidemail")
    
>>>>>>> daniel_branch
