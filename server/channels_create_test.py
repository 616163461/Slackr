# Function name: channels_create()
# Parameters: (token, name, is_public)
# Return type: { channel_id }
# Exception: ValueError when:
# - Name is more than 20 characters long
# Description: Creates a new channel with that name that is either a public or private channel
#

import pytest
from f_channels_create import channels_create
from f_auth_register import auth_register
from f_auth_logout import auth_logout
<<<<<<< HEAD


def test_channels_create(): 
    
    # SETUP BEGIN 
=======
import pytest

def test_channels_create(): 
    
    # SET UP BEGIN 
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
<<<<<<< HEAD
    # SETUP END 
=======
    # SET UP END 
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
    
    assert channels_create(token, "validchannel", True) == {channel_id: "validchannel"}
    assert channels_create(token, "validchannel1", False) == {channel_id: "validchannel1"}
    
def test_channels_create_bad():
   
<<<<<<< HEAD
    # SETUP BEGIN 
=======
    # SET UP BEGIN 
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
<<<<<<< HEAD
    # SETUP END 
    
    with pytest.raises(ValueError): 
        # Testing function with public channel_name which is too long 
        channels_create(token, "this name is way too long so it will cause an error", True)
        # Testing function with private channel name which is too long
=======
    # SET UP END 
    
    with pytest.raises(ValueError): 
        # calling function with public channel_name which is too long 
        channels_create(token, "this name is way too long so it will cause an error", True)
        # calling function with private channel name which is too long
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
        channels_create(token, "this name is way too long so it will cause an error", False)
        
        
    auth_logout(token)
    with pytest.raises(ValueError): 
<<<<<<< HEAD
        # Testing function with invalid token to create public channel
        channels_create(token, "validchannel", True)
        # Testing function with invalid token to create private channel
        channels_create(token, "validchannel", False)

=======
        # calling function with invalid token to create public channel
        channels_create(token, "validchannel", True)
        # calling function with invalid token to create private channel
        channels_create(token, "validchannel", False)
        
        
        
        
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
