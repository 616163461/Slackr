# Function: auth_logout()
# Parameters: (token)
# Return type: {}
# Exception: N/A
# Description: Given an active token, invalidates the taken to log the user out. Given a non-valid token, does nothing
#

import pytest
from f_auth_login import auth_login
from f_auth_register import auth_register
from f_auth_logout import auth_logout


def test_auth_logout(): 
    # SETUP BEGIN
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    # SETUP END
    
    with pytest.raises(ValueError): 
        # Testing login function with user which hasn't been logged out
        auth_login("validemail", "validpassword")
        
    auth_logout(token)
    # Testing login function with logged out user to check he's succesfully logged out 
    auth_login("validemail", "validpassword")
    
    auth_logout(token)
    # Testing logout function with a logged out user 
    assert auth_logout(token) == {}
